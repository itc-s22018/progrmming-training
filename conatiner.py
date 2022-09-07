data = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,
        31,33,35,39,41,43,45,47,49
]

print("data[11]:", data[11])
print("data[19]:", data[19])
print("data[0]:", data[0])
print("data[7]:", data[7])

for d in data:
    print("{0}の２倍は: {1:3d}".format(d, d * 2))

colors = {
        'red': 'rgb(255, 0, 0)',
        'green': 'rgb(0, 255, 0)',
        'blue': 'rgb(0, 0, 255)',
        'cyan': 'rgb(0, 255, 255)',
        'greenyello': 'rgb(172, 255, 47)',
        'yello': 'rgb(255, 255, 0)',
        'orange': 'rgb(255, 165, 0)',
        'magenta': 'rgb(255, 0, 255)',
}

print("背景色の黄緑(greenyello)のカラーコード:",
        colors['greenyello'])
print("前景色のオレンジ(orange)のカラーコード:",
        colors['orange'])

for key, value in colors.items():
    print(f"{key:12s} => {value}")



