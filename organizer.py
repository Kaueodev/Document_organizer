import os
import shutil
from rich.console import Console
from rich.progress import track

console = Console()

TIPOS_DE_ARQUIVOS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".doc", ".odt"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "Apresentações": [".pptx", ".ppt"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],   
    "Áudios": [".mp3", ".wav", ".ogg"],
    "Compactados": [".zip", ".rar", ".7z", ".tar"],
    "Executáveis": [".exe", ".msi", ".bat", ".sh", ".apk"],
    "Outros": []
}

def obter_categoria(extensao): 
    for categoria, extensoes in TIPOS_DE_ARQUIVOS.items():  
        if extensao.lower().strip() in extensoes:   
            return categoria 
    return "Outros..."       

def organize_folder(caminho, tipos_dict): 
    for item in track(os.listdir(caminho), description="[bold yellow]Organizando documentos...[/bold yellow]"):
        item_path = os.path.join(caminho, item) 
        arquivos = os.listdir(caminho)

        if os.path.isfile(item_path):
            _, extensao = os.path.splitext(item)
            categoria = obter_categoria(extensao) 
            pasta_destino = os.path.join(caminho, categoria) 

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)  
            novo_caminho = os.path.join(pasta_destino, item) 

            shutil.move(item_path, novo_caminho) 
    return "Arquivos organizados com sucesso!"

            


