import pandas as pd
import random
import requests

def download_excel_file(url, output_path):
    # Baixar o arquivo Excel
    response = requests.get(url)
    with open(output_path, 'wb') as file:
        file.write(response.content)

def read_excel_file(file_path):
    # Lê o arquivo Excel
    df = pd.read_excel(file_path)
    return df

def analyze_results(df):
    # Analisar os resultados anteriores para identificar padrões
    frequency = df.stack().value_counts()
    return frequency

def generate_possible_games(frequency, previous_results, num_games=10):
    # Garantir que todos os números sejam inteiros e válidos
    all_numbers = []
    for item in frequency.index:
        try:
            number = int(item)
            all_numbers.append(number)
        except ValueError:
            # Ignorar entradas que não são números válidos
            continue
    
    possible_games = []
    while len(possible_games) < num_games:
        game = sorted(random.sample(all_numbers[:25], 15))  # Seleciona 15 números aleatórios dos 25 mais frequentes
        if game not in previous_results:
            possible_games.append(game)
    return possible_games

def main():
    # URL do arquivo Excel no GitHub
    url = 'https://github.com/Mardoniosc/LOTOFACIL-TESTE/blob/master/Lotof%C3%A1cil.xlsx?raw=true'
    output_path = 'Lotofácil.xlsx'
    
    # Baixar o arquivo Excel
    download_excel_file(url, output_path)
    
    # Ler o arquivo Excel
    df = read_excel_file(output_path)
    
    # Filtrar apenas as colunas que contêm os números sorteados
    number_columns = [col for col in df.columns if df[col].dtype == 'int64' or df[col].dtype == 'float64']
    df_numbers = df[number_columns]
    
    # Analisar os resultados
    frequency = analyze_results(df_numbers)
    
    # Extrair os resultados anteriores
    previous_results = [sorted(list(map(int, row.dropna().tolist()))) for _, row in df_numbers.iterrows()]
    
    # Gerar jogos possíveis
    possible_games = generate_possible_games(frequency, previous_results)
    
    for game in possible_games:
        print(game)

if __name__ == "__main__":
    main()