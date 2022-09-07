#for i in range(8):
   #print("hello python!")
msg1 = ["The", "fox", "jumped", "over", "the", "fence", "."]
for i in msg1:
    print(i)

print("whileループ")
i = 0
while i < len(msg1):
    print(msg1[i])
    i += 1

print("数字を入力してください: ", end="")
num = float(input())
while num > 0:
    print(f"{num:}の二乗は '{num**2:}' です")
    print("次の数字を入力してください: ", end="")
    num = float(input())

