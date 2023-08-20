import time
import winsound

print("Enter the time in hr min sec format",end=" ")

hr,min,sec = list(map(int, input().split()))

tot=(hr*3600)+(min*60)+(sec)

for i in range(1, tot + 1):
  tot=tot-1
  if i % 60 == 0:
    min = min - 1
  elif i % 3600 == 0:
    hr = hr - 1
  else:
    sec = sec - 1
  print(hr,end="")
  print(":",end="")
  print(min,end="")
  print(":",end="")
  print(sec,end="")
  print("\r",end="")
  if tot==0:
    print("Time Over !")
    for i in range(10):
      winsound.Beep(1000,1000)
    break
  time.sleep(1)
  
        
