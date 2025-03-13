import os
import pandas as pd
from tabulate import tabulate  

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear") 


horarios = {
    1: "7:30 - 8:20", 2: "8:20 - 09:10", 3: "09:20 - 10:10", 
    4: "10:10 - 11:00", 5: "11:10 - 12:00", 6: "12:00 - 12:50"
}
salas = list(range(401, 417))

dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
tabelas = {dia: pd.DataFrame("-", index=salas, columns=horarios.values()) for dia in dias_da_semana}

for df in tabelas.values():
    df.index.name = "Salas"

def listar_salas_livres(dia, horario):
    df = tabelas[dia] 
    
    if horario not in df.columns:
        print("Horário inválido!")
        return []
    
    salas_livres = df[df[horario] == "-"].index.tolist()
    
    if salas_livres:
        print(f"Salas disponíveis para o horário {horario}: {', '.join(map(str, salas_livres))}")
    else:
        print(f"Nenhuma sala disponível para o horário {horario}.")
    
    return salas_livres

def alocar(dia):
    limpar_tela()
    print(f"\nAlocação de sala para {dia}\n")

    df = tabelas[dia]

    print("\nHorários disponíveis:")
    for key, value in horarios.items():
        print(f"{key} - {value}")

    try:
        escolha_horarios = input("\nDigite os números dos horários desejados (separados por espaço): ")
        escolha_horarios = [int(h) for h in escolha_horarios.split() if int(h) in horarios]

        if not escolha_horarios:
            print("Nenhum horário válido foi selecionado!")
            return

        horarios_selecionados = [horarios[h] for h in escolha_horarios]

        filtro = (df[horarios_selecionados] == "-").all(axis=1)
        salas_livres = df.query(filtro).index.tolist()

        if not salas_livres:
            print("Nenhuma sala está disponível para todos os horários selecionados.")
            return

        print(f"\nSalas disponíveis para os horários escolhidos: {', '.join(map(str, salas_livres))}")

        sala = int(input("\nDigite o número da sala para alocar: "))
        if sala not in salas_livres:
            print("Sala inválida ou já ocupada em algum horário!")
            return

        nome = input("Digite o nome do professor: ").strip()
        disciplina = input("Digite a disciplina: ").strip()

        if not nome or not disciplina:
            print("Nome e disciplina são obrigatórios!")
            return

        for horario in horarios_selecionados:
            df.at[sala, horario] = f"{nome} ({disciplina})"

        print(f"\nSala {sala} alocada para {nome} ({disciplina}) nos horários:")
        for horario in horarios_selecionados:
            print(f"  {horario}")

    except ValueError:
        print("Entrada inválida! Digite números separados por espaço.")


def exibir_horarios(dia):
    df = tabelas[dia]
    print(f"\nTabela de Alocação de Salas do dia {dia}:")
    print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex="always"))

def escolher_dia():
    dias = {1: "Segunda", 2: "Terça", 3: "Quarta", 4: "Quinta", 5: "Sexta"}
    
    for key, value in dias.items():
        print(f"{key} - {value}")
    
    try:
        dia = int(input("Qual dia da semana deseja? "))
        return dias[dia]
    except (ValueError, KeyError):
        print("Entrada inválida! Digite um número válido.")
        return None

def menu():
    while True:
        print("""
        Sistema de Gerenciamento de Salas
        1 - Ver todas as salas
        2 - Alocar Sala
        3 - Alterar locação
        4 - Consultar salas disponíveis em um horário específico
        5 - Exibir reservas de um professor
        6 - Exportar reservas para CSV
        7 - Sair
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            dia = escolher_dia()
            if dia:
                exibir_horarios(dia)

        elif opcao == "2":
            dia = escolher_dia()
            if dia:
                alocar(dia)

        elif opcao == "3":
            print("Função ainda não implementada.")

        elif opcao == "4":
            print("Função ainda não implementada.")

        elif opcao == "5":
            print("Função ainda não implementada.")

        elif opcao == "6":
            print("Função ainda não implementada.")

        elif opcao == "7":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Escolha novamente.")

menu()
