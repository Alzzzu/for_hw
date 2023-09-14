
a = list(map(int, input("введите числа через пробел: ").split()))
for el in a:
    top = el//2
    counter = 1
    pod_el = 0
    res = {}
    tempo = []
    for i in range(1, top+1):
        if el % i == 0:
            counter += 1
            tempo.append(i)
        if counter > 4:
            tempo = []
            break

    if len(tempo) == 3:
        tempo.append(el)
        print(f"{el}: {tempo}")
