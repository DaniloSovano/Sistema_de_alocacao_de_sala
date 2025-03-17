import os
import pandas as pd

ARQUIVO_XLSX = "salas_reservadas.xlsx"

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
    print(f"Dados salvos em {ARQUIVO_XLSX}")

tabelas = carregar_dados()