from decimal import Decimal, getcontext

getcontext().prec = 10 

faturamento_por_estado = {
    "SP": Decimal("67836.43"),
    "RJ": Decimal("36678.66"),
    "MG": Decimal("29229.88"),
    "ES": Decimal("27165.48"),
    "Outros": Decimal("19849.53")
}

def formatar_moeda(valor):
    
    return f"{valor:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ',')


valor_total = sum(faturamento_por_estado.values())

print(f"--- CÁLCULO DO PERCENTUAL DE REPRESENTAÇÃO ---")
print(f"Faturamento Total: R$ {formatar_moeda(valor_total)}")
print("-" * 45)


percentual_total = Decimal(0)
for estado, faturamento in faturamento_por_estado.items():
    percentual = (faturamento / valor_total) * 100
    percentual_total += percentual
    
    
    print(f"{estado:<8}: R$ {formatar_moeda(faturamento):<12} | {percentual:7.2f}%")

print("-" * 45)

print(f"Total Percentual: {percentual_total:.2f}%")