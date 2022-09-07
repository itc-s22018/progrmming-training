import random

print("グー(0) チョキ(1) パー(2) を選んでください:", end="")
player = int(input())
cpu_hands = [
        ["グー", "チョキ", "パー"],
        ["パー", "グー", "チョキ"],
        ["チョキ", "パー", "グー"],
]
message = ("アイコです", "コンピュータの勝ちです", "プレイヤーの勝ちです")

result = 0
if random.randint(0, 99) < 72 :
    result = 1
elif random.randint(0, 99) < 8:
    result = 2
print(f"コンピュータの手: {cpu_hands[result][player]}")
print(message[result])

