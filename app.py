from flask import Flask, render_template, request, jsonify
import organizer
import webbrowser
import threading

# Cria a instância da aplicação Flask.
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route("/organizar", methods=["POST"])
def organizar():
    data = request.get_json()
    caminho = data.get("caminho")

    tipos_dict = {
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

    if caminho:
        try:
            resultado = organizer.organize_folder(caminho, tipos_dict)
            return jsonify({'mensagem': resultado})
        except Exception as e:
            return jsonify({'erro': f'Erro ao organizar: {str(e)}'}), 500
    return jsonify({'erro': 'Caminho não fornecido'}), 400

def abrir_navegador():
    webbrowser.open_new("http://127.0.0.1:5000/")
    
# Inicia a aplicação flask se eu rodar o arquivo diretamente
if __name__=="__main__":
    threading.Timer(1, abrir_navegador).start()
    app.run(debug=True, use_reloader=False)
