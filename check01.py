for n in range(100):
    print(n)
if n % 15 == 0:
    print(n, n * 1.5)
elif n % 5 == 0:
    print(n, n // 2)
elif n % 3 == 0:
    print(n, n * 2)
else:
    print(n)
    # nが３の倍数なら２倍した数
    # nが５の倍数なら、２で割った数（整数）
    # nが３でも５でも割れるなら、１．５倍の数
    # それ以外何もしない（１つ目は出力だけ）

