# =================== THIS CODE IS AI GENERATED ==============
import os
import re
import json
from datetime import date, datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# ================= GPS DINÂMICO (NOVO) =================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

# ================= CONFIGURAÇÕES =================
DIRETORIOS_PARA_BUSCA = [
    os.path.join(PROJECT_ROOT, "knowledge-run"),
    os.path.join(PROJECT_ROOT, "care-projects"),
]

# EXTENSÕES PERMITIDAS
EXTENSOES_SUPORTADAS = (".py", ".md", ".sql", ".vba", ".html", ".htm")

REGEX_REVIEW = r"::to-review::\s*(\d{2}-\d{2}-\d{4})\s*::(.*)::"
CALENDAR_ID = "kauanhorvath1996@gmail.com"
# =================================================

DIRETORIOS = DIRETORIOS_PARA_BUSCA
PADRAO_ANTIGO = r"#\s*TODO:\s*\[REVIEW-DATE:\s*(\d{4})-(\d{2})-(\d{2})\]\s*(.*)"
NOVO_FORMATO = r"::to-review:: \3-\2-\1 ::\4::"


def migrar_tags():
    print("🛠️  Iniciando migração para o padrão ::to-review::...")
    arquivos_alterados = 0
    tags_convertidas = 0

    for diretorio in DIRETORIOS:
        if not os.path.exists(diretorio):
            continue
        for root, _, files in os.walk(diretorio):
            for file in files:
                if file.endswith(EXTENSOES_SUPORTADAS):
                    path = os.path.join(root, file)
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
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
                        with open(path, "w", encoding="utf-8") as f:
                            f.writelines(novas_linhas)
                        print(f"✅ Atualizado: {file}")
                        arquivos_alterados += 1

    print(
        f"\n✨ Sucesso! {tags_convertidas} tags em {arquivos_alterados} arquivos foram migradas."
    )


def buscar_revisoes():
    revisoes = []
    hoje = date.today()

    for diretorio in DIRETORIOS_PARA_BUSCA:
        if not os.path.exists(diretorio):
            continue
        for root, _, files in os.walk(diretorio):
            for file in files:
                if file.endswith(EXTENSOES_SUPORTADAS):
                    path = os.path.join(root, file)
                    nome_arquivo = os.path.basename(path)

                    try:
                        with open(path, "r", encoding="utf-8", errors="ignore") as f:
                            for line in f:
                                m = re.search(REGEX_REVIEW, line)
                                if m:
                                    data_br = m.group(1)
                                    data_rev = datetime.strptime(
                                        data_br, "%d-%m-%Y"
                                    ).date()
                                    desc = m.group(2).strip()

                                    status = (
                                        "hoje"
                                        if data_rev == hoje
                                        else (
                                            "atrasado" if data_rev < hoje else "futuro"
                                        )
                                    )

                                    revisoes.append(
                                        {
                                            "title": desc,
                                            "summary": f"Revisão: {desc}",
                                            "date_br": data_br,
                                            "date_iso": data_rev.strftime("%Y-%m-%d"),
                                            "status": status,
                                            "file": nome_arquivo,
                                        }
                                    )
                    except Exception:
                        continue
    return revisoes


def processar_agenda():
    creds_json = os.environ.get("GOOGLE_CALENDAR_CREDENTIAL") or os.environ.get(
        "GOOGLE_CALENDAR_CREDENTIALS"
    )
    if creds_json:
        info = json.loads(creds_json)
        creds = service_account.Credentials.from_service_account_info(info)
    else:
        caminho_local = os.path.join(
            PROJECT_ROOT, ".private", "credentials", "credential-googlecalendar.json"
        )
        creds = service_account.Credentials.from_service_account_file(caminho_local)

    service = build("calendar", "v3", credentials=creds)
    tarefas = buscar_revisoes()

    # Ordenar PRIMEIRO por Status (Atrasado -> Hoje -> Futuro), DEPOIS por Data
    ordem_status = {"atrasado": 0, "hoje": 1, "futuro": 2}
    tarefas.sort(key=lambda x: (ordem_status[x["status"]], x["date_iso"]))

    hoje = date.today()

    # --- Header do Dashboard (Largura travada em 80 chars) ---
    print(f"\n{'='*80}")
    print(f"📊 DASHBOARD DE REVISÕES HORVATH - {hoje.strftime('%d/%m/%Y')}")
    print(f"{'='*80}\n")

    if not tarefas:
        print(" 😴 Nenhuma revisão encontrada. Tudo em dia!\n")
        print(f"{'='*80}\n")
        return

    # --- Print da Tabela (Label Row) ---
    # Redistribuímos para exatos 80 chars (evita quebrar a linha no terminal)
    print(f" {'STATUS':<15} | {'DATA':<10} | {'ASSUNTO':<28} | {'ARQUIVO':<20}")
    print("-" * 80)

    ultimo_status = None

    for t in tarefas:
        status = t["status"]

        # Insere espaço sempre que mudar de grupo (ex: HOJE -> FUTURO)
        if ultimo_status and status != ultimo_status:
            print()

        dt_br = t["date_br"].replace("-", "/")
        assunto = t["title"]
        arquivo = t.get("file", "N/A")

        # Trunca as strings limitando exatamente ao tamanho da coluna
        assunto_fmt = assunto[:27] + "…" if len(assunto) > 28 else assunto
        arquivo_fmt = arquivo[:19] + "…" if len(arquivo) > 20 else arquivo

        # Prefixos formatados MANUALMENTE (exatos 15 caracteres visuais)
        prefixo = ""

        if status == "futuro":
            try:
                t_min, t_max = (
                    f"{t['date_iso']}T00:00:00Z",
                    f"{t['date_iso']}T23:59:59Z",
                )
                existente = (
                    service.events()
                    .list(
                        calendarId=CALENDAR_ID,
                        timeMin=t_min,
                        timeMax=t_max,
                        q=t["summary"],
                    )
                    .execute()
                )

                if not existente.get("items", []):
                    event = {
                        "summary": t["summary"],
                        "start": {
                            "date": t["date_iso"],
                            "timeZone": "America/Sao_Paulo",
                        },
                        "end": {"date": t["date_iso"], "timeZone": "America/Sao_Paulo"},
                    }
                    service.events().insert(
                        calendarId=CALENDAR_ID, body=event
                    ).execute()
                    prefixo = "✅ AGENDADO    "
                else:
                    prefixo = "⏩ EXISTENTE   "
            except Exception as e:
                prefixo = f"❌ ERRO {e}    "

        elif status == "hoje":
            prefixo = "📅 PARA HOJE   "
        elif status == "atrasado":
            prefixo = "🚨 ATRASADO    "

        # Print final travado em 80 colunas
        print(f" {prefixo} | {dt_br:<10} | {assunto_fmt:<28} | {arquivo_fmt:<20}")

        ultimo_status = status

    print(f"\n{'='*80}\n")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    processar_agenda()
