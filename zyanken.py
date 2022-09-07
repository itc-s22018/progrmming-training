import random

hands = {0:"グー", 1:"チョキ", 2:"パー"}

print("グー(0) チョキ(1) パー(2) を選んでください:",end="")
player_hand = int(input())
cpu_hand = random.randint(0,2)

print(f"コンピュータの手: {hands[cpu_hand]}")
print(f"  プレイヤーの手: {hands[player_hand]}")
if   player_hand > cpu_hand:
    print("コンピュータの勝ちです")
elif player_hand < cpu_hand:
    print("プレイヤーの勝ちです")
else:
    print("アイコです")
