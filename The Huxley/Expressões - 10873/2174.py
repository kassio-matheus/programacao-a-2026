entrada = input("").split()

m3 = float(entrada[0])
custo_por_litro = float(entrada[1])

valor_ser_pago = round((m3 * 1000) * custo_por_litro, 2);
esgoto = round(valor_ser_pago * 0.80, 2);
valor_total = round(valor_ser_pago + esgoto, 2);

print("%.2f" % valor_ser_pago, "%.2f" % esgoto, "%.2f" % valor_total, sep="\n");