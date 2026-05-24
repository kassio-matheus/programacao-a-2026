quantidade_itens_array = int(input())

items_a = [int(input()) for _ in range(quantidade_itens_array)]
items_b = [int(input()) for _ in range(quantidade_itens_array)]

for i in range(quantidade_itens_array):
    print(items_a[i])
    print(items_b[i])