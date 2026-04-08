import os
import re
import yaml
import json
from datetime import date, datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# ================= CONFIGURAÇÕES =================
DIRETORIOS_PARA_BUSCA = ['knowledge-run', 'care-projects']
REGEX_REVIEW = r"\[REVIEW-DATE:\s*(\d{4}-\d{2}-\d{2})\]\s*(.*)"
CALENDAR_ID = 'kauanhorvath1996@gmail.com' 
# =================================================

def buscar_revisoes_futuras():
    revisoes = []
    hoje = date.today()

    # 1. Busca nos Arquivos (Markdown, Python, etc)
    for diretorio in DIRETORIOS_PARA_BUSCA:
        if not os.path.exists(diretorio): continue
        for root, dirs, files in os.walk(diretorio):
            for file in files:
                if file.endswith(('.py', '.md', '.sql', '.vba')):
                    path = os.path.join(root, file)
                    nome_arquivo = os.path.basename(path) # <--- Ajuste: Apenas o nome
                    try:
                        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                            for line in f:
                                m = re.search(REGEX_REVIEW, line)
                                if m:
                                    data_rev = datetime.strptime(m.group(1), '%Y-%m-%d').date()
                                    # Ajuste: Apenas datas estritamente após hoje
                                    if data_rev > hoje:
                                        desc = m.group(2).strip()
                                        revisoes.append({
                                            'summary': f'Revisão: {desc} ({nome_arquivo})',
                                            'date': m.group(1)
                                        })
                    except Exception: continue

    # 2. Busca no YAML (revisions.yml)
    if os.path.exists('revisions.yml'):
        with open('revisions.yml', 'r', encoding='utf-8') as f:
            tarefas = yaml.safe_load(f) or []
            for t in tarefas:
                try:
                    data_rev = datetime.strptime(str(t.get('revisar_em')), '%Y-%m-%d').date()
                    if data_rev > hoje:
                        revisoes.append({
                            'summary': f"🔸 {t['projeto']}: {t.get('detalhes', 'Revisar')}",
                            'date': str(t.get('revisar_em'))
                        })
                except Exception: continue
    
    return revisoes

def evento_ja_existe(service, summary, data):
    """Verifica se o evento já existe na agenda para evitar duplicidade"""
    t_min = f"{data}T00:00:00Z"
    t_max = f"{data}T23:59:59Z"
    
    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=t_min,
        timeMax=t_max,
        q=summary, 
        singleEvents=True
    ).execute()
    
    return len(events_result.get('items', [])) > 0

def processar_agenda():
    # Autenticação (GitHub Secrets ou Local)
    creds_json = os.environ.get('GOOGLE_CALENDAR_CREDENTIAL') or os.environ.get('GOOGLE_CALENDAR_CREDENTIALS')
    
    if creds_json:
        info = json.loads(creds_json)
        creds = service_account.Credentials.from_service_account_info(info)
    else:
        caminho_local = '.github/credentials/credential-googlecalendar.json'
        if not os.path.exists(caminho_local):
            print(f"❌ Erro: Credenciais locais não encontradas em {caminho_local}")
            return
        creds = service_account.Credentials.from_service_account_file(caminho_local)

    service = build('calendar', 'v3', credentials=creds)
    tarefas = buscar_revisoes_futuras()

    if not tarefas:
        print("✅ Tudo em dia! Nenhuma revisão futura detectada (ignorado o dia de hoje).")
        return

    print(f"🔍 Analisando {len(tarefas)} possíveis revisões...")
    for t in tarefas:
        # Checagem de redundância
        if evento_ja_existe(service, t['summary'], t['date']):
            print(f"⏭️  Pulando (já existe): {t['summary']} para {t['date']}")
            continue

        event = {
            'summary': t['summary'],
            'description': 'Automação Horvath: Agendamento antecipado.',
            'start': {'date': t['date'], 'timeZone': 'America/Sao_Paulo'},
            'end': {'date': t['date'], 'timeZone': 'America/Sao_Paulo'},
        }

        try:
            service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
            print(f"✅ Agendado: {t['summary']} para {t['date']}")
        except Exception as e:
            print(f"❌ Erro ao agendar {t['summary']}: {e}")

if __name__ == "__main__":
    processar_agenda()