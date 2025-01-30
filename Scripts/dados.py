import os
import pandas as pd
import matplotlib.pyplot as plt

# 📂 Substitua pelo caminho correto do seu arquivo
file_path = r"C:\Users\Admin\Documents\DIO\Utilizando prompts para gerar insights de relatorios de vendas\Projeto Base\Data\processed_data\Meganium.xlsx"

# 🔹 Pasta onde os arquivos serão salvos
output_folder = r"C:\Users\Admin\Documents\DIO\Utilizando prompts para gerar insights de relatorios de vendas\Projeto Base\Data\processed_data"

# 🔹 Criar a pasta caso não exista
os.makedirs(output_folder, exist_ok=True)

# 🔹 Carregar os dados da planilha "Cosolidate"
df = pd.read_excel(file_path, sheet_name="Cosolidate")

# 🔹 Agrupar por país e produto para calcular quantidade vendida e receita total
sales_summary = df.groupby(["delivery_country", "product_sold"]).agg(
    total_quantity=("quantity", "sum"),        
    total_revenue=("total_price", "sum")      
).reset_index()

# 🔹 Encontrar o produto mais vendido por país
top_products = sales_summary.loc[sales_summary.groupby("delivery_country")["total_quantity"].idxmax()]

# 🔹 Criar gráfico de vendas por país
plt.figure(figsize=(12, 6))
top_products.groupby("delivery_country")["total_quantity"].sum().plot(kind="bar", color="skyblue")
plt.xlabel("País")
plt.ylabel("Quantidade Vendida")
plt.title("Vendas Totais por País")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# 🔹 Caminho para salvar o gráfico
graph_path = os.path.join(output_folder, "grafico_vendas_por_pais.png")
plt.savefig(graph_path)
plt.close()

# 🔹 Adicionar o caminho do gráfico na tabela
top_products["graph_path"] = graph_path

# 🔹 Caminho para salvar o arquivo CSV
csv_output_path = os.path.join(output_folder, "resumo_produtos_mais_vendidos_por_pais.csv")

# 🔹 Salvar o resumo em CSV
top_products.to_csv(csv_output_path, index=False)

print(f"Resumo salvo em: {csv_output_path}")
print(f"Gráfico salvo em: {graph_path}")



# 🔹 Criar gráfico de vendas por país
plt.figure(figsize=(12, 6))
top_products.groupby("delivery_country")["total_quantity"].sum().plot(kind="bar", color="skyblue")
plt.xlabel("País")
plt.ylabel("Quantidade Vendida")
plt.title("Vendas Totais por País")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# 🔹 Caminho para salvar o gráfico
graph_path = "/mnt/data/grafico_vendas_por_pais.png"
plt.savefig(graph_path)
plt.close()

# 🔹 Adicionar o caminho do gráfico na tabela
top_products["graph_path"] = graph_path

# 🔹 Caminho para salvar o arquivo CSV
csv_output_path = "/mnt/data/resumo_produtos_mais_vendidos_por_pais.csv"

# 🔹 Salvar o resumo em CSV
top_products.to_csv(csv_output_path, index=False)

# 🔹 Retornar os arquivos salvos
csv_output_path, graph_path
