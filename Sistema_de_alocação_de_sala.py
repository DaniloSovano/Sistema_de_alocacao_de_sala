import pandas as pd
from tabulate import tabulate  

salas = list(range(401, 417))
horarios_dataframe = ["7:30 - 8:20", "8:20 - 09:10", "09:20 - 10:10", "10:10 - 11:00", 
                      "11:10 - 12:00", "12:00 - 12:50"]

df = pd.DataFrame("-", index=salas, columns=horarios_dataframe) 
df.index.name = "Salas"

def listar_salas_livres(horario):
    """Lista as salas disponíveis para um determinado horário."""
    if horario not in df.columns:
        print("❌ Horário inválido!")
        return []
    
    salas_livres = df[df[horario] == "-"].index.tolist()
    
    if salas_livres:
        print(f"🟢 Salas disponíveis para o horário {horario}: {salas_livres}")
    else:
        print(f"⚠️ Nenhuma sala disponível para o horário {horario}.")
    
    return salas_livres

def alocar(horario):
    """Aloca uma sala no horário escolhido."""
    salas_livres = listar_salas_livres(horario)

    if not salas_livres:
        print("⚠️ Escolha outro horário!")
        return

    try:
        sala = int(input("Digite o número da sala para alocar: "))
        
        if sala not in salas_livres:
            print("❌ Sala inválida ou já ocupada!")
            return
        
        nome = input("Digite o nome do professor: ")
        disciplina = input("Digite a disciplina a ser ministrada: ")

        df.at[sala, horario] = f"{nome} ({disciplina})"
        print(f"✅ Sala {sala} alocada no horário {horario} para {nome} ({disciplina})!")
    
    except ValueError:
        print("❌ Entrada inválida! Digite um número válido.")

horarios = {
    1: "7:30 - 8:20", 2: "8:20 - 09:10", 3: "09:20 - 10:10", 
    4: "10:10 - 11:00", 5: "11:10 - 12:00", 6: "12:00 - 12:50"
}

print("Escolha um horário:")
for key, value in horarios.items():
    print(f"{key} - {value}")

try:
    escolha_horario = int(input("Digite o número do horário desejado: "))

    if escolha_horario in horarios:
        alocar(horarios[escolha_horario])
    else:
        print("❌ Opção inválida!")
except ValueError:
    print("❌ Entrada inválida! Digite um número válido.")

# Exibir tabela formatada com tabulate, garantindo alinhamento
print("\n📌 **Tabela de Alocação de Salas:**")
print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex="always"))
