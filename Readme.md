# 📂 Document Organizer

Organizador de documentos feito com **Python + Flask + HTML + CSS + JavaScript**.  
Esse projeto organiza automaticamente arquivos de uma pasta, movendo-os para subpastas conforme suas extensões.

> Projeto Full Stack básico, ideal para treinar integração entre frontend e backend.

---

## 🚀 Tecnologias utilizadas

- 🐍 Python 3
- 🔥 Flask
- 🌐 HTML5 + CSS3 + JavaScript
- 🎨 Rich (para logs bonitos no terminal)
- 🧠 VSCode + Live Server
- 📦 Flask-CORS (para integração segura)

---

## 🧩 Funcionalidades

- Organiza arquivos automaticamente com base nas extensões
- Cria subpastas como "Imagens", "Documentos", "Planilhas", etc.
- Interface web para digitar o caminho da pasta
- Integração com backend Python via `fetch()`
- Feedback visual no navegador e no terminal

---

## 💻 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/document-organizer.git
cd document-organizer
```
### 2. Crie um ambiente virtual e ative

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependêcias

```bash
pip install flask flask-cors rich
```

### 4. Rode o backend e o front abrirá automaticamente

```bash
cd backend
python app.py
```

---
# 📂 Exemplo de organização

Antes de rodar:

```bash
/Downloads
├── foto.jpg
├── documento.pdf
├── planilha.xlsx
```

Depois de rodar:

```bash
/Downloads
├── Imagens/
│   └── foto.jpg
├── Documentos/
│   └── documento.pdf
├── Planilhas/
│   └── planilha.xlsx
```
 
 ---
**Feito por Kaue Guimarães**

**Estudante de Análise e Desenvolvimento de Sistemas**

**Conecte-se comigo pelo [Linkedin](https://www.linkedin.com/in/kaueguimaraesodev/)**
