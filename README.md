# web-server-benchmark-using-python
This repository include python code to benchmark web servers to know how much traffic and connection they can handle..
# How to use the script 
1. pull the repository
2. run the script as follows <br>
   python3 test.py www.domain.com PortNumber NumberOfProcesses threads  > /dev/null 2>&1 <br>
   for instance
   python3 www.example.com 443 2 50 > /dev/null 2>&1 <br>
   Running this command will create 2 processes and each process will open 50 threads. <br>
   Note: each threads will send get request every 1 second you can change this in line 14.
```diff
- Please please do not use this script for DDoS attacks.
```
