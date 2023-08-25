n = int(input())
um = "one  "
dois = "two  "
tres = "three"
for i in range(n):
    palavra = input().lower()
    if len(palavra) == 3:
        acerto = 0
        for i in range(len(palavra)):
            if palavra[i] == um[i]:
                acerto += 1
        if acerto >= 2:
            print(1)
        acerto = 0
        for i in range(len(palavra)):
            if palavra[i] == dois[i]:
                acerto += 1
        if acerto >= 2:
            print(2)
    else:
        print(3)