# Importação das bibliotecas
import pandas as pd
import numpy as np

#FUNÇÕES DE CORREÇÃO DO DB
# Função de leitura do banco de dados quebrado
def read_data():
    try:
        return pd.read_json("broken-database.txt")
    except:
        print("Erro ao abrir o arquivo")
        exit(1)

# Função de correção dos nomes
def correct_names(data):
    replace_dict = {"æ":"a", "¢":"c","ø":"o","ß":"b"}
    data["name"].replace(to_replace=replace_dict, regex=True, inplace=True)

# Função de correção dos preços
def correct_price(data):
    data["price"].astype(np.float64)

# Função de correção da quantidade
def correct_quantity(data):
    data["quantity"] = data["quantity"].fillna(0)

# Função de exportação do DB correto
def export_json(data):
    data.to_json("saida.json", orient="records")

#FUNÇÕES DE VALIDAÇÃO
# Função de leitura do banco de dados correto
def read_correct_data():
    try:
        return pd.read_json("saida.json")
    except:
        print("Erro ao abrir o arquivo")
        exit(1)
        
# Função de impressão dos produtos em categorias em ordem alfabetica e ordem de id em ordem crescente.
def print_list_of_products(data):
    data.sort_values(by=["category", "id"], inplace=True)
    print("\n\n", data, "\n\n")

# Função de impressão da soma dos valores do estoque agrupados por categorias
def print_total_of_categories(data):
    data["total_supply"] = data["quantity"] * data["price"]
    print(data.groupby("category")["total_supply"].sum(), "\n\n")


# Fução main, inicializa todas as outras funções quando carregado o script.
def main():
    data = read_data()
    correct_names(data)
    correct_price(data)
    correct_quantity(data)
    export_json(data)

    correct_data = read_correct_data()
    print_list_of_products(correct_data)
    print_total_of_categories(correct_data)

if __name__ == '__main__':
    main()