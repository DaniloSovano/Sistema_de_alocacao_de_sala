import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# Definição das salas e horários
salas = list(range(401, 417))
horarios = {
    1: "7:30 - 8:20", 2: "8:20 - 09:10", 3: "09:20 - 10:10", 
    4: "10:10 - 11:00", 5: "11:10 - 12:00", 6: "12:00 - 12:50"
}

horarios_dataframe = list(horarios.values())
df = pd.DataFrame("🔘", index=salas, columns=horarios_dataframe)
df.index.name = "Salas"

# Função para listar salas livres
def listar_salas_livres(horario):
    return df[df[horario] == "🔘"].index.tolist()

# Função para alocar sala
def alocar():
    horario = combo_horario.get()
    if not horario:
        messagebox.showerror("Erro", "Selecione um horário!")
        return
    
    salas_livres = listar_salas_livres(horario)
    if not salas_livres:
        messagebox.showwarning("Aviso", "Nenhuma sala disponível neste horário!")
        return
    
    sala = int(entry_sala.get())
    if sala not in salas_livres:
        messagebox.showerror("Erro", "Sala inválida ou já ocupada!")
        return
    
    nome = entry_professor.get()
    disciplina = entry_disciplina.get()
    if not nome or not disciplina:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return
    
    df.at[sala, horario] = f"{nome} ({disciplina})"
    atualizar_tabela()
    messagebox.showinfo("Sucesso", f"Sala {sala} alocada para {nome} ({disciplina})!")

# Função para atualizar a tabela
def atualizar_tabela():
    for row in tree.get_children():
        tree.delete(row)
    
    for sala in salas:
        valores = [sala] + list(df.loc[sala])
        tree.insert("", "end", values=valores)

# Interface Gráfica
top = tk.Tk()
top.title("Sistema de Alocação de Salas")
top.geometry("800x400")

tk.Label(top, text="Professor:").grid(row=0, column=0)
entry_professor = tk.Entry(top)
entry_professor.grid(row=0, column=1)

tk.Label(top, text="Disciplina:").grid(row=1, column=0)
entry_disciplina = tk.Entry(top)
entry_disciplina.grid(row=1, column=1)

tk.Label(top, text="Sala:").grid(row=2, column=0)
entry_sala = tk.Entry(top)
entry_sala.grid(row=2, column=1)

tk.Label(top, text="Horário:").grid(row=3, column=0)
combo_horario = ttk.Combobox(top, values=horarios_dataframe)
combo_horario.grid(row=3, column=1)

btn_alocar = tk.Button(top, text="Alocar", command=alocar)
btn_alocar.grid(row=4, column=0, columnspan=2)

# Tabela
columns = ["Sala"] + horarios_dataframe
tree = ttk.Treeview(top, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.grid(row=5, column=0, columnspan=3)
atualizar_tabela()

top.mainloop()
