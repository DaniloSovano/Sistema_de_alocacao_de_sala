import pandas as pd
import random

caminho_arquivo = "C:\Users\Esdra\Documents\Sistema_de_alocacao_de_sala\salas_reservadas.xlsx"


# Carregar os dados do arquivo original
tabelas = pd.read_excel(caminho_arquivo, sheet_name=None, index_col=0, engine="openpyxl")

# Lista de professores e matérias de computação
professores_materias = [
    ("Dr. Carlos Souza", "Algoritmos"),
    ("Prof. Ana Lima", "Estruturas de Dados"),
    ("Dr. Ricardo Mendes", "Banco de Dados"),
    ("Prof. Fernanda Costa", "Programação Web"),
    ("Dr. João Silva", "Inteligência Artificial"),
    ("Prof. Laura Martins", "Redes de Computadores"),
    ("Dr. Marcos Oliveira", "Segurança da Informação"),
    ("Prof. Beatriz Santos", "Desenvolvimento Mobile"),
    ("Dr. Pedro Rocha", "Engenharia de Software"),
    ("Prof. Camila Ribeiro", "Computação Gráfica")
]

# Percorrer cada dia da semana e preencher aleatoriamente algumas reservas
for dia, df in tabelas.items():
    for _ in range(random.randint(5, 15)):  # Define um número aleatório de reservas por dia
        sala = random.choice(df.index)
        horario = random.choice(df.columns)

        if df.at[sala, horario] == "-":  # Apenas preenche se estiver vazio
            professor, materia = random.choice(professores_materias)
            df.at[sala, horario] = f"{professor} ({materia})"

# Caminho do novo arquivo gerado
novo_caminho = "/mnt/data/salas_reservadas_computacao.xlsx"

# Salvar os novos dados
with pd.ExcelWriter(novo_caminho, engine="openpyxl") as writer:
    for dia, df in tabelas.items():
        df.to_excel(writer, sheet_name=dia)

novo_caminho
