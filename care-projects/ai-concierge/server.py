import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# 1. Segurança da Chave
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("⚠️ AVISO: Variável 'GEMINI_API_KEY' não encontrada.")

genai.configure(api_key=api_key)


# 2. Carregamento da Alma e Dados
def carregar_contexto():
    base = os.path.dirname(__file__)
    try:
        with open(
            os.path.join(base, "database", "concierge-soul.md"), "r", encoding="utf-8"
        ) as f:
            soul = f.read()
        with open(
            os.path.join(base, "database", "my-data.md"), "r", encoding="utf-8"
        ) as f:
            data = f.read()
        return f"{soul}\n\n=== DADOS DO KAUAN ===\n{data}"
    except Exception as e:
        print(f"⚠️ Erro ao carregar arquivos da database: {e}")
        return "Você é o concierge virtual do Kauan. Seja profissional e direto."


model = genai.GenerativeModel(
    model_name="gemini-2.5-flash", system_instruction=carregar_contexto()
)


# 3. Rotas
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    if not user_msg:
        return jsonify({"error": "Mensagem vazia"}), 400

    try:
        response = model.generate_content(user_msg)
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
