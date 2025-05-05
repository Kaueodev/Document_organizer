function organizar() {
    const caminho = document.getElementById("caminho").value;
    const mensagem = document.getElementById("mensagem");
  
    if (caminho.trim() === "") {
      mensagem.innerText = "Digite um caminho válido!";
      mensagem.style.color = "red";
      return;
    }
  
    mensagem.innerText = "Organizando arquivos...";
    mensagem.style.color = "blue";

    fetch("http://127.0.0.1:5000/organizar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ caminho: caminho }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.mensagem) {
          mensagem.innerText = "✅ " + data.mensagem;
          mensagem.style.color = "green";
        } else if (data.erro) {
          mensagem.innerText = "❌ " + data.erro;
          mensagem.style.color = "red";
        }
      })
      .catch(error => {
        console.error("Erro:", error);
        document.getElementById("mensagem").innerText = "Erro ao organizar os arquivos.";
    });
  }