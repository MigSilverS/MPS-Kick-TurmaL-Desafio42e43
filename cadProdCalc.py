codigo = input("Digite o código do produto: ")
nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço unitário: "))

valor_total = quantidade + preco
print("\nInformações do produto cadastrado:")
print(f"Código: {codigo}")
print(f"Nome: {nome_produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: {preco:.2f}")
print(f"Valor total da compra: {valor_total:.2f}")
