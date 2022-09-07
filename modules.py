import math

def circle(r):
    return math.pow(r, 2.0) * math.pi

#print("半径rを入力してください: ", end="")
#radius = float(input())
#area_circle = circle(radius)
#print(f"半径'{radius}'の円の面積は、{area_circle:.4f} です")

data = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]

print(sum(data))

total = 0
for i in data:
    total += i
print(math.fsum(data))

print("randomモジュール")
import random

for _ in range(10):
    print(random.randint(0, 100))

