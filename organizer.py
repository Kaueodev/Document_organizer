import os
import shutil

TIPOS_DE_ARQUIVOS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".doc", ".odt"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "Apresentações": [".pptx", ".ppt"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],   #Dicionário com os tipos de categoria e suas extensoes 
    "Áudios": [".mp3", ".wav", ".ogg"],
    "Compactados": [".zip", ".rar", ".7z", ".tar"],
    "Executáveis": [".exe", ".msi", ".bat", ".sh", ".apk"],
    "Outros": []  # qualquer coisa que não caia nos de cima
}

def obter_categoria(extensao):
    for categoria, extensoes in TIPOS_DE_ARQUIVOS.items():  #Usa lista para iterar entre as extensoes e selecionar a categoria baseado na extensao
        if extensao.lower().strip() in extensoes:   
            return categoria 
    return "outros..."       

def organize_folder(caminho, tipos_dict): #Função que irá receber o caminho da pasta
    for item in os.listdir(caminho): #Percorre todos os itens da pasta indicada
        item_path = os.path.join(caminho, item) #Cria o caminho do item atual

    if os.path.isfile(item_path): #Filtra o que é arquivo(file) ignorando pastas
        _, extensao = os.path.splitext(item) #Separa a extensao do nome do arquivo
        categoria = obter_categoria(extensao) #Descobre o tipo do arquivo imagens, videos, documentos, etc...
        pasta_destino = os.path.join(caminho, categoria) #Irá mover o arquivo para sua determinada pasta

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)   #Essa condição vai criar a pasta caso ela ainda não exista

    novo_caminho = os.path.join(pasta_destino, item) #Cria o novo caminho completo onde o arquivo vai ficar após ser movido

    shutil.move(item_path, novo_caminho) #Move o arquivo para a pasta correta


