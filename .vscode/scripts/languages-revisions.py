# =================== THIS CODE IS AI GENERATED ==============
import os
import re
import json
from datetime import date, datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# ================= GPS DINÂMICO =================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

# ================= CONFIGURAÇÕES DE IDIOMAS =================
DIRETORIOS_PARA_BUSCA = [
    os.path.join(PROJECT_ROOT, "a-language-vault"),
]

EXTENSOES_SUPORTADAS = (".md", ".txt")

# Regex para capturar TEMA, DATA e TURNO (opcional)
REGEX_BLOCO = re.compile(
    r"::vocab-review::\s*(.*?)\s*::\s*(\d{2}-\d{2}-\d{4})(?:\s*::\s*(TURN\s*\d+))?\s*(.*?)::end-vocab::",
    re.IGNORECASE | re.DOTALL,
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
                            tema = match.group(1).strip().upper()
                            data_br = match.group(2).strip()

                            turno_match = match.group(3)
                            turno = (
                                turno_match.strip().upper() if turno_match else "TURN 1"
                            )

                            tabela_conteudo = match.group(4)

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
                                                "tema": tema,
                                                "turno": turno,
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
    hoje = date.today()

    # --- Header do Dashboard ---
    print(f"\n{'='*82}")
    print(f"🌍 DASHBOARD DE IDIOMAS HORVATH - {hoje.strftime('%d/%m/%Y')}")
    print()

    # --- Cálculo e Print do Total Acumulado ---
    total_por_idioma = {}
    for t in tarefas:
        idi = t["idioma"]
        total_por_idioma[idi] = total_por_idioma.get(idi, 0) + 1

    if total_por_idioma:
        print("📊 TOTAL ACUMULADO:")
        for idi, qtd in total_por_idioma.items():
            print(f"  • {idi.upper()}: {qtd} words")

    print(f"{'='*82}\n")

    if not tarefas:
        print(" 😴 Nenhuma revisão de idioma encontrada. Tudo em dia!\n")
        print(f"{'='*82}\n")
        return

    agrupamento_unico = {}
    for t in tarefas:
        chave = (t["idioma"], t["tema"], t["turno"], t["date_iso"])
        if chave not in agrupamento_unico:
            agrupamento_unico[chave] = {
                "idioma": t["idioma"],
                "tema": t["tema"],
                "turno": t["turno"],
                "date_iso": t["date_iso"],
                "date_br": t["date_br"].replace("-", "/"),
                "status": t["status"],
                "termos": [],
            }
        agrupamento_unico[chave]["termos"].append(t["termo"])

    todas_as_linhas = list(agrupamento_unico.values())
    todas_as_linhas.sort(key=lambda x: (x["idioma"], x["date_iso"]))

    # --- Print da Tabela (Label Row) ---
    print(
        f" {'IDIOMA':<12} | {'STATUS':<16} | {'DATA':<10} | {'TEMA':<22} | {'TRN':^3} | {'QTD':^3}"
    )
    print("-" * 82)

    ultimo_idioma = None
    for dados in todas_as_linhas:
        idioma = dados["idioma"]

        # Insere espaço entre diferentes idiomas
        if ultimo_idioma and idioma != ultimo_idioma:
            print()

        tema = dados["tema"]
        turno = dados["turno"]
        dt_iso = dados["date_iso"]
        dt_br = dados["date_br"]
        status = dados["status"]
        termos = dados["termos"]
        quantidade = len(termos)

        tema_formatado = tema[:21] + "…" if len(tema) > 22 else tema
        turno_num = turno.replace("TURN", "").strip()
        qtd_str = f"{quantidade:02d}"

        # Prefixos formatados com largura fixa de 16 para evitar desalinhamento por emojis
        prefixo = ""

        if status == "futuro":
            titulo_evento = (
                f"🌍 Revisão de {idioma} ({tema} | {turno}) - {quantidade} palavras"
            )
            desc_evento = (
                f"Suas {quantidade} palavras de {tema} ({turno}) para revisar hoje:\n\n"
                + "\n".join([f"- {t}" for t in termos])
            )

            try:
                t_min, t_max = (f"{dt_iso}T00:00:00Z", f"{dt_iso}T23:59:59Z")
                existente = (
                    service.events()
                    .list(
                        calendarId=CALENDAR_ID,
                        timeMin=t_min,
                        timeMax=t_max,
                        q=f"Revisão de {idioma} ({tema} | {turno})",
                    )
                    .execute()
                )

                if not existente.get("items", []):
                    event = {
                        "summary": titulo_evento,
                        "description": desc_evento,
                        "start": {"date": dt_iso, "timeZone": "America/Sao_Paulo"},
                        "end": {"date": dt_iso, "timeZone": "America/Sao_Paulo"},
                    }
                    service.events().insert(
                        calendarId=CALENDAR_ID, body=event
                    ).execute()
                    prefixo = "✅ AGENDADO     "
                else:
                    prefixo = "⏩ EXISTENTE    "
            except Exception as e:
                prefixo = f"❌ ERRO {e}    "

        elif status == "hoje":
            prefixo = "📅 PARA HOJE    "
        elif status == "atrasado":
            prefixo = "🚨 ATRASADO     "

        print(
            f" {idioma:<12} | {prefixo} | {dt_br:<10} | {tema_formatado:<22} | {turno_num:^3} | {qtd_str:^3}"
        )
        ultimo_idioma = idioma

    print(f"\n{'='*82}\n")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    processar_agenda()
