import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# 1. Segurança da Chave
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "⚠️ ERRO CRÍTICO: Variável de ambiente 'GEMINI_API_KEY' não encontrada."
    )


# 2. DATA PIVOT: Lendo o cérebro (dados externos) com caminho absoluto
def carregar_cerebro():
    try:
        # Pega a pasta onde este server.py está localizado
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "data.json")

        with open(file_path, "r", encoding="utf-8") as file:
            dados = json.load(file)

        instrucao = f"""
        {dados['regras_de_comportamento']}

        DADOS OFICIAIS DO KAUAN:
        - Nome: {dados['perfil']['nome']}
        - Cargo: {dados['perfil']['cargo']}
        - Status: {dados['perfil']['status']}

        HABILIDADES (STACK):
        - {', '.join(dados['habilidades_principais'])}

        PROJETOS DE DESTAQUE:
        """
        for projeto in dados["projetos"]:
            instrucao += f"- {projeto['nome']}: {projeto['descricao']}\n"

        return instrucao

    except Exception as e:
        print(f"⚠️ Erro ao carregar data.json: {e}")
        return "Você é o concierge do Kauan. Seja educado e profissional."


# 3. Configurando a IA
genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    model_name="gemini-3-flash-preview", system_instruction=carregar_cerebro()
)


# 4. Rotas
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "Mensagem vazia"}), 400

    try:
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        print(f"Erro no servidor: {e}")
        return jsonify({"error": "Falha ao processar a mensagem."}), 500


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "active", "message": "Concierge está operante"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
