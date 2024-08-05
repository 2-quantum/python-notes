# for loop executes its code limited amount of times unlike to
# while which runs unlimited amount of times i.e. until the condition is not met

import time

name = "Om Prabhat"

for i in range(10):
    print(i)
time.sleep(5)
for i in range(1, 100+1):
    print(i)
time.sleep(5)
for i in range(1, 11, 2):
    print(i)
time.sleep(5)
for i in range(2, 11, 2):
    print(i)
for i in name:
    print(i)
# counter
print("Countdown Starts.")
for seconds in range(10, -1, -1): # -1 because we have to print till 0
    print(seconds)
    time.sleep(1)
