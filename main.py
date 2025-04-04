import pandas as pd
import random

def read_excel_file(file_path):
    # Lê o arquivo Excel
    df = pd.read_excel(file_path)
    return df

def analyze_results(df):
    # Analisar os resultados anteriores para identificar padrões
    # Aqui você pode implementar a lógica de análise que preferir
    # Por exemplo, calcular a frequência de cada número sorteado
    frequency = df.stack().value_counts()
    return frequency

def generate_possible_games(frequency, num_games=10):
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
    for _ in range(num_games):
        game = random.sample(all_numbers[:25], 15)  # Seleciona 15 números aleatórios dos 25 mais frequentes
        possible_games.append(sorted(game))
    return possible_games

def main():
    # Caminho para o arquivo Excel
    file_path = 'Lotofácil.xlsx'
    
    # Ler o arquivo Excel
    df = read_excel_file(file_path)
    
    # Analisar os resultados
    frequency = analyze_results(df)
    
    # Gerar jogos possíveis
    possible_games = generate_possible_games(frequency)
    
    for game in possible_games:
        print(game)

if __name__ == "__main__":
    main()