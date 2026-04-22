quantidade = int(input("Quantas notas deseja digitar? "))

soma = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

media = soma / quantidade

print(f"Média final: {media:.2f}")

if media >= 7:
    print("APROVADO!")
else:
    print("REPROVADO!")
