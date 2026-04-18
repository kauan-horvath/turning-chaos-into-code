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

# ================= CONFIGURAÇÕES DE IDIOMAS =================
DIRETORIOS_PARA_BUSCA = [
    os.path.join(PROJECT_ROOT, "a-language-vault"),
]

EXTENSOES_SUPORTADAS = (".md", ".txt")

# Regex EXCLUSIVA para idiomas
REGEX_BLOCO = re.compile(
    r"::vocab-review::\s*(\d{2}-\d{2}-\d{4})\s*(.*?)::end-vocab::", re.DOTALL
)
CALENDAR_ID = "kauanhorvath1996@gmail.com"
# ==========================================================


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
                    idioma = os.path.splitext(file)[0].upper()

                    try:
                        with open(path, "r", encoding="utf-8", errors="ignore") as f:
                            conteudo = f.read()

                        for match in REGEX_BLOCO.finditer(conteudo):
                            data_br = match.group(1)
                            tabela_conteudo = match.group(2)

                            data_rev = datetime.strptime(data_br, "%d-%m-%Y").date()
                            status = (
                                "hoje"
                                if data_rev == hoje
                                else ("atrasado" if data_rev < hoje else "futuro")
                            )

                            for linha in tabela_conteudo.strip().split("\n"):
                                linha = linha.strip()
                                if linha.startswith("|") and "---" not in linha:
                                    partes = [
                                        p.strip() for p in linha.split("|") if p.strip()
                                    ]

                                    if len(partes) >= 2 and partes[0].lower() not in [
                                        "palavra",
                                        "húngaro",
                                        "inglês",
                                    ]:
                                        partes_limpas = [
                                            re.sub(r"<[^>]+>", "", p)
                                            .replace("*", "")
                                            .strip()
                                            for p in partes
                                        ]

                                        palavra = partes_limpas[0]
                                        significado = partes_limpas[-1]
                                        termo = f"{palavra} = {significado}"

                                        revisoes.append(
                                            {
                                                "termo": termo,
                                                "date_br": data_br,
                                                "date_iso": data_rev.strftime(
                                                    "%Y-%m-%d"
                                                ),
                                                "status": status,
                                                "idioma": idioma,
                                            }
                                        )
                    except Exception:
                        continue
    return revisoes


def processar_agenda():
    # EXATAMENTE COMO NO CHECK-REVISIONS ORIGINAL
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
    tarefas.sort(key=lambda x: x["date_iso"])
    hoje = date.today()

    print(f"\n{'='*75}")
    print(f"🌍 DASHBOARD DE IDIOMAS HORVATH - {hoje.strftime('%d/%m/%Y')}")
    print(f"{'='*75}")

    agrupamento = {"atrasado": {}, "hoje": {}, "futuro": {}}

    for t in tarefas:
        st = t["status"]
        dt = t["date_iso"]
        dt_br = t["date_br"]
        idioma = t["idioma"]

        if dt not in agrupamento[st]:
            agrupamento[st][dt] = {"date_br": dt_br, "idiomas": {}}
        if idioma not in agrupamento[st][dt]["idiomas"]:
            agrupamento[st][dt]["idiomas"][idioma] = []

        agrupamento[st][dt]["idiomas"][idioma].append(t["termo"])

    for categoria in ["atrasado", "hoje", "futuro"]:
        if not agrupamento[categoria]:
            continue

        header = (
            "🚨 ATRASADOS"
            if categoria == "atrasado"
            else ("📅 PARA HOJE" if categoria == "hoje" else "🚀 PRÓXIMAS REVISÕES")
        )
        print(f"\n{header}:")

        for dt_iso, info_data in agrupamento[categoria].items():
            dt_br = info_data["date_br"]

            for idioma, termos in info_data["idiomas"].items():
                quantidade = len(termos)

                if categoria in ["atrasado", "hoje"]:
                    print(f" • [{dt_br}] - {idioma} ({quantidade} palavras):")
                    for termo in termos:
                        print(f"    - {termo}")

                elif categoria == "futuro":
                    titulo_evento = f"🌍 Revisão de {idioma} ({quantidade} palavras)"
                    desc_evento = (
                        f"Suas {quantidade} palavras para revisar hoje:\n\n"
                        + "\n".join([f"- {t}" for t in termos])
                    )

                    try:
                        t_min, t_max = (
                            f"{dt_iso}T00:00:00Z",
                            f"{dt_iso}T23:59:59Z",
                        )
                        existente = (
                            service.events()
                            .list(
                                calendarId=CALENDAR_ID,
                                timeMin=t_min,
                                timeMax=t_max,
                                q=f"Revisão de {idioma}",
                            )
                            .execute()
                        )

                        if not existente.get("items", []):
                            event = {
                                "summary": titulo_evento,
                                "description": desc_evento,
                                "start": {
                                    "date": dt_iso,
                                    "timeZone": "America/Sao_Paulo",
                                },
                                "end": {
                                    "date": dt_iso,
                                    "timeZone": "America/Sao_Paulo",
                                },
                            }
                            service.events().insert(
                                calendarId=CALENDAR_ID, body=event
                            ).execute()
                            prefixo = f"✅ AGENDADO   - [{dt_br}]"
                        else:
                            prefixo = f"⏭️  EXISTENTE - [{dt_br}]"
                    except Exception as e:
                        prefixo = f"❌ ERRO: {e} - [{dt_br}]"

                    print(f" {prefixo} - {idioma} ({quantidade} palavras aguardando)")

    if not tarefas:
        print("\n 😴 Nenhuma revisão de idioma encontrada. Tudo em dia!")

    print(f"\n{'='*75}\n")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    processar_agenda()
