# =================== THIS CODE IS AI GENERATED ==============
import os
import re
import yaml
import json
from datetime import date, datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# ================= GPS DINÂMICO (NOVO) =================
# Calcula a raiz do projeto automaticamente, independente do terminal
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
# =======================================================

# ================= CONFIGURAÇÕES =================
DIRETORIOS_PARA_BUSCA = [
    os.path.join(PROJECT_ROOT, 'knowledge-run'), 
    os.path.join(PROJECT_ROOT, 'care-projects')
]
# Nova REGEX: Captura data BR e o título entre :: ::
REGEX_REVIEW = r"::to-review::\s*(\d{2}-\d{2}-\d{4})\s*::(.*)::"
CALENDAR_ID = 'kauanhorvath1996@gmail.com' 
# =================================================

DIRETORIOS = DIRETORIOS_PARA_BUSCA

# Captura: # TODO: [REVIEW-DATE: YYYY-MM-DD] TEXTO
PADRAO_ANTIGO = r"#\s*TODO:\s*\[REVIEW-DATE:\s*(\d{4})-(\d{2})-(\d{2})\]\s*(.*)"

# Transforma em: ::to-review:: DD-MM-YYYY ::TEXTO::
# \3 = dia, \2 = mês, \1 = ano, \4 = título
NOVO_FORMATO = r"::to-review:: \3-\2-\1 ::\4::" 

def migrar_tags():
    print("🛠️  Iniciando migração para o padrão ::to-review::...")
    arquivos_alterados = 0
    tags_convertidas = 0

    for diretorio in DIRETORIOS:
        if not os.path.exists(diretorio): continue
        for root, _, files in os.walk(diretorio):
            for file in files:
                if file.endswith(('.py', '.md', '.sql', '.vba')):
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        linhas = f.readlines()
                    
                    novas_linhas = []
                    mudou_arquivo = False
                    
                    for linha in linhas:
                        if re.search(PADRAO_ANTIGO, linha):
                            nova_linha = re.sub(PADRAO_ANTIGO, NOVO_FORMATO, linha)
                            novas_linhas.append(nova_linha)
                            tags_convertidas += 1
                            mudou_arquivo = True
                        else:
                            novas_linhas.append(linha)
                    
                    if mudou_arquivo:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.writelines(novas_linhas)
                        print(f"✅ Atualizado: {file}")
                        arquivos_alterados += 1

    print(f"\n✨ Sucesso! {tags_convertidas} tags em {arquivos_alterados} arquivos foram migradas.")

def buscar_revisoes():
    revisoes = []
    hoje = date.today()

    for diretorio in DIRETORIOS_PARA_BUSCA:
        if not os.path.exists(diretorio): continue
        for root, _, files in os.walk(diretorio):
            for file in files:
                if file.endswith(('.py', '.md', '.sql', '.vba')):
                    path = os.path.join(root, file)
                    nome_arquivo = os.path.basename(path)
                    nome_pasta = os.path.basename(root)

                    try:
                        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                            for line in f:
                                m = re.search(REGEX_REVIEW, line)
                                if m:
                                    data_br = m.group(1)
                                    data_rev = datetime.strptime(data_br, '%d-%m-%Y').date()
                                    desc = m.group(2).strip()
                                    
                                    # Lógica de status
                                    status = "hoje" if data_rev == hoje else ("atrasado" if data_rev < hoje else "futuro")
                                    
                                    revisoes.append({
                                        'title': desc, # Título limpo
                                        'summary': f'Revisão: {desc}', # Para o Google Calendar
                                        'date_br': data_br,
                                        'date_iso': data_rev.strftime('%Y-%m-%d'),
                                        'status': status,
                                        'file': nome_arquivo,
                                        'folder': nome_pasta
                                    })
                    except Exception: continue
    return revisoes

def processar_agenda():
    creds_json = os.environ.get('GOOGLE_CALENDAR_CREDENTIAL') or os.environ.get('GOOGLE_CALENDAR_CREDENTIALS')
    if creds_json:
        info = json.loads(creds_json)
        creds = service_account.Credentials.from_service_account_info(info)
    else:
        # ======= CORREÇÃO APLICADA AQUI 👇 =======
        # Agora ele usa o GPS absoluto para achar a pasta, sem erro!
        caminho_local = os.path.join(PROJECT_ROOT, '.private', 'credentials', 'credential-googlecalendar.json')
        # =========================================
        creds = service_account.Credentials.from_service_account_file(caminho_local)

    service = build('calendar', 'v3', credentials=creds)
    
    # 1. Busca as revisões
    tarefas = buscar_revisoes()
    
    # 2. ORDENAÇÃO: Da data mais próxima para a mais distante
    tarefas.sort(key=lambda x: x['date_iso'])
    
    hoje = date.today()

    print(f"\n{'='*75}")
    print(f"📊 DASHBOARD DE REVISÕES HORVATH - {hoje.strftime('%d/%m/%Y')}")
    print(f"{'='*75}")

    # Mantemos a separação por blocos, mas cada bloco estará ordenado por data
    for categoria in ["atrasado", "hoje", "futuro"]:
        itens = [t for t in tarefas if t['status'] == categoria]
        if not itens: continue

        header = "🚨 ATRASADOS (Ignorados pelo agendador)" if categoria == "atrasado" \
                 else ("📅 PARA HOJE" if categoria == "hoje" else "🚀 PRÓXIMAS REVISÕES")
        print(f"\n{header}:")
        
        for t in itens:
            if categoria == "futuro":
                try:
                    t_min = f"{t['date_iso']}T00:00:00Z"
                    t_max = f"{t['date_iso']}T23:59:59Z"
                    existente = service.events().list(calendarId=CALENDAR_ID, timeMin=t_min, timeMax=t_max, q=t['summary']).execute()
                    
                    if not existente.get('items', []):
                        event = {
                            'summary': t['summary'],
                            'start': {'date': t['date_iso'], 'timeZone': 'America/Sao_Paulo'},
                            'end': {'date': t['date_iso'], 'timeZone': 'America/Sao_Paulo'},
                        }
                        service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
                        prefixo = f"✅ AGENDADO  - [{t['date_br']}]"
                    else:
                        prefixo = f"⏭️  EXISTENTE - [{t['date_br']}]"
                except Exception as e:
                    prefixo = f"❌ ERRO       - [{t['date_br']}]"
            else:
                # Exibe o status (Atrasado ou Hoje) seguido da data
                status_label = "ATRASADO" if categoria == "atrasado" else "HOJE"
                prefixo = f"• {status_label}    - [{t['date_br']}]"

            # OUTPUT REFINADO EM DUAS LINHAS
            print(f" {prefixo} - {t['summary']}")
            print(f"    file: ({t.get('file', 'N/A')}) | folder: ({t.get('folder', 'N/A')})")

    print(f"\n{'='*75}\n")

if __name__ == "__main__":
    os.system("cls" if os.name =="nt" else "clear")
    #migrar_tags()
    processar_agenda()