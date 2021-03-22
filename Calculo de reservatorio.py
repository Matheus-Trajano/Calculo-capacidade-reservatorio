h = float(input("altura do reservatório (m):"))
largura = float(input("largura do reservatório (m):"))
comprimento = float(input("comprimento do reservatório (m):"))
consumo_medio = float(input("quantos litros consome por dia?"))  # em litros/dia.

dimen1 = float(h * 10)
dimen2 = float(largura * 10)
dimen3 = float(comprimento * 10)

v_reservatorio = dimen1 * dimen2 * dimen3
print("Seu reservatório tem uma capacidade total de:", v_reservatorio, "litros.")

autonomia_dias = v_reservatorio / consumo_medio
print("você tem autônomia para:", autonomia_dias, "dias")

if autonomia_dias < 2:
    print(f"seu consumo ainda é considerado elevado.")
elif autonomia_dias <= 7:
    print(f"seu consumo é moderado,está indo bem.")
else:
    print(f"seu consumo de água está reduzido.")
