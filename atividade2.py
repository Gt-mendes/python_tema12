nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}° nome: ")
    nomes.append(nome)

print("Nomes em maiúsculo:")
for nome in nomes:
    print(nome.upper())
