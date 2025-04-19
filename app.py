from flask import Flask, request, jsonify
from flask_cors import CORS
from organizer import organize_folder, TIPOS_DE_ARQUIVOS
import os

# Cria a instância da aplicação Flask.
app = Flask(__name__)
CORS(app)

@app.route("/organizar", methods=["POST"])
def organizar():
    data = request.get_json()
    caminho = data.get("caminho")

# Verificação do caminho
    if not caminho or not os.path.exists(caminho):
        return jsonify({"erro": "Caminho inválido ou não encontrado"}), 400
    
    try:
        organize_folder(caminho, TIPOS_DE_ARQUIVOS)
        return jsonify({"mensagem": "Organização concluida com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
# Inicia a aplicação flask se eu rodar o arquivo diretamente
if __name__=="__main__":
    app.run(debug=True)
