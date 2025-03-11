import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

salas = list(range(401, 417))
horarios = {
    1: "7:30 - 8:20", 2: "8:20 - 09:10", 3: "09:20 - 10:10", 
    4: "10:10 - 11:00", 5: "11:10 - 12:00", 6: "12:00 - 12:50"
}

horarios_dataframe = list(horarios.values())
df = pd.DataFrame("🔘", index=salas, columns=horarios_dataframe)
df.index.name = "Salas"

def listar_salas_livres(horario):
    return df[df[horario] == "🔘"].index.tolist()

def alocar():
    horario = combo_horario.get()
    if not horario:
        messagebox.showerror("Erro", "Selecione um horário!")
        return
    
    salas_livres = listar_salas_livres(horario)
    if not salas_livres:
        messagebox.showwarning("Aviso", "Nenhuma sala disponível neste horário!")
        return
    
    try:
        sala = int(entry_sala.get())
        if sala not in salas_livres:
            messagebox.showerror("Erro", "Sala inválida ou já ocupada!")
            return
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para a sala!")
        return
    
    nome = entry_professor.get()
    disciplina = entry_disciplina.get()
    if not nome or not disciplina:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return
    
    df.at[sala, horario] = f"{nome} ({disciplina})"
    atualizar_tabela()
    messagebox.showinfo("Sucesso", f"Sala {sala} alocada para {nome} ({disciplina})!")

def atualizar_tabela():
    for row in tree.get_children():
        tree.delete(row)
    
    for sala in salas:
        valores = [sala] + list(df.loc[sala])
        tree.insert("", "end", values=valores)

top = tk.Tk()
top.title("Sistema de Alocação de Salas")
top.geometry("1600x900")

tk.Label(top, text="Professor:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=5)
entry_professor = tk.Entry(top, font=("Arial", 14), width=20)
entry_professor.grid(row=0, column=1, padx=10, pady=5)

tk.Label(top, text="Disciplina:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=5)
entry_disciplina = tk.Entry(top, font=("Arial", 14), width=20)
entry_disciplina.grid(row=1, column=1, padx=10, pady=5)

tk.Label(top, text="Sala:", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=5)
entry_sala = tk.Entry(top, font=("Arial", 14), width=10)
entry_sala.grid(row=2, column=1, padx=10, pady=5)

tk.Label(top, text="Horário:", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=5)
combo_horario = ttk.Combobox(top, values=horarios_dataframe, font=("Arial", 14), width=18)
combo_horario.grid(row=3, column=1, padx=10, pady=5)

btn_alocar = tk.Button(top, text="Alocar", font=("Arial", 14, "bold"), command=alocar)
btn_alocar.grid(row=4, column=0, columnspan=2, pady=10)

columns = ["Sala"] + horarios_dataframe
tree = ttk.Treeview(top, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
atualizar_tabela()

top.mainloop()