def calcular_porcentagem(votos, total_votos):
    return (votos / total_votos) * 100

# Leitura dos dados
total_eleitores = int(input("Informe o total de eleitores: "))
votos_candidato_a = int(input("Informe o total de votos para o candidato A: "))
votos_candidato_b = int(input("Informe o total de votos para o candidato B: "))
votos_candidato_c = int(input("Informe o total de votos para o candidato C: "))

# Calcula o total de votos válidos
total_votos_validos = votos_candidato_a + votos_candidato_b + votos_candidato_c

# Calcula as porcentagens
porcentagem_a = calcular_porcentagem(votos_candidato_a, total_votos_validos)
porcentagem_b = calcular_porcentagem(votos_candidato_b, total_votos_validos)
porcentagem_c = calcular_porcentagem(votos_candidato_c, total_votos_validos)

# Calcula a porcentagem de votos anulados
votos_anulados = total_eleitores - total_votos_validos
porcentagem_anulados = calcular_porcentagem(votos_anulados, total_eleitores)

# Verifica se haverá segundo turno
if porcentagem_a < 51:
    segundo_turno = True
else:
    segundo_turno = False

# Mostra os resultados
print(f"Porcentagem de votos para o candidato A: {porcentagem_a:.2f}%")
print(f"Porcentagem de votos para o candidato B: {porcentagem_b:.2f}%")
print(f"Porcentagem de votos para o candidato C: {porcentagem_c:.2f}%")
print(f"Porcentagem de votos anulados: {porcentagem_anulados:.2f}%")

if segundo_turno:
    print(f"Haverá segundo turno entre os candidatos A e B.")
else:
    print(f"O candidato A foi eleito no primeiro turno.")
