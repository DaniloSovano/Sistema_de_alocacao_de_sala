from tabulate import tabulate
from modules.data import tabelas,horarios
from utils.utils import limpar_tela

def exibir_horarios(dia):
    df = tabelas[dia]
    print(f"\nTabela de Alocação de Salas do dia {dia}:")
    print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex="always"))

def consultar_salas_disponiveis(dia):
    limpar_tela()
    print(f"\nConsulta de salas disponíveis para {dia}\n")

    df = tabelas[dia]

    print("\nHorários disponíveis:")
    for key, value in horarios.items():
        print(f"{key} - {value}")

    try:
        escolha_horario = int(input("\nDigite o número do horário desejado: "))

        if escolha_horario not in horarios:
            print("Horário inválido!")
            return
        
        horario_selecionado = horarios[escolha_horario]

        # Filtrar as salas que estão livres ("-") no horário escolhido
        salas_disponiveis = df[df[horario_selecionado] == "-"].index.tolist()

        if salas_disponiveis:
            print("\nSalas disponíveis nesse horário:")
            print(", ".join(map(str, salas_disponiveis)))
        else:
            print("\nNenhuma sala está disponível nesse horário.")

    except ValueError:
        print("Entrada inválida! Digite um número correspondente ao horário.")

def exibir_reservas_professor():
    limpar_tela()
    nome_professor = input("Digite o nome do professor: ").strip().lower()

    if not nome_professor:
        print("Nome inválido!")
        return

    encontrou_reservas = False

    print(f"\nReservas para o professor {nome_professor}:\n")

    for dia, df in tabelas.items():
        for sala in df.index:
            for horario, reserva in df.loc[sala].items():
                if isinstance(reserva, str) and reserva.lower().startswith(nome_professor):  # Converte para minúsculas antes da comparação
                    print(f"{dia} - Sala {sala} - {horario}: {reserva}")
                    encontrou_reservas = True
    if not encontrou_reservas:
        print(f"\nNenhuma reserva encontrada para {nome_professor}.")
