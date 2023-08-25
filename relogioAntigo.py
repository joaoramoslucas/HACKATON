while True:
    try:
        h, m = input().split()
        h = int(h)
        m = int(m)
        h//= 30
        m//= 6
        print(f'{h:02}:{m:02}')
    except EOFError:
        break