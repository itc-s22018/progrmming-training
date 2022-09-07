import math 

pointA = {"x": 100.0, "y": 100.0}
print("スタート地点:" ,pointA)
print("進む方向（角度）?:", end="")
angle = float(input())
"""
ここで計算が必要
"""
distAC = math.cos(math.radians(-67.5)) * 100.0
distBC = math.sin(math.radians(-67.5)) * 100.0
print("スタート地点からx座標で進む距離:", distAC)
print("スタート地点からy座標で進む距離:", distBC)

pointB = {
        "x": pointA["x"] + distAC,
        "y": pointA["y"] + distBC
        print(f"スタート地点から'{angle:.2f}'北北東へ１００移動した先:",
              f"'x:{pointB['x']:.2f} y:{pointB['y']:.2f}'")
        `
