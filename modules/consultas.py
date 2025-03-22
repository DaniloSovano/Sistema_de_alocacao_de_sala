from rich.console import Console
from rich.table import Table
from modules.data import tabelas, horarios
from utils.utils import limpar_tela

console = Console()

def exibir_horarios(dia):
    df = tabelas[dia]
    
    table = Table(title=f"Tabela de Alocação de Salas do dia {dia}", show_lines=True)
    table.add_column("Sala", justify="center", style="cyan")
    
    for horario in df.columns:
        table.add_column(horario, justify="center", style="magenta")
    
    for sala, row in df.iterrows():
        table.add_row(str(sala), *[str(row[col]) for col in df.columns])
    
    console.print(table)

def consultar_salas_disponiveis(dia):
    limpar_tela()
    console.print(f"\n[bold yellow]Consulta de salas disponíveis para {dia}[/bold yellow]\n")
    
    df = tabelas[dia]
    
    console.print("\n[bold green]Horários disponíveis:[/bold green]")
    for key, value in horarios.items():
        console.print(f"[cyan]{key}[/cyan] - {value}")
    
    try:
        escolha_horario = int(input("\nDigite o número do horário desejado: "))
        
        if escolha_horario not in horarios:
            console.print("[red]Horário inválido![/red]")
            return
        
        horario_selecionado = horarios[escolha_horario]
        salas_disponiveis = df[df[horario_selecionado] == "-"].index.tolist()
        
        if salas_disponiveis:
            console.print("\n[bold green]Salas disponíveis nesse horário:[/bold green]")
            console.print(", ".join(map(str, salas_disponiveis)))
        else:
            console.print("\n[bold red]Nenhuma sala está disponível nesse horário.[/bold red]")
    
    except ValueError:
        console.print("[red]Entrada inválida! Digite um número correspondente ao horário.[/red]")

def exibir_reservas_professor():
    limpar_tela()
    nome_professor = input("Digite o nome do professor: ").strip().lower()
    
    if not nome_professor:
        console.print("[red]Nome inválido![/red]")
        return
    
    encontrou_reservas = False
    console.print(f"\n[bold yellow]Reservas para o professor {nome_professor}:[/bold yellow]\n")
    
    for dia, df in tabelas.items():
        for sala in df.index:
            for horario, reserva in df.loc[sala].items():
                if isinstance(reserva, str) and reserva.lower().startswith(nome_professor):
                    console.print(f"[cyan]{dia}[/cyan] - Sala [bold]{sala}[/bold] - [magenta]{horario}[/magenta]: {reserva}")
                    encontrou_reservas = True
    
    if not encontrou_reservas:
        console.print(f"\n[red]Nenhuma reserva encontrada para {nome_professor}.[/red]")
