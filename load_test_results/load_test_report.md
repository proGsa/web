# Отчет по нагрузочному тестированию TravelGuide API
Дата: Thu Nov 13 13:34:58 MSK 2025

## GET_localhost_api_v1_health
```
=== GET http://localhost/api/v1/health ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v1/health
Document Length:        34 bytes

Concurrency Level:      10
Time taken for tests:   0.118 seconds
Complete requests:      100
Failed requests:        50
   (Connect: 0, Receive: 0, Length: 50, Exceptions: 0)
Total transferred:      18250 bytes
HTML transferred:       3350 bytes
Requests per second:    848.25 [#/sec] (mean)
Time per request:       11.789 [ms] (mean)
Time per request:       1.179 [ms] (mean, across all concurrent requests)
Transfer rate:          151.18 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:     1   10   9.4      6      40
Waiting:        1   10   9.4      6      40
Total:          2   10   9.4      7      40

Percentage of the requests served within a certain time (ms)
  50%      7
  66%     10
  75%     11
  80%     14
  90%     26
  95%     39
  98%     40
  99%     40
 100%     40 (longest request)
=== GET http://localhost/api/v1/health ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v1/health
Document Length:        34 bytes

Concurrency Level:      10
Time taken for tests:   0.607 seconds
Complete requests:      100
Failed requests:        50
   (Connect: 0, Receive: 0, Length: 50, Exceptions: 0)
Total transferred:      18250 bytes
HTML transferred:       3350 bytes
Requests per second:    164.77 [#/sec] (mean)
Time per request:       60.692 [ms] (mean)
Time per request:       6.069 [ms] (mean, across all concurrent requests)
Transfer rate:          29.37 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:     1   40  88.2      8     322
Waiting:        1   40  88.2      8     322
Total:          1   40  88.3      8     322

Percentage of the requests served within a certain time (ms)
  50%      8
  66%     11
  75%     15
  80%     19
  90%    271
  95%    282
  98%    322
  99%    322
 100%    322 (longest request)
```
## GET_localhost_api_v2_health
```
=== GET http://localhost/api/v2/health ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/health
Document Length:        34 bytes

Concurrency Level:      10
Time taken for tests:   0.059 seconds
Complete requests:      100
Failed requests:        50
   (Connect: 0, Receive: 0, Length: 50, Exceptions: 0)
Total transferred:      18250 bytes
HTML transferred:       3350 bytes
Requests per second:    1687.02 [#/sec] (mean)
Time per request:       5.928 [ms] (mean)
Time per request:       0.593 [ms] (mean, across all concurrent requests)
Transfer rate:          300.67 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:     2    5   3.2      4      12
Waiting:        1    5   3.2      4      12
Total:          2    5   3.2      4      13

Percentage of the requests served within a certain time (ms)
  50%      4
  66%      5
  75%      8
  80%      9
  90%     11
  95%     12
  98%     12
  99%     13
 100%     13 (longest request)
=== GET http://localhost/api/v2/health ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/health
Document Length:        34 bytes

Concurrency Level:      10
Time taken for tests:   0.069 seconds
Complete requests:      100
Failed requests:        50
   (Connect: 0, Receive: 0, Length: 50, Exceptions: 0)
Total transferred:      18250 bytes
HTML transferred:       3350 bytes
Requests per second:    1459.77 [#/sec] (mean)
Time per request:       6.850 [ms] (mean)
Time per request:       0.685 [ms] (mean, across all concurrent requests)
Transfer rate:          260.16 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:     2    6   3.4      5      19
Waiting:        2    6   3.3      5      19
Total:          2    6   3.4      6      19

Percentage of the requests served within a certain time (ms)
  50%      6
  66%      7
  75%      8
  80%      9
  90%     11
  95%     14
  98%     15
  99%     19
 100%     19 (longest request)
```
## POST_cities
```
=== POST http://localhost/api/v2/cities/ ===
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        35 bytes

Concurrency Level:      1
Time taken for tests:   0.108 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      189 bytes
Total body sent:        174
HTML transferred:       35 bytes
Requests per second:    9.23 [#/sec] (mean)
Time per request:       108.354 [ms] (mean)
Time per request:       108.354 [ms] (mean, across all concurrent requests)
Transfer rate:          1.70 [Kbytes/sec] received
                        1.57 kb/s sent
                        3.27 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:   108  108   0.0    108     108
Waiting:      108  108   0.0    108     108
Total:        108  108   0.0    108     108
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        35 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      189 bytes
Total body sent:        174
HTML transferred:       35 bytes
Requests per second:    177.12 [#/sec] (mean)
Time per request:       5.646 [ms] (mean)
Time per request:       5.646 [ms] (mean, across all concurrent requests)
Transfer rate:          32.69 [Kbytes/sec] received
                        30.10 kb/s sent
                        62.79 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          6    6   0.0      6       6
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        35 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      189 bytes
Total body sent:        174
HTML transferred:       35 bytes
Requests per second:    183.65 [#/sec] (mean)
Time per request:       5.445 [ms] (mean)
Time per request:       5.445 [ms] (mean, across all concurrent requests)
Transfer rate:          33.90 [Kbytes/sec] received
                        31.21 kb/s sent
                        65.10 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        35 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      189 bytes
Total body sent:        174
HTML transferred:       35 bytes
Requests per second:    223.16 [#/sec] (mean)
Time per request:       4.481 [ms] (mean)
Time per request:       4.481 [ms] (mean, across all concurrent requests)
Transfer rate:          41.19 [Kbytes/sec] received
                        37.92 kb/s sent
                        79.11 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    177.43 [#/sec] (mean)
Time per request:       5.636 [ms] (mean)
Time per request:       5.636 [ms] (mean, across all concurrent requests)
Transfer rate:          32.92 [Kbytes/sec] received
                        30.15 kb/s sent
                        63.07 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          6    6   0.0      6       6
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    186.05 [#/sec] (mean)
Time per request:       5.375 [ms] (mean)
Time per request:       5.375 [ms] (mean, across all concurrent requests)
Transfer rate:          34.52 [Kbytes/sec] received
                        31.61 kb/s sent
                        66.13 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    168.41 [#/sec] (mean)
Time per request:       5.938 [ms] (mean)
Time per request:       5.938 [ms] (mean, across all concurrent requests)
Transfer rate:          31.25 [Kbytes/sec] received
                        28.62 kb/s sent
                        59.86 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.012 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    86.64 [#/sec] (mean)
Time per request:       11.542 [ms] (mean)
Time per request:       11.542 [ms] (mean, across all concurrent requests)
Transfer rate:          16.08 [Kbytes/sec] received
                        14.72 kb/s sent
                        30.80 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:    11   11   0.0     11      11
Waiting:       11   11   0.0     11      11
Total:         11   11   0.0     11      11
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    200.68 [#/sec] (mean)
Time per request:       4.983 [ms] (mean)
Time per request:       4.983 [ms] (mean, across all concurrent requests)
Transfer rate:          37.24 [Kbytes/sec] received
                        34.10 kb/s sent
                        71.34 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    247.34 [#/sec] (mean)
Time per request:       4.043 [ms] (mean)
Time per request:       4.043 [ms] (mean, across all concurrent requests)
Transfer rate:          45.89 [Kbytes/sec] received
                        42.03 kb/s sent
                        87.92 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    183.02 [#/sec] (mean)
Time per request:       5.464 [ms] (mean)
Time per request:       5.464 [ms] (mean, across all concurrent requests)
Transfer rate:          33.96 [Kbytes/sec] received
                        31.10 kb/s sent
                        65.06 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    249.44 [#/sec] (mean)
Time per request:       4.009 [ms] (mean)
Time per request:       4.009 [ms] (mean, across all concurrent requests)
Transfer rate:          46.28 [Kbytes/sec] received
                        42.39 kb/s sent
                        88.67 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    237.64 [#/sec] (mean)
Time per request:       4.208 [ms] (mean)
Time per request:       4.208 [ms] (mean, across all concurrent requests)
Transfer rate:          44.09 [Kbytes/sec] received
                        40.38 kb/s sent
                        84.47 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    221.68 [#/sec] (mean)
Time per request:       4.511 [ms] (mean)
Time per request:       4.511 [ms] (mean, across all concurrent requests)
Transfer rate:          41.13 [Kbytes/sec] received
                        37.67 kb/s sent
                        78.80 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    236.46 [#/sec] (mean)
Time per request:       4.229 [ms] (mean)
Time per request:       4.229 [ms] (mean, across all concurrent requests)
Transfer rate:          43.87 [Kbytes/sec] received
                        40.18 kb/s sent
                        84.06 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    189.68 [#/sec] (mean)
Time per request:       5.272 [ms] (mean)
Time per request:       5.272 [ms] (mean, across all concurrent requests)
Transfer rate:          35.19 [Kbytes/sec] received
                        32.23 kb/s sent
                        67.43 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    217.82 [#/sec] (mean)
Time per request:       4.591 [ms] (mean)
Time per request:       4.591 [ms] (mean, across all concurrent requests)
Transfer rate:          40.42 [Kbytes/sec] received
                        37.01 kb/s sent
                        77.43 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    241.43 [#/sec] (mean)
Time per request:       4.142 [ms] (mean)
Time per request:       4.142 [ms] (mean, across all concurrent requests)
Transfer rate:          44.80 [Kbytes/sec] received
                        41.02 kb/s sent
                        85.82 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    251.19 [#/sec] (mean)
Time per request:       3.981 [ms] (mean)
Time per request:       3.981 [ms] (mean, across all concurrent requests)
Transfer rate:          46.61 [Kbytes/sec] received
                        42.68 kb/s sent
                        89.29 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    237.25 [#/sec] (mean)
Time per request:       4.215 [ms] (mean)
Time per request:       4.215 [ms] (mean, across all concurrent requests)
Transfer rate:          44.02 [Kbytes/sec] received
                        40.31 kb/s sent
                        84.33 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    225.48 [#/sec] (mean)
Time per request:       4.435 [ms] (mean)
Time per request:       4.435 [ms] (mean, across all concurrent requests)
Transfer rate:          41.84 [Kbytes/sec] received
                        38.31 kb/s sent
                        80.15 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    272.03 [#/sec] (mean)
Time per request:       3.676 [ms] (mean)
Time per request:       3.676 [ms] (mean, across all concurrent requests)
Transfer rate:          50.48 [Kbytes/sec] received
                        46.22 kb/s sent
                        96.70 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     3    3   0.0      3       3
Waiting:        3    3   0.0      3       3
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    232.29 [#/sec] (mean)
Time per request:       4.305 [ms] (mean)
Time per request:       4.305 [ms] (mean, across all concurrent requests)
Transfer rate:          43.10 [Kbytes/sec] received
                        39.47 kb/s sent
                        82.57 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    196.73 [#/sec] (mean)
Time per request:       5.083 [ms] (mean)
Time per request:       5.083 [ms] (mean, across all concurrent requests)
Transfer rate:          36.50 [Kbytes/sec] received
                        33.43 kb/s sent
                        69.93 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    200.76 [#/sec] (mean)
Time per request:       4.981 [ms] (mean)
Time per request:       4.981 [ms] (mean, across all concurrent requests)
Transfer rate:          37.25 [Kbytes/sec] received
                        34.11 kb/s sent
                        71.36 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.007 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    153.33 [#/sec] (mean)
Time per request:       6.522 [ms] (mean)
Time per request:       6.522 [ms] (mean, across all concurrent requests)
Transfer rate:          28.45 [Kbytes/sec] received
                        26.05 kb/s sent
                        54.50 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    191.20 [#/sec] (mean)
Time per request:       5.230 [ms] (mean)
Time per request:       5.230 [ms] (mean, across all concurrent requests)
Transfer rate:          35.48 [Kbytes/sec] received
                        32.49 kb/s sent
                        67.97 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    229.41 [#/sec] (mean)
Time per request:       4.359 [ms] (mean)
Time per request:       4.359 [ms] (mean, across all concurrent requests)
Transfer rate:          42.57 [Kbytes/sec] received
                        38.98 kb/s sent
                        81.55 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    254.13 [#/sec] (mean)
Time per request:       3.935 [ms] (mean)
Time per request:       3.935 [ms] (mean, across all concurrent requests)
Transfer rate:          47.15 [Kbytes/sec] received
                        43.18 kb/s sent
                        90.34 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    200.04 [#/sec] (mean)
Time per request:       4.999 [ms] (mean)
Time per request:       4.999 [ms] (mean, across all concurrent requests)
Transfer rate:          37.12 [Kbytes/sec] received
                        33.99 kb/s sent
                        71.11 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.007 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    148.15 [#/sec] (mean)
Time per request:       6.750 [ms] (mean)
Time per request:       6.750 [ms] (mean, across all concurrent requests)
Transfer rate:          27.49 [Kbytes/sec] received
                        25.17 kb/s sent
                        52.66 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     7    7   0.0      7       7
Waiting:        7    7   0.0      7       7
Total:          7    7   0.0      7       7
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    261.51 [#/sec] (mean)
Time per request:       3.824 [ms] (mean)
Time per request:       3.824 [ms] (mean, across all concurrent requests)
Transfer rate:          48.52 [Kbytes/sec] received
                        44.44 kb/s sent
                        92.96 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    210.04 [#/sec] (mean)
Time per request:       4.761 [ms] (mean)
Time per request:       4.761 [ms] (mean, across all concurrent requests)
Transfer rate:          38.97 [Kbytes/sec] received
                        35.69 kb/s sent
                        74.66 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    183.45 [#/sec] (mean)
Time per request:       5.451 [ms] (mean)
Time per request:       5.451 [ms] (mean, across all concurrent requests)
Transfer rate:          34.04 [Kbytes/sec] received
                        31.17 kb/s sent
                        65.21 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    221.68 [#/sec] (mean)
Time per request:       4.511 [ms] (mean)
Time per request:       4.511 [ms] (mean, across all concurrent requests)
Transfer rate:          41.13 [Kbytes/sec] received
                        37.67 kb/s sent
                        78.80 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    207.30 [#/sec] (mean)
Time per request:       4.824 [ms] (mean)
Time per request:       4.824 [ms] (mean, across all concurrent requests)
Transfer rate:          38.46 [Kbytes/sec] received
                        35.22 kb/s sent
                        73.69 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    187.06 [#/sec] (mean)
Time per request:       5.346 [ms] (mean)
Time per request:       5.346 [ms] (mean, across all concurrent requests)
Transfer rate:          34.71 [Kbytes/sec] received
                        31.78 kb/s sent
                        66.49 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    182.68 [#/sec] (mean)
Time per request:       5.474 [ms] (mean)
Time per request:       5.474 [ms] (mean, across all concurrent requests)
Transfer rate:          33.90 [Kbytes/sec] received
                        31.04 kb/s sent
                        64.94 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    216.22 [#/sec] (mean)
Time per request:       4.625 [ms] (mean)
Time per request:       4.625 [ms] (mean, across all concurrent requests)
Transfer rate:          40.12 [Kbytes/sec] received
                        36.74 kb/s sent
                        76.86 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    256.81 [#/sec] (mean)
Time per request:       3.894 [ms] (mean)
Time per request:       3.894 [ms] (mean, across all concurrent requests)
Transfer rate:          47.65 [Kbytes/sec] received
                        43.64 kb/s sent
                        91.29 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    244.68 [#/sec] (mean)
Time per request:       4.087 [ms] (mean)
Time per request:       4.087 [ms] (mean, across all concurrent requests)
Transfer rate:          45.40 [Kbytes/sec] received
                        41.58 kb/s sent
                        86.98 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    247.10 [#/sec] (mean)
Time per request:       4.047 [ms] (mean)
Time per request:       4.047 [ms] (mean, across all concurrent requests)
Transfer rate:          45.85 [Kbytes/sec] received
                        41.99 kb/s sent
                        87.84 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    230.20 [#/sec] (mean)
Time per request:       4.344 [ms] (mean)
Time per request:       4.344 [ms] (mean, across all concurrent requests)
Transfer rate:          42.71 [Kbytes/sec] received
                        39.12 kb/s sent
                        81.83 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    213.95 [#/sec] (mean)
Time per request:       4.674 [ms] (mean)
Time per request:       4.674 [ms] (mean, across all concurrent requests)
Transfer rate:          39.70 [Kbytes/sec] received
                        36.35 kb/s sent
                        76.05 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    247.95 [#/sec] (mean)
Time per request:       4.033 [ms] (mean)
Time per request:       4.033 [ms] (mean, across all concurrent requests)
Transfer rate:          46.01 [Kbytes/sec] received
                        42.13 kb/s sent
                        88.14 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    230.89 [#/sec] (mean)
Time per request:       4.331 [ms] (mean)
Time per request:       4.331 [ms] (mean, across all concurrent requests)
Transfer rate:          42.84 [Kbytes/sec] received
                        39.23 kb/s sent
                        82.08 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    232.99 [#/sec] (mean)
Time per request:       4.292 [ms] (mean)
Time per request:       4.292 [ms] (mean, across all concurrent requests)
Transfer rate:          43.23 [Kbytes/sec] received
                        39.59 kb/s sent
                        82.82 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    176.46 [#/sec] (mean)
Time per request:       5.667 [ms] (mean)
Time per request:       5.667 [ms] (mean, across all concurrent requests)
Transfer rate:          32.74 [Kbytes/sec] received
                        29.98 kb/s sent
                        62.73 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          6    6   0.0      6       6
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    194.06 [#/sec] (mean)
Time per request:       5.153 [ms] (mean)
Time per request:       5.153 [ms] (mean, across all concurrent requests)
Transfer rate:          36.01 [Kbytes/sec] received
                        32.98 kb/s sent
                        68.98 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    181.79 [#/sec] (mean)
Time per request:       5.501 [ms] (mean)
Time per request:       5.501 [ms] (mean, across all concurrent requests)
Transfer rate:          33.73 [Kbytes/sec] received
                        30.89 kb/s sent
                        64.62 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    239.58 [#/sec] (mean)
Time per request:       4.174 [ms] (mean)
Time per request:       4.174 [ms] (mean, across all concurrent requests)
Transfer rate:          44.45 [Kbytes/sec] received
                        40.71 kb/s sent
                        85.16 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    256.21 [#/sec] (mean)
Time per request:       3.903 [ms] (mean)
Time per request:       3.903 [ms] (mean, across all concurrent requests)
Transfer rate:          47.54 [Kbytes/sec] received
                        43.54 kb/s sent
                        91.08 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    211.77 [#/sec] (mean)
Time per request:       4.722 [ms] (mean)
Time per request:       4.722 [ms] (mean, across all concurrent requests)
Transfer rate:          39.29 [Kbytes/sec] received
                        35.99 kb/s sent
                        75.28 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    242.37 [#/sec] (mean)
Time per request:       4.126 [ms] (mean)
Time per request:       4.126 [ms] (mean, across all concurrent requests)
Transfer rate:          44.97 [Kbytes/sec] received
                        41.18 kb/s sent
                        86.15 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    225.23 [#/sec] (mean)
Time per request:       4.440 [ms] (mean)
Time per request:       4.440 [ms] (mean, across all concurrent requests)
Transfer rate:          41.79 [Kbytes/sec] received
                        38.27 kb/s sent
                        80.06 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    249.13 [#/sec] (mean)
Time per request:       4.014 [ms] (mean)
Time per request:       4.014 [ms] (mean, across all concurrent requests)
Transfer rate:          46.22 [Kbytes/sec] received
                        42.33 kb/s sent
                        88.56 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    234.91 [#/sec] (mean)
Time per request:       4.257 [ms] (mean)
Time per request:       4.257 [ms] (mean, across all concurrent requests)
Transfer rate:          43.59 [Kbytes/sec] received
                        39.92 kb/s sent
                        83.50 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    257.73 [#/sec] (mean)
Time per request:       3.880 [ms] (mean)
Time per request:       3.880 [ms] (mean, across all concurrent requests)
Transfer rate:          47.82 [Kbytes/sec] received
                        43.79 kb/s sent
                        91.62 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    223.76 [#/sec] (mean)
Time per request:       4.469 [ms] (mean)
Time per request:       4.469 [ms] (mean, across all concurrent requests)
Transfer rate:          41.52 [Kbytes/sec] received
                        38.02 kb/s sent
                        79.54 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    216.83 [#/sec] (mean)
Time per request:       4.612 [ms] (mean)
Time per request:       4.612 [ms] (mean, across all concurrent requests)
Transfer rate:          40.23 [Kbytes/sec] received
                        36.84 kb/s sent
                        77.07 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    267.52 [#/sec] (mean)
Time per request:       3.738 [ms] (mean)
Time per request:       3.738 [ms] (mean, across all concurrent requests)
Transfer rate:          49.64 [Kbytes/sec] received
                        45.46 kb/s sent
                        95.10 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        3    3   0.0      3       3
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    217.25 [#/sec] (mean)
Time per request:       4.603 [ms] (mean)
Time per request:       4.603 [ms] (mean, across all concurrent requests)
Transfer rate:          40.31 [Kbytes/sec] received
                        36.92 kb/s sent
                        77.23 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    259.34 [#/sec] (mean)
Time per request:       3.856 [ms] (mean)
Time per request:       3.856 [ms] (mean, across all concurrent requests)
Transfer rate:          48.12 [Kbytes/sec] received
                        44.07 kb/s sent
                        92.19 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.014 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    73.20 [#/sec] (mean)
Time per request:       13.661 [ms] (mean)
Time per request:       13.661 [ms] (mean, across all concurrent requests)
Transfer rate:          13.58 [Kbytes/sec] received
                        12.44 kb/s sent
                        26.02 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:    13   13   0.0     13      13
Waiting:       13   13   0.0     13      13
Total:         14   14   0.0     14      14
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.022 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    45.47 [#/sec] (mean)
Time per request:       21.993 [ms] (mean)
Time per request:       21.993 [ms] (mean, across all concurrent requests)
Transfer rate:          8.44 [Kbytes/sec] received
                        7.73 kb/s sent
                        16.16 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:    22   22   0.0     22      22
Waiting:       22   22   0.0     22      22
Total:         22   22   0.0     22      22
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.008 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    130.67 [#/sec] (mean)
Time per request:       7.653 [ms] (mean)
Time per request:       7.653 [ms] (mean, across all concurrent requests)
Transfer rate:          24.24 [Kbytes/sec] received
                        22.20 kb/s sent
                        46.45 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     7    7   0.0      7       7
Waiting:        7    7   0.0      7       7
Total:          8    8   0.0      8       8
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    170.44 [#/sec] (mean)
Time per request:       5.867 [ms] (mean)
Time per request:       5.867 [ms] (mean, across all concurrent requests)
Transfer rate:          31.63 [Kbytes/sec] received
                        28.96 kb/s sent
                        60.59 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    196.58 [#/sec] (mean)
Time per request:       5.087 [ms] (mean)
Time per request:       5.087 [ms] (mean, across all concurrent requests)
Transfer rate:          36.47 [Kbytes/sec] received
                        33.40 kb/s sent
                        69.88 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    212.36 [#/sec] (mean)
Time per request:       4.709 [ms] (mean)
Time per request:       4.709 [ms] (mean, across all concurrent requests)
Transfer rate:          39.40 [Kbytes/sec] received
                        36.08 kb/s sent
                        75.49 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    260.28 [#/sec] (mean)
Time per request:       3.842 [ms] (mean)
Time per request:       3.842 [ms] (mean, across all concurrent requests)
Transfer rate:          48.29 [Kbytes/sec] received
                        44.23 kb/s sent
                        92.52 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    230.79 [#/sec] (mean)
Time per request:       4.333 [ms] (mean)
Time per request:       4.333 [ms] (mean, across all concurrent requests)
Transfer rate:          42.82 [Kbytes/sec] received
                        39.22 kb/s sent
                        82.04 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    247.04 [#/sec] (mean)
Time per request:       4.048 [ms] (mean)
Time per request:       4.048 [ms] (mean, across all concurrent requests)
Transfer rate:          45.84 [Kbytes/sec] received
                        41.98 kb/s sent
                        87.81 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    193.42 [#/sec] (mean)
Time per request:       5.170 [ms] (mean)
Time per request:       5.170 [ms] (mean, across all concurrent requests)
Transfer rate:          35.89 [Kbytes/sec] received
                        32.87 kb/s sent
                        68.76 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    230.26 [#/sec] (mean)
Time per request:       4.343 [ms] (mean)
Time per request:       4.343 [ms] (mean, across all concurrent requests)
Transfer rate:          42.72 [Kbytes/sec] received
                        39.13 kb/s sent
                        81.85 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    200.56 [#/sec] (mean)
Time per request:       4.986 [ms] (mean)
Time per request:       4.986 [ms] (mean, across all concurrent requests)
Transfer rate:          37.21 [Kbytes/sec] received
                        34.08 kb/s sent
                        71.29 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    247.10 [#/sec] (mean)
Time per request:       4.047 [ms] (mean)
Time per request:       4.047 [ms] (mean, across all concurrent requests)
Transfer rate:          45.85 [Kbytes/sec] received
                        41.99 kb/s sent
                        87.84 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    215.98 [#/sec] (mean)
Time per request:       4.630 [ms] (mean)
Time per request:       4.630 [ms] (mean, across all concurrent requests)
Transfer rate:          40.07 [Kbytes/sec] received
                        36.70 kb/s sent
                        76.78 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    238.04 [#/sec] (mean)
Time per request:       4.201 [ms] (mean)
Time per request:       4.201 [ms] (mean, across all concurrent requests)
Transfer rate:          44.17 [Kbytes/sec] received
                        40.45 kb/s sent
                        84.62 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    214.27 [#/sec] (mean)
Time per request:       4.667 [ms] (mean)
Time per request:       4.667 [ms] (mean, across all concurrent requests)
Transfer rate:          39.76 [Kbytes/sec] received
                        36.41 kb/s sent
                        76.17 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    212.22 [#/sec] (mean)
Time per request:       4.712 [ms] (mean)
Time per request:       4.712 [ms] (mean, across all concurrent requests)
Transfer rate:          39.38 [Kbytes/sec] received
                        36.06 kb/s sent
                        75.44 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    250.25 [#/sec] (mean)
Time per request:       3.996 [ms] (mean)
Time per request:       3.996 [ms] (mean, across all concurrent requests)
Transfer rate:          46.43 [Kbytes/sec] received
                        42.52 kb/s sent
                        88.96 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    230.36 [#/sec] (mean)
Time per request:       4.341 [ms] (mean)
Time per request:       4.341 [ms] (mean, across all concurrent requests)
Transfer rate:          42.74 [Kbytes/sec] received
                        39.14 kb/s sent
                        81.89 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    250.25 [#/sec] (mean)
Time per request:       3.996 [ms] (mean)
Time per request:       3.996 [ms] (mean, across all concurrent requests)
Transfer rate:          46.43 [Kbytes/sec] received
                        42.52 kb/s sent
                        88.96 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    246.91 [#/sec] (mean)
Time per request:       4.050 [ms] (mean)
Time per request:       4.050 [ms] (mean, across all concurrent requests)
Transfer rate:          45.81 [Kbytes/sec] received
                        41.96 kb/s sent
                        87.77 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    219.73 [#/sec] (mean)
Time per request:       4.551 [ms] (mean)
Time per request:       4.551 [ms] (mean, across all concurrent requests)
Transfer rate:          40.77 [Kbytes/sec] received
                        37.34 kb/s sent
                        78.11 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    260.89 [#/sec] (mean)
Time per request:       3.833 [ms] (mean)
Time per request:       3.833 [ms] (mean, across all concurrent requests)
Transfer rate:          48.41 [Kbytes/sec] received
                        44.33 kb/s sent
                        92.74 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    246.55 [#/sec] (mean)
Time per request:       4.056 [ms] (mean)
Time per request:       4.056 [ms] (mean, across all concurrent requests)
Transfer rate:          45.75 [Kbytes/sec] received
                        41.89 kb/s sent
                        87.64 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    252.72 [#/sec] (mean)
Time per request:       3.957 [ms] (mean)
Time per request:       3.957 [ms] (mean, across all concurrent requests)
Transfer rate:          46.89 [Kbytes/sec] received
                        42.94 kb/s sent
                        89.83 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    185.15 [#/sec] (mean)
Time per request:       5.401 [ms] (mean)
Time per request:       5.401 [ms] (mean, across all concurrent requests)
Transfer rate:          34.35 [Kbytes/sec] received
                        31.46 kb/s sent
                        65.82 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    177.34 [#/sec] (mean)
Time per request:       5.639 [ms] (mean)
Time per request:       5.639 [ms] (mean, across all concurrent requests)
Transfer rate:          32.90 [Kbytes/sec] received
                        30.13 kb/s sent
                        63.04 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          6    6   0.0      6       6
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    195.43 [#/sec] (mean)
Time per request:       5.117 [ms] (mean)
Time per request:       5.117 [ms] (mean, across all concurrent requests)
Transfer rate:          36.26 [Kbytes/sec] received
                        33.21 kb/s sent
                        69.47 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    172.56 [#/sec] (mean)
Time per request:       5.795 [ms] (mean)
Time per request:       5.795 [ms] (mean, across all concurrent requests)
Transfer rate:          32.02 [Kbytes/sec] received
                        29.32 kb/s sent
                        61.34 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    191.68 [#/sec] (mean)
Time per request:       5.217 [ms] (mean)
Time per request:       5.217 [ms] (mean, across all concurrent requests)
Transfer rate:          35.57 [Kbytes/sec] received
                        32.57 kb/s sent
                        68.14 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        36 bytes

Concurrency Level:      1
Time taken for tests:   0.007 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      190 bytes
Total body sent:        174
HTML transferred:       36 bytes
Requests per second:    142.29 [#/sec] (mean)
Time per request:       7.028 [ms] (mean)
Time per request:       7.028 [ms] (mean, across all concurrent requests)
Transfer rate:          26.40 [Kbytes/sec] received
                        24.18 kb/s sent
                        50.58 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     7    7   0.0      7       7
Waiting:        7    7   0.0      7       7
Total:          7    7   0.0      7       7
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        37 bytes

Concurrency Level:      1
Time taken for tests:   0.010 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      191 bytes
Total body sent:        174
HTML transferred:       37 bytes
Requests per second:    100.41 [#/sec] (mean)
Time per request:       9.959 [ms] (mean)
Time per request:       9.959 [ms] (mean, across all concurrent requests)
Transfer rate:          18.73 [Kbytes/sec] received
                        17.06 kb/s sent
                        35.79 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:    10   10   0.0     10      10
Waiting:       10   10   0.0     10      10
Total:         10   10   0.0     10      10
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        37 bytes

Concurrency Level:      1
Time taken for tests:   0.010 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      191 bytes
Total body sent:        174
HTML transferred:       37 bytes
Requests per second:    103.97 [#/sec] (mean)
Time per request:       9.618 [ms] (mean)
Time per request:       9.618 [ms] (mean, across all concurrent requests)
Transfer rate:          19.39 [Kbytes/sec] received
                        17.67 kb/s sent
                        37.06 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     9    9   0.0      9       9
Waiting:        9    9   0.0      9       9
Total:         10   10   0.0     10      10
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        37 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      191 bytes
Total body sent:        174
HTML transferred:       37 bytes
Requests per second:    203.21 [#/sec] (mean)
Time per request:       4.921 [ms] (mean)
Time per request:       4.921 [ms] (mean, across all concurrent requests)
Transfer rate:          37.90 [Kbytes/sec] received
                        34.53 kb/s sent
                        72.43 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        37 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      191 bytes
Total body sent:        174
HTML transferred:       37 bytes
Requests per second:    258.53 [#/sec] (mean)
Time per request:       3.868 [ms] (mean)
Time per request:       3.868 [ms] (mean, across all concurrent requests)
Transfer rate:          48.22 [Kbytes/sec] received
                        43.93 kb/s sent
                        92.15 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        37 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      191 bytes
Total body sent:        174
HTML transferred:       37 bytes
Requests per second:    239.69 [#/sec] (mean)
Time per request:       4.172 [ms] (mean)
Time per request:       4.172 [ms] (mean, across all concurrent requests)
Transfer rate:          44.71 [Kbytes/sec] received
                        40.73 kb/s sent
                        85.44 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        37 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      191 bytes
Total body sent:        174
HTML transferred:       37 bytes
Requests per second:    222.47 [#/sec] (mean)
Time per request:       4.495 [ms] (mean)
Time per request:       4.495 [ms] (mean, across all concurrent requests)
Transfer rate:          41.50 [Kbytes/sec] received
                        37.80 kb/s sent
                        79.30 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4

=== DELETE созданных городов ===
Удаление города: LoadCity_7CE9D582
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_7CE9D582"}]}
Удаление города: LoadCity_DB4A0E5D
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_DB4A0E5D"}]}
Удаление города: LoadCity_D12924E9
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_D12924E9"}]}
Удаление города: LoadCity_CED26790
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_CED26790"}]}
Удаление города: LoadCity_DE2F3579
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_DE2F3579"}]}
Удаление города: LoadCity_DB6DA902
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_DB6DA902"}]}
Удаление города: LoadCity_1324A673
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_1324A673"}]}
Удаление города: LoadCity_4A72D83C
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_4A72D83C"}]}
Удаление города: LoadCity_AC4740F4
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_AC4740F4"}]}
Удаление города: LoadCity_3584621C
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_3584621C"}]}
Удаление города: LoadCity_756A50D0
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_756A50D0"}]}
Удаление города: LoadCity_4C409F25
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_4C409F25"}]}
Удаление города: LoadCity_2EE30523
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_2EE30523"}]}
Удаление города: LoadCity_BF5CE04A
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_BF5CE04A"}]}
Удаление города: LoadCity_45ED0D06
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_45ED0D06"}]}
Удаление города: LoadCity_03185048
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_03185048"}]}
Удаление города: LoadCity_5B07B029
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_5B07B029"}]}
Удаление города: LoadCity_7288EEB9
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_7288EEB9"}]}
Удаление города: LoadCity_D277261F
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_D277261F"}]}
Удаление города: LoadCity_4DE061BA
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_4DE061BA"}]}
Удаление города: LoadCity_DC12C68D
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_DC12C68D"}]}
Удаление города: LoadCity_5AB8F70C
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_5AB8F70C"}]}
Удаление города: LoadCity_7BDB6DA2
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_7BDB6DA2"}]}
Удаление города: LoadCity_9EB48988
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_9EB48988"}]}
Удаление города: LoadCity_3F6E0B3D
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_3F6E0B3D"}]}
Удаление города: LoadCity_D849A227
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_D849A227"}]}
Удаление города: LoadCity_36E82538
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_36E82538"}]}
Удаление города: LoadCity_DEA095F4
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_DEA095F4"}]}
Удаление города: LoadCity_13C32E7E
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_13C32E7E"}]}
Удаление города: LoadCity_6B069F04
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_6B069F04"}]}
Удаление города: LoadCity_1750448C
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_1750448C"}]}
Удаление города: LoadCity_7BCA43C4
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_7BCA43C4"}]}
Удаление города: LoadCity_9E045878
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_9E045878"}]}
Удаление города: LoadCity_AC576D62
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_AC576D62"}]}
Удаление города: LoadCity_ECAA8D89
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_ECAA8D89"}]}
Удаление города: LoadCity_B6947D68
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_B6947D68"}]}
Удаление города: LoadCity_15A7E29D
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_15A7E29D"}]}
Удаление города: LoadCity_0B67D0CC
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_0B67D0CC"}]}
Удаление города: LoadCity_CDE4E51D
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_CDE4E51D"}]}
Удаление города: LoadCity_740F388D
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_740F388D"}]}
Удаление города: LoadCity_D97A11CD
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_D97A11CD"}]}
Удаление города: LoadCity_AFF0C971
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_AFF0C971"}]}
Удаление города: LoadCity_63803A73
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_63803A73"}]}
Удаление города: LoadCity_DA85404E
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_DA85404E"}]}
Удаление города: LoadCity_83D80DA4
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_83D80DA4"}]}
Удаление города: LoadCity_80FDA968
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_80FDA968"}]}
Удаление города: LoadCity_EBED51A4
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_EBED51A4"}]}
Удаление города: LoadCity_5DC6112D
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_5DC6112D"}]}
Удаление города: LoadCity_216F9124
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_216F9124"}]}
Удаление города: LoadCity_8083904D
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_8083904D"}]}
Удаление города: LoadCity_162A73A1
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_162A73A1"}]}
Удаление города: LoadCity_FE3DA7AC
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_FE3DA7AC"}]}
Удаление города: LoadCity_363011E6
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_363011E6"}]}
Удаление города: LoadCity_AA6D38FF
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_AA6D38FF"}]}
Удаление города: LoadCity_7B6EA339
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_7B6EA339"}]}
Удаление города: LoadCity_6C4115E4
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_6C4115E4"}]}
Удаление города: LoadCity_7F9763A0
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_7F9763A0"}]}
Удаление города: LoadCity_6AE1C7AF
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_6AE1C7AF"}]}
Удаление города: LoadCity_60D2A37A
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_60D2A37A"}]}
Удаление города: LoadCity_96BF0EB8
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_96BF0EB8"}]}
Удаление города: LoadCity_AE920B06
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_AE920B06"}]}
Удаление города: LoadCity_C0EAE274
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_C0EAE274"}]}
Удаление города: LoadCity_D696A59E
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_D696A59E"}]}
Удаление города: LoadCity_7F52A044
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_7F52A044"}]}
Удаление города: LoadCity_52C435C7
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_52C435C7"}]}
Удаление города: LoadCity_7D5C89E8
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_7D5C89E8"}]}
Удаление города: LoadCity_2DF0D824
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_2DF0D824"}]}
Удаление города: LoadCity_8CD6B079
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_8CD6B079"}]}
Удаление города: LoadCity_01F82D0A
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_01F82D0A"}]}
Удаление города: LoadCity_C1AC686A
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_C1AC686A"}]}
Удаление города: LoadCity_D47C9565
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_D47C9565"}]}
Удаление города: LoadCity_8D4AA4DC
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_8D4AA4DC"}]}
Удаление города: LoadCity_B3281683
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_B3281683"}]}
Удаление города: LoadCity_4CA388B3
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_4CA388B3"}]}
Удаление города: LoadCity_3A963157
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_3A963157"}]}
Удаление города: LoadCity_12CB9383
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_12CB9383"}]}
Удаление города: LoadCity_AE0A6B19
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_AE0A6B19"}]}
Удаление города: LoadCity_8E25C769
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_8E25C769"}]}
Удаление города: LoadCity_1D4CAE38
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_1D4CAE38"}]}
Удаление города: LoadCity_8BC6607A
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_8BC6607A"}]}
Удаление города: LoadCity_3133F423
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_3133F423"}]}
Удаление города: LoadCity_0A482345
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_0A482345"}]}
Удаление города: LoadCity_8A2B9986
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_8A2B9986"}]}
Удаление города: LoadCity_F4079F58
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_F4079F58"}]}
Удаление города: LoadCity_CD14DC3D
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_CD14DC3D"}]}
Удаление города: LoadCity_8CD70B31
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_8CD70B31"}]}
Удаление города: LoadCity_687AB8AC
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_687AB8AC"}]}
Удаление города: LoadCity_C2DDAB65
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_C2DDAB65"}]}
Удаление города: LoadCity_AD62FECF
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_AD62FECF"}]}
Удаление города: LoadCity_BB1169F5
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_BB1169F5"}]}
Удаление города: LoadCity_65F968D5
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_65F968D5"}]}
Удаление города: LoadCity_58EE1B31
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_58EE1B31"}]}
Удаление города: LoadCity_1A2E821D
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_1A2E821D"}]}
Удаление города: LoadCity_A2397F44
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_A2397F44"}]}
Удаление города: LoadCity_4D04CFB0
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_4D04CFB0"}]}
Удаление города: LoadCity_4CFCC29E
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_4CFCC29E"}]}
Удаление города: LoadCity_03291E5E
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_03291E5E"}]}
Удаление города: LoadCity_4C63381C
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_4C63381C"}]}
Удаление города: LoadCity_A53EFD8E
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_A53EFD8E"}]}
Удаление города: LoadCity_3D51E9C6
{"detail":[{"type":"int_parsing","loc":["path","city_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"LoadCity_3D51E9C6"}]}
```
## POST_localhost_api_v2_cities_
```
=== POST http://localhost/api/v2/cities/ ===
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        42 bytes

Concurrency Level:      1
Time taken for tests:   0.015 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      196 bytes
Total body sent:        178
HTML transferred:       42 bytes
Requests per second:    67.65 [#/sec] (mean)
Time per request:       14.782 [ms] (mean)
Time per request:       14.782 [ms] (mean, across all concurrent requests)
Transfer rate:          12.95 [Kbytes/sec] received
                        11.76 kb/s sent
                        24.71 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:    15   15   0.0     15      15
Waiting:       15   15   0.0     15      15
Total:         15   15   0.0     15      15
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    185.77 [#/sec] (mean)
Time per request:       5.383 [ms] (mean)
Time per request:       5.383 [ms] (mean, across all concurrent requests)
Transfer rate:          35.74 [Kbytes/sec] received
                        32.47 kb/s sent
                        68.21 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        44 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      198 bytes
Total body sent:        180
HTML transferred:       44 bytes
Requests per second:    177.94 [#/sec] (mean)
Time per request:       5.620 [ms] (mean)
Time per request:       5.620 [ms] (mean, across all concurrent requests)
Transfer rate:          34.41 [Kbytes/sec] received
                        31.28 kb/s sent
                        65.68 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    177.18 [#/sec] (mean)
Time per request:       5.644 [ms] (mean)
Time per request:       5.644 [ms] (mean, across all concurrent requests)
Transfer rate:          34.09 [Kbytes/sec] received
                        30.97 kb/s sent
                        65.06 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    158.55 [#/sec] (mean)
Time per request:       6.307 [ms] (mean)
Time per request:       6.307 [ms] (mean, across all concurrent requests)
Transfer rate:          30.50 [Kbytes/sec] received
                        27.72 kb/s sent
                        58.22 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    178.60 [#/sec] (mean)
Time per request:       5.599 [ms] (mean)
Time per request:       5.599 [ms] (mean, across all concurrent requests)
Transfer rate:          34.36 [Kbytes/sec] received
                        31.22 kb/s sent
                        65.58 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    191.02 [#/sec] (mean)
Time per request:       5.235 [ms] (mean)
Time per request:       5.235 [ms] (mean, across all concurrent requests)
Transfer rate:          36.75 [Kbytes/sec] received
                        33.39 kb/s sent
                        70.14 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    199.68 [#/sec] (mean)
Time per request:       5.008 [ms] (mean)
Time per request:       5.008 [ms] (mean, across all concurrent requests)
Transfer rate:          38.42 [Kbytes/sec] received
                        34.91 kb/s sent
                        73.32 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    211.28 [#/sec] (mean)
Time per request:       4.733 [ms] (mean)
Time per request:       4.733 [ms] (mean, across all concurrent requests)
Transfer rate:          40.65 [Kbytes/sec] received
                        36.93 kb/s sent
                        77.58 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    192.09 [#/sec] (mean)
Time per request:       5.206 [ms] (mean)
Time per request:       5.206 [ms] (mean, across all concurrent requests)
Transfer rate:          36.95 [Kbytes/sec] received
                        33.58 kb/s sent
                        70.53 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    215.84 [#/sec] (mean)
Time per request:       4.633 [ms] (mean)
Time per request:       4.633 [ms] (mean, across all concurrent requests)
Transfer rate:          41.52 [Kbytes/sec] received
                        37.73 kb/s sent
                        79.25 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    222.92 [#/sec] (mean)
Time per request:       4.486 [ms] (mean)
Time per request:       4.486 [ms] (mean, across all concurrent requests)
Transfer rate:          42.89 [Kbytes/sec] received
                        38.97 kb/s sent
                        81.85 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        42 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      196 bytes
Total body sent:        178
HTML transferred:       42 bytes
Requests per second:    186.08 [#/sec] (mean)
Time per request:       5.374 [ms] (mean)
Time per request:       5.374 [ms] (mean, across all concurrent requests)
Transfer rate:          35.62 [Kbytes/sec] received
                        32.35 kb/s sent
                        67.96 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    205.85 [#/sec] (mean)
Time per request:       4.858 [ms] (mean)
Time per request:       4.858 [ms] (mean, across all concurrent requests)
Transfer rate:          39.60 [Kbytes/sec] received
                        35.98 kb/s sent
                        75.58 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    196.62 [#/sec] (mean)
Time per request:       5.086 [ms] (mean)
Time per request:       5.086 [ms] (mean, across all concurrent requests)
Transfer rate:          37.83 [Kbytes/sec] received
                        34.37 kb/s sent
                        72.20 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    208.72 [#/sec] (mean)
Time per request:       4.791 [ms] (mean)
Time per request:       4.791 [ms] (mean, across all concurrent requests)
Transfer rate:          40.16 [Kbytes/sec] received
                        36.49 kb/s sent
                        76.64 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    164.37 [#/sec] (mean)
Time per request:       6.084 [ms] (mean)
Time per request:       6.084 [ms] (mean, across all concurrent requests)
Transfer rate:          31.62 [Kbytes/sec] received
                        28.73 kb/s sent
                        60.35 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    197.36 [#/sec] (mean)
Time per request:       5.067 [ms] (mean)
Time per request:       5.067 [ms] (mean, across all concurrent requests)
Transfer rate:          37.97 [Kbytes/sec] received
                        34.50 kb/s sent
                        72.47 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    209.12 [#/sec] (mean)
Time per request:       4.782 [ms] (mean)
Time per request:       4.782 [ms] (mean, across all concurrent requests)
Transfer rate:          40.23 [Kbytes/sec] received
                        36.55 kb/s sent
                        76.79 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.008 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    121.42 [#/sec] (mean)
Time per request:       8.236 [ms] (mean)
Time per request:       8.236 [ms] (mean, across all concurrent requests)
Transfer rate:          23.36 [Kbytes/sec] received
                        21.22 kb/s sent
                        44.58 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     8    8   0.0      8       8
Waiting:        8    8   0.0      8       8
Total:          8    8   0.0      8       8
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    158.05 [#/sec] (mean)
Time per request:       6.327 [ms] (mean)
Time per request:       6.327 [ms] (mean, across all concurrent requests)
Transfer rate:          30.41 [Kbytes/sec] received
                        27.63 kb/s sent
                        58.04 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.008 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    126.47 [#/sec] (mean)
Time per request:       7.907 [ms] (mean)
Time per request:       7.907 [ms] (mean, across all concurrent requests)
Transfer rate:          24.33 [Kbytes/sec] received
                        22.11 kb/s sent
                        46.44 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     8    8   0.0      8       8
Waiting:        8    8   0.0      8       8
Total:          8    8   0.0      8       8
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    166.22 [#/sec] (mean)
Time per request:       6.016 [ms] (mean)
Time per request:       6.016 [ms] (mean, across all concurrent requests)
Transfer rate:          31.98 [Kbytes/sec] received
                        29.06 kb/s sent
                        61.04 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        42 bytes

Concurrency Level:      1
Time taken for tests:   0.007 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      196 bytes
Total body sent:        178
HTML transferred:       42 bytes
Requests per second:    153.59 [#/sec] (mean)
Time per request:       6.511 [ms] (mean)
Time per request:       6.511 [ms] (mean, across all concurrent requests)
Transfer rate:          29.40 [Kbytes/sec] received
                        26.70 kb/s sent
                        56.09 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    156.94 [#/sec] (mean)
Time per request:       6.372 [ms] (mean)
Time per request:       6.372 [ms] (mean, across all concurrent requests)
Transfer rate:          30.19 [Kbytes/sec] received
                        27.43 kb/s sent
                        57.63 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    219.11 [#/sec] (mean)
Time per request:       4.564 [ms] (mean)
Time per request:       4.564 [ms] (mean, across all concurrent requests)
Transfer rate:          42.15 [Kbytes/sec] received
                        38.30 kb/s sent
                        80.45 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    172.92 [#/sec] (mean)
Time per request:       5.783 [ms] (mean)
Time per request:       5.783 [ms] (mean, across all concurrent requests)
Transfer rate:          33.27 [Kbytes/sec] received
                        30.23 kb/s sent
                        63.49 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    205.63 [#/sec] (mean)
Time per request:       4.863 [ms] (mean)
Time per request:       4.863 [ms] (mean, across all concurrent requests)
Transfer rate:          39.56 [Kbytes/sec] received
                        35.95 kb/s sent
                        75.51 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    190.22 [#/sec] (mean)
Time per request:       5.257 [ms] (mean)
Time per request:       5.257 [ms] (mean, across all concurrent requests)
Transfer rate:          36.60 [Kbytes/sec] received
                        33.25 kb/s sent
                        69.85 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    208.94 [#/sec] (mean)
Time per request:       4.786 [ms] (mean)
Time per request:       4.786 [ms] (mean, across all concurrent requests)
Transfer rate:          40.20 [Kbytes/sec] received
                        36.52 kb/s sent
                        76.72 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    207.60 [#/sec] (mean)
Time per request:       4.817 [ms] (mean)
Time per request:       4.817 [ms] (mean, across all concurrent requests)
Transfer rate:          39.94 [Kbytes/sec] received
                        36.29 kb/s sent
                        76.23 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    209.95 [#/sec] (mean)
Time per request:       4.763 [ms] (mean)
Time per request:       4.763 [ms] (mean, across all concurrent requests)
Transfer rate:          40.39 [Kbytes/sec] received
                        36.70 kb/s sent
                        77.09 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    194.74 [#/sec] (mean)
Time per request:       5.135 [ms] (mean)
Time per request:       5.135 [ms] (mean, across all concurrent requests)
Transfer rate:          37.47 [Kbytes/sec] received
                        34.04 kb/s sent
                        71.51 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    190.26 [#/sec] (mean)
Time per request:       5.256 [ms] (mean)
Time per request:       5.256 [ms] (mean, across all concurrent requests)
Transfer rate:          36.60 [Kbytes/sec] received
                        33.26 kb/s sent
                        69.86 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        42 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      196 bytes
Total body sent:        178
HTML transferred:       42 bytes
Requests per second:    185.19 [#/sec] (mean)
Time per request:       5.400 [ms] (mean)
Time per request:       5.400 [ms] (mean, across all concurrent requests)
Transfer rate:          35.45 [Kbytes/sec] received
                        32.19 kb/s sent
                        67.64 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.009 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    107.17 [#/sec] (mean)
Time per request:       9.331 [ms] (mean)
Time per request:       9.331 [ms] (mean, across all concurrent requests)
Transfer rate:          20.62 [Kbytes/sec] received
                        18.73 kb/s sent
                        39.35 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     9    9   0.0      9       9
Waiting:        9    9   0.0      9       9
Total:          9    9   0.0      9       9
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.007 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    142.15 [#/sec] (mean)
Time per request:       7.035 [ms] (mean)
Time per request:       7.035 [ms] (mean, across all concurrent requests)
Transfer rate:          27.35 [Kbytes/sec] received
                        24.85 kb/s sent
                        52.19 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     7    7   0.0      7       7
Waiting:        7    7   0.0      7       7
Total:          7    7   0.0      7       7
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    218.58 [#/sec] (mean)
Time per request:       4.575 [ms] (mean)
Time per request:       4.575 [ms] (mean, across all concurrent requests)
Transfer rate:          42.05 [Kbytes/sec] received
                        38.21 kb/s sent
                        80.26 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    203.05 [#/sec] (mean)
Time per request:       4.925 [ms] (mean)
Time per request:       4.925 [ms] (mean, across all concurrent requests)
Transfer rate:          39.06 [Kbytes/sec] received
                        35.49 kb/s sent
                        74.56 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    199.40 [#/sec] (mean)
Time per request:       5.015 [ms] (mean)
Time per request:       5.015 [ms] (mean, across all concurrent requests)
Transfer rate:          38.36 [Kbytes/sec] received
                        34.86 kb/s sent
                        73.22 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    221.68 [#/sec] (mean)
Time per request:       4.511 [ms] (mean)
Time per request:       4.511 [ms] (mean, across all concurrent requests)
Transfer rate:          42.65 [Kbytes/sec] received
                        38.75 kb/s sent
                        81.40 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    185.70 [#/sec] (mean)
Time per request:       5.385 [ms] (mean)
Time per request:       5.385 [ms] (mean, across all concurrent requests)
Transfer rate:          35.73 [Kbytes/sec] received
                        32.46 kb/s sent
                        68.19 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    172.89 [#/sec] (mean)
Time per request:       5.784 [ms] (mean)
Time per request:       5.784 [ms] (mean, across all concurrent requests)
Transfer rate:          33.26 [Kbytes/sec] received
                        30.22 kb/s sent
                        63.48 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    209.60 [#/sec] (mean)
Time per request:       4.771 [ms] (mean)
Time per request:       4.771 [ms] (mean, across all concurrent requests)
Transfer rate:          40.32 [Kbytes/sec] received
                        36.64 kb/s sent
                        76.96 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    202.10 [#/sec] (mean)
Time per request:       4.948 [ms] (mean)
Time per request:       4.948 [ms] (mean, across all concurrent requests)
Transfer rate:          38.88 [Kbytes/sec] received
                        35.33 kb/s sent
                        74.21 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        42 bytes

Concurrency Level:      1
Time taken for tests:   0.009 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      196 bytes
Total body sent:        178
HTML transferred:       42 bytes
Requests per second:    116.75 [#/sec] (mean)
Time per request:       8.565 [ms] (mean)
Time per request:       8.565 [ms] (mean, across all concurrent requests)
Transfer rate:          22.35 [Kbytes/sec] received
                        20.30 kb/s sent
                        42.64 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     8    8   0.0      8       8
Waiting:        8    8   0.0      8       8
Total:          9    9   0.0      9       9
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    163.19 [#/sec] (mean)
Time per request:       6.128 [ms] (mean)
Time per request:       6.128 [ms] (mean, across all concurrent requests)
Transfer rate:          31.39 [Kbytes/sec] received
                        28.53 kb/s sent
                        59.92 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.007 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    142.05 [#/sec] (mean)
Time per request:       7.040 [ms] (mean)
Time per request:       7.040 [ms] (mean, across all concurrent requests)
Transfer rate:          27.33 [Kbytes/sec] received
                        24.83 kb/s sent
                        52.16 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     7    7   0.0      7       7
Waiting:        7    7   0.0      7       7
Total:          7    7   0.0      7       7
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    227.89 [#/sec] (mean)
Time per request:       4.388 [ms] (mean)
Time per request:       4.388 [ms] (mean, across all concurrent requests)
Transfer rate:          43.84 [Kbytes/sec] received
                        39.84 kb/s sent
                        83.68 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    174.49 [#/sec] (mean)
Time per request:       5.731 [ms] (mean)
Time per request:       5.731 [ms] (mean, across all concurrent requests)
Transfer rate:          33.57 [Kbytes/sec] received
                        30.50 kb/s sent
                        64.07 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    162.26 [#/sec] (mean)
Time per request:       6.163 [ms] (mean)
Time per request:       6.163 [ms] (mean, across all concurrent requests)
Transfer rate:          31.22 [Kbytes/sec] received
                        28.36 kb/s sent
                        59.58 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    202.22 [#/sec] (mean)
Time per request:       4.945 [ms] (mean)
Time per request:       4.945 [ms] (mean, across all concurrent requests)
Transfer rate:          38.90 [Kbytes/sec] received
                        35.35 kb/s sent
                        74.25 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    211.10 [#/sec] (mean)
Time per request:       4.737 [ms] (mean)
Time per request:       4.737 [ms] (mean, across all concurrent requests)
Transfer rate:          40.61 [Kbytes/sec] received
                        36.90 kb/s sent
                        77.51 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    217.49 [#/sec] (mean)
Time per request:       4.598 [ms] (mean)
Time per request:       4.598 [ms] (mean, across all concurrent requests)
Transfer rate:          41.84 [Kbytes/sec] received
                        38.02 kb/s sent
                        79.86 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    205.25 [#/sec] (mean)
Time per request:       4.872 [ms] (mean)
Time per request:       4.872 [ms] (mean, across all concurrent requests)
Transfer rate:          39.49 [Kbytes/sec] received
                        35.88 kb/s sent
                        75.37 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    167.76 [#/sec] (mean)
Time per request:       5.961 [ms] (mean)
Time per request:       5.961 [ms] (mean, across all concurrent requests)
Transfer rate:          32.27 [Kbytes/sec] received
                        29.32 kb/s sent
                        61.60 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        42 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      196 bytes
Total body sent:        178
HTML transferred:       42 bytes
Requests per second:    201.73 [#/sec] (mean)
Time per request:       4.957 [ms] (mean)
Time per request:       4.957 [ms] (mean, across all concurrent requests)
Transfer rate:          38.61 [Kbytes/sec] received
                        35.07 kb/s sent
                        73.68 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    163.64 [#/sec] (mean)
Time per request:       6.111 [ms] (mean)
Time per request:       6.111 [ms] (mean, across all concurrent requests)
Transfer rate:          31.48 [Kbytes/sec] received
                        28.60 kb/s sent
                        60.09 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.008 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    126.86 [#/sec] (mean)
Time per request:       7.883 [ms] (mean)
Time per request:       7.883 [ms] (mean, across all concurrent requests)
Transfer rate:          24.40 [Kbytes/sec] received
                        22.17 kb/s sent
                        46.58 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     8    8   0.0      8       8
Waiting:        8    8   0.0      8       8
Total:          8    8   0.0      8       8
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    164.26 [#/sec] (mean)
Time per request:       6.088 [ms] (mean)
Time per request:       6.088 [ms] (mean, across all concurrent requests)
Transfer rate:          31.60 [Kbytes/sec] received
                        28.71 kb/s sent
                        60.31 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    179.18 [#/sec] (mean)
Time per request:       5.581 [ms] (mean)
Time per request:       5.581 [ms] (mean, across all concurrent requests)
Transfer rate:          34.47 [Kbytes/sec] received
                        31.32 kb/s sent
                        65.79 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    223.71 [#/sec] (mean)
Time per request:       4.470 [ms] (mean)
Time per request:       4.470 [ms] (mean, across all concurrent requests)
Transfer rate:          43.04 [Kbytes/sec] received
                        39.11 kb/s sent
                        82.14 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    201.65 [#/sec] (mean)
Time per request:       4.959 [ms] (mean)
Time per request:       4.959 [ms] (mean, across all concurrent requests)
Transfer rate:          38.79 [Kbytes/sec] received
                        35.25 kb/s sent
                        74.04 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    238.38 [#/sec] (mean)
Time per request:       4.195 [ms] (mean)
Time per request:       4.195 [ms] (mean, across all concurrent requests)
Transfer rate:          45.86 [Kbytes/sec] received
                        41.67 kb/s sent
                        87.53 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    188.79 [#/sec] (mean)
Time per request:       5.297 [ms] (mean)
Time per request:       5.297 [ms] (mean, across all concurrent requests)
Transfer rate:          36.32 [Kbytes/sec] received
                        33.00 kb/s sent
                        69.32 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    230.15 [#/sec] (mean)
Time per request:       4.345 [ms] (mean)
Time per request:       4.345 [ms] (mean, across all concurrent requests)
Transfer rate:          44.28 [Kbytes/sec] received
                        40.23 kb/s sent
                        84.51 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    200.96 [#/sec] (mean)
Time per request:       4.976 [ms] (mean)
Time per request:       4.976 [ms] (mean, across all concurrent requests)
Transfer rate:          38.66 [Kbytes/sec] received
                        35.13 kb/s sent
                        73.79 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        42 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      196 bytes
Total body sent:        178
HTML transferred:       42 bytes
Requests per second:    226.04 [#/sec] (mean)
Time per request:       4.424 [ms] (mean)
Time per request:       4.424 [ms] (mean, across all concurrent requests)
Transfer rate:          43.27 [Kbytes/sec] received
                        39.29 kb/s sent
                        82.56 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    164.55 [#/sec] (mean)
Time per request:       6.077 [ms] (mean)
Time per request:       6.077 [ms] (mean, across all concurrent requests)
Transfer rate:          31.66 [Kbytes/sec] received
                        28.76 kb/s sent
                        60.42 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    216.08 [#/sec] (mean)
Time per request:       4.628 [ms] (mean)
Time per request:       4.628 [ms] (mean, across all concurrent requests)
Transfer rate:          41.57 [Kbytes/sec] received
                        37.77 kb/s sent
                        79.34 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    214.96 [#/sec] (mean)
Time per request:       4.652 [ms] (mean)
Time per request:       4.652 [ms] (mean, across all concurrent requests)
Transfer rate:          41.35 [Kbytes/sec] received
                        37.58 kb/s sent
                        78.93 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    185.05 [#/sec] (mean)
Time per request:       5.404 [ms] (mean)
Time per request:       5.404 [ms] (mean, across all concurrent requests)
Transfer rate:          35.60 [Kbytes/sec] received
                        32.35 kb/s sent
                        67.95 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    196.23 [#/sec] (mean)
Time per request:       5.096 [ms] (mean)
Time per request:       5.096 [ms] (mean, across all concurrent requests)
Transfer rate:          37.75 [Kbytes/sec] received
                        34.30 kb/s sent
                        72.05 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    196.58 [#/sec] (mean)
Time per request:       5.087 [ms] (mean)
Time per request:       5.087 [ms] (mean, across all concurrent requests)
Transfer rate:          37.82 [Kbytes/sec] received
                        34.36 kb/s sent
                        72.18 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    221.93 [#/sec] (mean)
Time per request:       4.506 [ms] (mean)
Time per request:       4.506 [ms] (mean, across all concurrent requests)
Transfer rate:          42.69 [Kbytes/sec] received
                        38.79 kb/s sent
                        81.49 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    207.17 [#/sec] (mean)
Time per request:       4.827 [ms] (mean)
Time per request:       4.827 [ms] (mean, across all concurrent requests)
Transfer rate:          39.86 [Kbytes/sec] received
                        36.21 kb/s sent
                        76.07 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    165.43 [#/sec] (mean)
Time per request:       6.045 [ms] (mean)
Time per request:       6.045 [ms] (mean, across all concurrent requests)
Transfer rate:          31.83 [Kbytes/sec] received
                        28.92 kb/s sent
                        60.74 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    207.86 [#/sec] (mean)
Time per request:       4.811 [ms] (mean)
Time per request:       4.811 [ms] (mean, across all concurrent requests)
Transfer rate:          39.99 [Kbytes/sec] received
                        36.33 kb/s sent
                        76.32 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        42 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      196 bytes
Total body sent:        178
HTML transferred:       42 bytes
Requests per second:    197.98 [#/sec] (mean)
Time per request:       5.051 [ms] (mean)
Time per request:       5.051 [ms] (mean, across all concurrent requests)
Transfer rate:          37.89 [Kbytes/sec] received
                        34.41 kb/s sent
                        72.31 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    211.77 [#/sec] (mean)
Time per request:       4.722 [ms] (mean)
Time per request:       4.722 [ms] (mean, across all concurrent requests)
Transfer rate:          40.74 [Kbytes/sec] received
                        37.02 kb/s sent
                        77.76 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    210.17 [#/sec] (mean)
Time per request:       4.758 [ms] (mean)
Time per request:       4.758 [ms] (mean, across all concurrent requests)
Transfer rate:          40.43 [Kbytes/sec] received
                        36.74 kb/s sent
                        77.17 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    204.37 [#/sec] (mean)
Time per request:       4.893 [ms] (mean)
Time per request:       4.893 [ms] (mean, across all concurrent requests)
Transfer rate:          39.32 [Kbytes/sec] received
                        35.73 kb/s sent
                        75.04 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    223.86 [#/sec] (mean)
Time per request:       4.467 [ms] (mean)
Time per request:       4.467 [ms] (mean, across all concurrent requests)
Transfer rate:          43.07 [Kbytes/sec] received
                        39.13 kb/s sent
                        82.20 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    186.46 [#/sec] (mean)
Time per request:       5.363 [ms] (mean)
Time per request:       5.363 [ms] (mean, across all concurrent requests)
Transfer rate:          35.87 [Kbytes/sec] received
                        32.59 kb/s sent
                        68.47 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    206.83 [#/sec] (mean)
Time per request:       4.835 [ms] (mean)
Time per request:       4.835 [ms] (mean, across all concurrent requests)
Transfer rate:          39.79 [Kbytes/sec] received
                        36.15 kb/s sent
                        75.94 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    167.64 [#/sec] (mean)
Time per request:       5.965 [ms] (mean)
Time per request:       5.965 [ms] (mean, across all concurrent requests)
Transfer rate:          32.25 [Kbytes/sec] received
                        29.31 kb/s sent
                        61.56 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    220.70 [#/sec] (mean)
Time per request:       4.531 [ms] (mean)
Time per request:       4.531 [ms] (mean, across all concurrent requests)
Transfer rate:          42.46 [Kbytes/sec] received
                        38.58 kb/s sent
                        81.04 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    200.16 [#/sec] (mean)
Time per request:       4.996 [ms] (mean)
Time per request:       4.996 [ms] (mean, across all concurrent requests)
Transfer rate:          38.51 [Kbytes/sec] received
                        34.99 kb/s sent
                        73.50 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.004 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    225.28 [#/sec] (mean)
Time per request:       4.439 [ms] (mean)
Time per request:       4.439 [ms] (mean, across all concurrent requests)
Transfer rate:          43.34 [Kbytes/sec] received
                        39.38 kb/s sent
                        82.72 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          4    4   0.0      4       4
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        42 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      196 bytes
Total body sent:        178
HTML transferred:       42 bytes
Requests per second:    193.99 [#/sec] (mean)
Time per request:       5.155 [ms] (mean)
Time per request:       5.155 [ms] (mean, across all concurrent requests)
Transfer rate:          37.13 [Kbytes/sec] received
                        33.72 kb/s sent
                        70.85 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    172.12 [#/sec] (mean)
Time per request:       5.810 [ms] (mean)
Time per request:       5.810 [ms] (mean, across all concurrent requests)
Transfer rate:          33.11 [Kbytes/sec] received
                        30.09 kb/s sent
                        63.20 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    209.86 [#/sec] (mean)
Time per request:       4.765 [ms] (mean)
Time per request:       4.765 [ms] (mean, across all concurrent requests)
Transfer rate:          40.37 [Kbytes/sec] received
                        36.69 kb/s sent
                        77.06 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    173.46 [#/sec] (mean)
Time per request:       5.765 [ms] (mean)
Time per request:       5.765 [ms] (mean, across all concurrent requests)
Transfer rate:          33.37 [Kbytes/sec] received
                        30.32 kb/s sent
                        63.69 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        5    5   0.0      5       5
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    217.72 [#/sec] (mean)
Time per request:       4.593 [ms] (mean)
Time per request:       4.593 [ms] (mean, across all concurrent requests)
Transfer rate:          41.89 [Kbytes/sec] received
                        38.06 kb/s sent
                        79.95 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4    4   0.0      4       4
Waiting:        4    4   0.0      4       4
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    172.53 [#/sec] (mean)
Time per request:       5.796 [ms] (mean)
Time per request:       5.796 [ms] (mean, across all concurrent requests)
Transfer rate:          33.19 [Kbytes/sec] received
                        30.16 kb/s sent
                        63.35 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    157.55 [#/sec] (mean)
Time per request:       6.347 [ms] (mean)
Time per request:       6.347 [ms] (mean, across all concurrent requests)
Transfer rate:          30.31 [Kbytes/sec] received
                        27.54 kb/s sent
                        57.85 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    187.69 [#/sec] (mean)
Time per request:       5.328 [ms] (mean)
Time per request:       5.328 [ms] (mean, across all concurrent requests)
Transfer rate:          36.11 [Kbytes/sec] received
                        32.81 kb/s sent
                        68.92 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    175.22 [#/sec] (mean)
Time per request:       5.707 [ms] (mean)
Time per request:       5.707 [ms] (mean, across all concurrent requests)
Transfer rate:          33.71 [Kbytes/sec] received
                        30.63 kb/s sent
                        64.34 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.006 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    158.70 [#/sec] (mean)
Time per request:       6.301 [ms] (mean)
Time per request:       6.301 [ms] (mean, across all concurrent requests)
Transfer rate:          30.53 [Kbytes/sec] received
                        27.74 kb/s sent
                        58.27 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.0      6       6
Waiting:        6    6   0.0      6       6
Total:          6    6   0.0      6       6
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.29.3
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v2/cities/
Document Length:        43 bytes

Concurrency Level:      1
Time taken for tests:   0.005 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      197 bytes
Total body sent:        179
HTML transferred:       43 bytes
Requests per second:    186.67 [#/sec] (mean)
Time per request:       5.357 [ms] (mean)
Time per request:       5.357 [ms] (mean, across all concurrent requests)
Transfer rate:          35.91 [Kbytes/sec] received
                        32.63 kb/s sent
                        68.54 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    5   0.0      5       5
Waiting:        5    5   0.0      5       5
Total:          5    5   0.0      5       5
```
## delete_summary_DELETE
```
=== DELETE /cities тест ===
Удалён город id=546 (TestCity_20450)
Удалён город id=547 (TestCity_589)
Удалён город id=548 (TestCity_14069)
Удалён город id=549 (TestCity_25310)
Удалён город id=550 (TestCity_15174)
Удалён город id=551 (TestCity_29889)
Удалён город id=552 (TestCity_17125)
Удалён город id=553 (TestCity_20025)
Удалён город id=554 (TestCity_18794)
Удалён город id=555 (TestCity_12194)
```
## localhost_api_v1_health_GET
```
=== GET /health (JSON) тест: http://localhost/api/v1/health ===
app_read2: 25 запросов
app_main: 50 запросов
app_read1: 25 запросов
```
## localhost_api_v2_cities__POST
```
=== POST /cities (JSON v2) тест: http://localhost/api/v2/cities/ ===
Создан город TestCity_20450 с id=546
Создан город TestCity_589 с id=547
Создан город TestCity_14069 с id=548
Создан город TestCity_25310 с id=549
Создан город TestCity_15174 с id=550
Создан город TestCity_29889 с id=551
Создан город TestCity_17125 с id=552
Создан город TestCity_20025 с id=553
Создан город TestCity_18794 с id=554
Создан город TestCity_12194 с id=555
```
## localhost_api_v2_health_GET
```
=== GET /health (JSON) тест: http://localhost/api/v2/health ===
app_read2: 25 запросов
app_main: 50 запросов
app_read1: 25 запросов
```
