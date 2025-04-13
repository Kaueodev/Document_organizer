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

#Categoria -> nome da pasta onde vai conter a extensão. Usa lista para iterar entre as extensoes e selecionar a categoria baseado na extensao
def obter_categoria(extensao): 
    for categoria, extensoes in TIPOS_DE_ARQUIVOS.items():  
        if extensao.lower().strip() in extensoes:   
            return categoria 
    return "Outros..."       

#Função que irá receber o caminho da pasta
def organize_folder(caminho, tipos_dict): 
    for item in track(os.listdir(caminho), description="[bold yellow]Organizando documentos...[/bold yellow]"):
        item_path = os.path.join(caminho, item) 
        arquivos = os.listdir(caminho)

#Organiza os itens no caminhio fornecido, filtrando, separando, descobrindo e movendo
        if os.path.isfile(item_path):
            _, extensao = os.path.splitext(item)
            categoria = obter_categoria(extensao) 
            pasta_destino = os.path.join(caminho, categoria) 

 #Essa condição vai criar a pasta caso ela ainda não exista
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)  

#Cria o novo caminho completo onde o arquivo vai ficar após ser movido
        novo_caminho = os.path.join(pasta_destino, item) 

#Move o arquivo para a pasta correta
        shutil.move(item_path, novo_caminho) 


