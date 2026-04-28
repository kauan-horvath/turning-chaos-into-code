import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# 1. Credenciais
api_key = os.environ.get("GEMINI_API_KEY")
email_user = os.environ.get("EMAIL_USER")
email_pass = os.environ.get("EMAIL_PASS")

if not api_key:
    print("⚠️ AVISO: Variável 'GEMINI_API_KEY' não encontrada.")

genai.configure(api_key=api_key)

# Caminho absoluto para o arquivo de Logs
LOG_FILE = os.path.join(os.path.dirname(__file__), "database", "logs_interacoes.json")
active_chats = {}  # Mantém o contexto da conversa atual na memória


# 2. Carregamento da Alma
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
        print(f"⚠️ Erro ao carregar arquivos: {e}")
        return "Você é o concierge virtual do Kauan. Seja profissional e direto."


model = genai.GenerativeModel(
    model_name="gemini-2.5-flash", system_instruction=carregar_contexto()
)


# --- FUNÇÃO DE ARQUIVAMENTO PERSISTENTE ---
def salvar_no_arquivo(email, dados_usuario, pergunta, resposta):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    registro = {
        "hora": agora,
        "email": email,
        "nome": dados_usuario.get("nome", "Desconhecido"),
        "tipo": dados_usuario.get("tipo", "N/A"),
        "detalhe": dados_usuario.get("detalhe", "N/A"),
        "pergunta": pergunta,
        "resposta": resposta,
    }

    logs = []
    # Lê o que já existe no arquivo
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Aviso: não foi possível carregar o arquivo de logs: {e}")
            logs = []

    # Adiciona a nova interação e salva
    logs.append(registro)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4, ensure_ascii=False)


# 3. Rota de Chat
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "")
    session_data = data.get("user_data", {})

    if not user_msg:
        return jsonify({"error": "Mensagem vazia"}), 400

    user_id = session_data.get("email", "visitante_anonimo")

    try:
        if user_msg == "START_CONVERSATION" or user_id not in active_chats:
            active_chats[user_id] = model.start_chat(history=[])
            full_prompt = (
                f"[SISTEMA: O usuário {session_data.get('nome')} acabou de entrar no chat. "
                f"Ele é um {session_data.get('tipo')} da empresa/relação {session_data.get('detalhe')}. "
                f"Dê as boas-vindas curtas e ofereça as opções com PIVO:]"
            )
            pergunta_log = "INÍCIO DA SESSÃO"
        else:
            full_prompt = user_msg
            pergunta_log = user_msg

        chat_session = active_chats[user_id]
        response = chat_session.send_message(full_prompt)
        resposta_texto = response.text

        # 💾 ARQUIVA NO ARQUIVO JSON IMEDIATAMENTE
        salvar_no_arquivo(user_id, session_data, pergunta_log, resposta_texto)

        return jsonify({"reply": resposta_texto})

    except Exception as e:
        print(f"Erro no servidor: {e}")
        return jsonify({"error": "Falha ao processar a mensagem."}), 500


# 4. Rota para Ler o Arquivo e Disparar o E-mail
@app.route("/gerar_relatorio", methods=["GET"])
def gerar_relatorio():
    if not email_user or not email_pass:
        return jsonify({"error": "Credenciais de e-mail não configuradas."}), 500

    if not os.path.exists(LOG_FILE):
        return (
            jsonify(
                {
                    "message": "Nenhum arquivo de log encontrado. Nenhuma interação ainda."
                }
            ),
            200,
        )

    # Lê as interações arquivadas
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs_arquivados = json.load(f)

    if not logs_arquivados:
        return jsonify({"message": "Arquivo de log está vazio."}), 200

    # Montando o corpo do e-mail
    corpo_email = "<h2>Relatório de Interações - Concierge IA</h2><hr>"

    for interacao in logs_arquivados:
        corpo_email += "<div style='background:#f9f9f9; padding:10px; border-left: 4px solid #3b82f6; margin-bottom: 15px;'>"
        corpo_email += f"<p><b>👤 {interacao['nome']}</b> ({interacao['tipo']} - {interacao['detalhe']}) | 📧 {interacao['email']}</p>"
        corpo_email += f"<p><small>⏰ {interacao['hora']}</small></p>"
        corpo_email += f"<p><b>🗣️ Pergunta:</b> {interacao['pergunta']}</p>"
        corpo_email += f"<p><b>🤖 Resposta:</b> {interacao['resposta']}</p>"
        corpo_email += "</div>"

    try:
        msg = MIMEMultipart()
        msg["From"] = email_user
        msg["To"] = email_user
        msg["Subject"] = (
            f"Relatório do Concierge - {datetime.now().strftime('%d/%m/%Y')}"
        )
        msg.attach(MIMEText(corpo_email, "html"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_user, email_pass)
        server.send_message(msg)
        server.quit()

        # Esvazia o arquivo após enviar o email com sucesso
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

        return (
            jsonify(
                {
                    "success": f"Relatório com {len(logs_arquivados)} interações enviado com sucesso!"
                }
            ),
            200,
        )

    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return jsonify({"error": f"Falha ao enviar o e-mail: {e}"}), 500


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "active"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
