# Sistema de Gerenciamento de Salas

Este é um sistema simples para alocação e gerenciamento de salas em uma instituição de ensino. O programa permite alocar salas para professores, consultar horários disponíveis e exportar os dados em um arquivo Excel.

## 🚀 Funcionalidades
- Ver todas as salas e seus horários.
- Alocar salas para professores.
- Alterar ou remover alocações.
- Consultar salas disponíveis para um horário específico.
- Exibir reservas de um professor específico.
- Exportar as reservas para um arquivo XLSX.

## 🛠️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter o Python instalado e as seguintes bibliotecas:

```sh
pip install pandas openpyxl rich
```

## 📖 Como Usar

Após executar o programa, você verá um menu com as seguintes opções:

1️⃣ **Ver todas as salas** → Exibe a alocação de todas as salas. <br>
2️⃣ **Alocar Sala** → Permite reservar uma sala para um professor.<br>
3️⃣ **Alterar ou Remover locação** → Modifica ou exclui uma reserva existente.<br>
4️⃣ **Consultar salas disponíveis** → Mostra quais salas estão livres em determinado horário.<br>
5️⃣ **Exibir reservas de um professor** → Lista todas as reservas de um professor específico.<br>
6️⃣ **Exportar reservas para XLSX** → Salva todas as reservas no arquivo `salas_reservadas.xlsx`.<br>
7️⃣ **Sair** → Encerra o sistema.<br>

## 📂 Formato do Arquivo de Dados

As reservas são armazenadas em `salas_reservadas.xlsx`, onde cada dia da semana possui sua própria aba com as alocações de horários.

## 📝 Exemplo de Uso

### **Alocar uma sala**

1. Escolha a opção `2 - Alocar Sala`.
2. Selecione um dia da semana.
3. Escolha um ou mais horários.
4. Escolha uma sala disponível.
5. Insira o nome do professor e a disciplina.

### **Consultar salas disponíveis**

1. Escolha a opção `4 - Consultar salas disponíveis`.
2. Selecione um dia da semana.
3. Escolha um horário.
4. O sistema exibirá as salas disponíveis para aquele horário.

## 📌 Notas
- Caso o arquivo `salas_reservadas.xlsx` não exista, ele será criado automaticamente.
- O sistema funciona apenas em dias úteis (segunda a sexta-feira).
