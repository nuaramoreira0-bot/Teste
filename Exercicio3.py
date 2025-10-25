import json
from decimal import Decimal, getcontext
import os 


getcontext().prec = 10 

NOME_DO_ARQUIVO = "dados.json" 


def formatar_moeda(valor):
    return f"{valor:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ',')

dados_mensais = []
try:
    caminho_completo = os.path.abspath(NOME_DO_ARQUIVO)
    print(f"Tentando ler o arquivo: {caminho_completo}")
    
    with open(NOME_DO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        dados_mensais = json.load(arquivo)
    
    print("Arquivo JSON lido com sucesso.")

except FileNotFoundError:
    print(f"\nERRO: O arquivo '{NOME_DO_ARQUIVO}' não foi encontrado.")
    print("Certifique-se de que o arquivo está na mesma pasta onde o script está sendo executado no VS Code.")
    exit()
except json.JSONDecodeError as e:
    print(f"\nERRO: O arquivo '{NOME_DO_ARQUIVO}' está com formato JSON inválido.")
    print(f"Detalhe do erro de parseamento: {e}")
    exit()
except Exception as e:
    print(f"\nERRO inesperado ao carregar o arquivo: {e}")
    exit()


faturamentos_validos = []
dias_totais = len(dados_mensais)

for item in dados_mensais:
    try:
        valor = Decimal(str(item.get('valor', 0.0)))
    except Exception:
        continue 

    if valor > 0:
        faturamentos_validos.append(valor)


if not faturamentos_validos:
    print("\nNão há dados de faturamento válidos (> R$ 0,00) para processamento.")
else:
    dias_com_faturamento = len(faturamentos_validos)
    
    
    menor_faturamento = min(faturamentos_validos)
    
    
    maior_faturamento = max(faturamentos_validos)
    
    
    soma_total = sum(faturamentos_validos)
    media_mensal = soma_total / Decimal(dias_com_faturamento)
    
   
    dias_acima_da_media = sum(1 for f in faturamentos_validos if f > media_mensal)

    print("\n--- ANÁLISE DE FATURAMENTO MENSAL ---")
    print(f"Total de dias no mês (base de dados): {dias_totais}")
    print(f"Dias considerados na média (faturamento > R$ 0,00): {dias_com_faturamento}")
    print(f"Média Mensal de Faturamento (dias válidos): R$ {formatar_moeda(media_mensal)}")
    print("-" * 50)
    
    print(f"• Menor valor de faturamento: R$ {formatar_moeda(menor_faturamento)}")
    print(f"• Maior valor de faturamento: R$ {formatar_moeda(maior_faturamento)}")
    print(f"• Número de dias com faturamento superior à média: {dias_acima_da_media} dias")