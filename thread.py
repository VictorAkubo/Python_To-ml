import threading
import time

def print_number():
  for v in range(4):
    time.sleep(1)
    print(v)
    
def print_alpha():
  for a in "ABCDEFGH":
    time.sleep(1)
    print(a)

thread1 = threading.Thread(target=print_number)

thread2 = threading.Thread(target=print_alpha)


thread1.start()
thread2.start()

#join waits for threads to finish before the print("main thread still running") prints

#thread1.join()
#thread2.join()

print("main thread still running")

