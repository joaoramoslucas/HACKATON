while True:
    a = float(input())
    b = float(input())
    if a == 0 and b == 0:
        break
    media = (a * 3.5 + b * 7.5 ) / 11
    print(f'{media:.5f}')