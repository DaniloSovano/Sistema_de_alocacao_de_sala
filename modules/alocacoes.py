from modules.data import horarios,tabelas, salvar_dados
from utils.utils import limpar_tela

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

