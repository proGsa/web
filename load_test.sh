#!/usr/bin/env bash
# ========================================
# Нагрузочное тестирование TravelGuide API с ApacheBench
# ========================================

OUTPUT_DIR="./load_test_results"
mkdir -p "$OUTPUT_DIR"

# Эндпоинты
GET_ENDPOINTS=(
    "http://localhost/api/v1/health"
    "http://localhost/api/v2/health"
)

POST_ENDPOINT="http://localhost/api/v2/cities/"
DELETE_ENDPOINT="http://localhost/api/v2/cities"  # ← сюда DELETE запросы

# Параметры ab
TOTAL_REQUESTS=100
CONCURRENCY=10

# ----------------------
# Функция запуска ab
# ----------------------
run_ab_test() {
    local method=$1
    local url=$2
    local outfile=$3
    local postdata=$4

    echo "=== $method $url ===" >> "$outfile"

    if [ "$method" = "GET" ]; then
        ab -n $TOTAL_REQUESTS -c $CONCURRENCY "$url" 2>&1 | tee -a "$outfile"
    elif [ "$method" = "POST" ]; then
        echo "$postdata" > /tmp/post.json
        ab -n 1 -c 1 -p /tmp/post.json -T application/json "$url" 2>&1 | tee -a "$outfile"
        rm -f /tmp/post.json
    fi
}

# ----------------------
# Генерация Markdown отчета
# ----------------------
generate_md_report() {
    local report_file="$OUTPUT_DIR/load_test_report.md"
    echo "# Отчет по нагрузочному тестированию TravelGuide API" > "$report_file"
    echo "Дата: $(date)" >> "$report_file"
    echo "" >> "$report_file"

    for file in "$OUTPUT_DIR"/*.txt; do
        local title=$(basename "$file" .txt)
        echo "## $title" >> "$report_file"
        echo '```' >> "$report_file"
        cat "$file" >> "$report_file"
        echo '```' >> "$report_file"
        echo ""
    done

    echo "Отчет сформирован: $report_file"
}

# ======================
# GET тесты
# ======================
for url in "${GET_ENDPOINTS[@]}"; do
    FILENAME="$OUTPUT_DIR/GET_$(echo $url | sed 's|http://||;s|/|_|g').txt"
    run_ab_test "GET" "$url" "$FILENAME"
done

# ======================
# POST тесты с уникальными городами
# ======================
POST_OUTFILE="$OUTPUT_DIR/POST_cities.txt"
echo "=== POST $POST_ENDPOINT ===" > "$POST_OUTFILE"

CITY_NAMES=()
for i in $(seq 1 $TOTAL_REQUESTS); do
    CITY_NAME="LoadCity_$(uuidgen | cut -d'-' -f1)"
    POST_DATA="{\"name\": \"$CITY_NAME\"}"
    echo "Создание города: $CITY_NAME"
    run_ab_test "POST" "$POST_ENDPOINT" "$POST_OUTFILE" "$POST_DATA"
    CITY_NAMES+=("$CITY_NAME")
done

# ======================
# Удаляем созданные города
# ======================
echo "" >> "$POST_OUTFILE"
echo "=== DELETE созданных городов ===" >> "$POST_OUTFILE"
for name in "${CITY_NAMES[@]}"; do
    echo "Удаление города: $name" >> "$POST_OUTFILE"
    curl -s -X DELETE "$DELETE_ENDPOINT/$name" >> "$POST_OUTFILE"
    echo "" >> "$POST_OUTFILE"
done

# ======================
# Генерация отчета
# ======================
generate_md_report
