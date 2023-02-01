#Example One: Program for Python Sleep
import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")

#Example Three: Program to create a digital clock
import time

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result)
  time.sleep(1)