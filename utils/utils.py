import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear") 

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