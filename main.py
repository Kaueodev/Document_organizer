import os 
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from organizer import organize_folder, TIPOS_DE_ARQUIVOS 

console = Console()

def main():
    print('[bold cyan]Document Organizer[/bold cyan]')             
    caminho = input("Digite o caminho da pasta que deseja organizar: ").strip()

    if not os.path.exists(caminho):
        print('[bold red]❌ Caminho inválido, certifique-se de que a pasta existe[/bold red]')  
        return

    organize_folder(caminho, TIPOS_DE_ARQUIVOS)  
    print('[bold green]✅ Organização concluida com sucesso![bold green]')

if __name__ == '__main__':
    main()
