#1 ano -> 3%
#2 anos -> 5%

valor_produto = float(input());
quantidade_anos_garantia = int(input());

valor_total = float();

if(quantidade_anos_garantia == 1):
    valor_total = valor_produto * 1.03
elif(quantidade_anos_garantia == 2):
    valor_total = valor_produto * 1.05
else:
    valor_total = valor_produto

print("%.2f" % valor_total)