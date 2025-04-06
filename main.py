import os #Biblioteca para funcionamento integrada do py

from organizer import organize_folder, TIPOS_DE_ARQUIVOS #Chama a função na organizer.py

def main():
    print('====Documents Organizer====')             #Apenas uma função inicial para o usuário
    caminho = input("Digite o caminho da pasta que deseja organizar: ").strip()

    if not os.path.exists(caminho):
        print('Caminho inválido, certifique-se de que a pasta existe')  #Se o caminho não funcionar cai nessa condição
        return

    organize_folder(caminho, TIPOS_DE_ARQUIVOS)   #Se o caminho estiver correto, vai cair nessa parte que irá rodar o programa e organizar os docs
    print('====Organização concluida com sucesso!====')

if __name__ == '__main__':
    main()
