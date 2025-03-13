import os
import pandas as pd
from tabulate import tabulate  

ARQUIVO_XLSX = "salas_reservadas.xlsx"

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear") 

horarios = {
    1: "7:30 - 8:20", 2: "8:20 - 09:10", 3: "09:20 - 10:10", 
    4: "10:10 - 11:00", 5: "11:10 - 12:00", 6: "12:00 - 12:50"
}
salas = list(range(401, 417))
dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

def carregar_dados():
    if os.path.exists(ARQUIVO_XLSX):
        return pd.read_excel(ARQUIVO_XLSX, sheet_name=None, index_col=0, engine="openpyxl")
    else:
        return {dia: pd.DataFrame("-", index=salas, columns=horarios.values()) for dia in dias_da_semana}

def salvar_dados():
    with pd.ExcelWriter(ARQUIVO_XLSX, engine="openpyxl") as writer:
        for dia, df in tabelas.items():
            df.to_excel(writer, sheet_name=dia)
    print(f"📁 Dados salvos em {ARQUIVO_XLSX}")

tabelas = carregar_dados()

def alocar(dia):
    limpar_tela()
    print(f"\nAlocação de sala para {dia}\n")

    df = tabelas[dia]

    print("\nHorários disponíveis:")
    for key, value in horarios.items():
        print(f"{key} - {value}")

    try:
        escolha_horarios = input("\nDigite os números dos horários desejados (separados por espaço): ").strip()
        
        if not escolha_horarios:
            print("Nenhum horário foi inserido!")
            return
        
        escolha_horarios = [int(h) for h in escolha_horarios.split() if h.isdigit() and int(h) in horarios]

        if not escolha_horarios:
            print("Nenhum horário válido foi selecionado!")
            return

        horarios_selecionados = [horarios[h] for h in escolha_horarios]

        filtro = (df[horarios_selecionados] == "-").all(axis=1)
        salas_livres = df[filtro].index.tolist()

        if not salas_livres:
            print("Nenhuma sala está disponível para todos os horários selecionados.")
            return

        print("\nSalas disponíveis para os horários escolhidos:")
        print(", ".join(map(str, salas_livres)))

        sala = input("\nDigite o número da sala para alocar: ").strip()

        if not sala.isdigit() or int(sala) not in salas_livres:
            print("Sala inválida ou já ocupada em algum horário!")
            return
        
        sala = int(sala)

        nome = input("Digite o nome do professor: ").strip()
        disciplina = input("Digite a disciplina: ").strip()

        if not nome or not disciplina:
            print("Nome e disciplina são obrigatórios!")
            return

        for horario in horarios_selecionados:
            df.at[sala, horario] = f"{nome} ({disciplina})"

        salvar_dados()  

        print(f"\n✅ Sala {sala} alocada para {nome} ({disciplina}) nos horários:")
        for horario in horarios_selecionados:
            print(f"  - {horario}")

    except ValueError:
        print("Entrada inválida! Digite números separados por espaço.")
    
def alterar_locacao(dia):
    limpar_tela()
    print(f"\nAlterar locação de sala para {dia}")

    df = tabelas[dia]

    print("\nHorários disponíveis:")
    for key, value in horarios.items():
        print(f"{key} - {value}")

    try:
        escolha_horarios = input("\nDigite os números dos horários desejados (separados por espaço): ").strip()

        if not escolha_horarios:
            print("Nenhum horário foi inserido!")
            return

        escolha_horarios = [int(h) for h in escolha_horarios.split() if h.isdigit() and int(h) in horarios]

        if not escolha_horarios:
            print("Nenhum horário válido foi selecionado!")
            return

        horarios_selecionados = [horarios[h] for h in escolha_horarios]

        filtro = (df[horarios_selecionados] != "-").any(axis=1)
        salas_ocupadas = df[filtro].index.tolist()

        if not salas_ocupadas:
            print("\nNenhuma sala está ocupada nos horários selecionados.")
            return

        print("\nSalas ocupadas nos horários escolhidos:")
        print(", ".join(map(str, salas_ocupadas)))

        sala = input("\nDigite o número da sala para modificar a alocação: ").strip()

        if not sala.isdigit() or int(sala) not in salas_ocupadas:
            print("Sala inválida ou sem reservas nesses horários!")
            return
        
        sala = int(sala)

        print(f"\nReservas atuais da sala {sala}:")
        for horario in horarios_selecionados:
            if df.at[sala, horario] != "-":
                print(f"  {horario}: {df.at[sala, horario]}")

        opcao = input("\nDeseja remover (R) ou modificar (M) a reserva? ").strip().lower()
        
        if opcao == "r":
            for horario in horarios_selecionados:
                df.at[sala, horario] = "-"
            print(f"\nReservas removidas da sala {sala}.")
        
        elif opcao == "m":
            nome = input("Digite o novo nome do professor: ").strip()
            disciplina = input("Digite a nova disciplina: ").strip()

            if not nome or not disciplina:
                print("Nome e disciplina são obrigatórios!")
                return

            for horario in horarios_selecionados:
                df.at[sala, horario] = f"{nome} ({disciplina})"

            print(f"\nSala {sala} agora está alocada para {nome} ({disciplina}) nos horários:")
            for horario in horarios_selecionados:
                print(f"  {horario}")
        else:
            print("Opção inválida!")
            return
        
        salvar_dados()  

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
        3 - Alterar ou Remover locação
        4 - Consultar salas disponíveis em um horário específico
        5 - Exibir reservas de um professor
        6 - Exportar reservas para XLSX
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
            dia = escolher_dia()
            alterar_locacao(dia)
            
        elif opcao == "4":
            print("Função ainda não implementada.")

        elif opcao == "5":
            print("Função ainda não implementada.")

        elif opcao == "6":
            salvar_dados()
            print(f"Reservas exportadas para '{ARQUIVO_XLSX}'.")

        elif opcao == "7":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Escolha novamente.")

menu()
