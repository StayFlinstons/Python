a = 0

for i in range(10):
    a = a + 1
    print(f"Tabuada do {i+1}")
    for i in range(10):
        print(f"Indice: {(i + 1) * a}")