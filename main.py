from modules.alocacoes import alocar, alterar_locacao
from modules.consultas import consultar_salas_disponiveis, exibir_horarios, exibir_reservas_professor
from modules.data import ARQUIVO_XLSX, salvar_dados
from utils.utils import escolher_dia



def menu():
    executando = True
    while executando:
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
            dia = escolher_dia()
            if dia:
                consultar_salas_disponiveis(dia)

        elif opcao == "5":
            exibir_reservas_professor()

        elif opcao == "6":
            salvar_dados()
            print(f"Reservas exportadas para '{ARQUIVO_XLSX}'.")

        elif opcao == "7":
            print("Saindo do sistema...")
            executando = False

        else:
            print("Opção inválida! Escolha novamente.")

if __name__ == "__main__":
    menu()
