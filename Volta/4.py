frase = "suBIno onibus".lower().replace(" ", "")

palindromo = frase[::-1]

if frase == palindromo:
    print('isso ai')
else:
    print('deu bosta')