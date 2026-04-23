import os
import re
from datetime import datetime, timedelta

# ================= CONFIGURAÇÕES =================
ARQUIVO_MD = "hungaro.md"

# Regra de saltos a partir da última revisão concluída
# Turno atual concluído -> Dias para a próxima cobrança
SALTOS = {
    "Turn 1": 1,
    "Turn 2": 3,
    "Turn 3": 7,
    "Turn 4": 14,
    "Turn 5": 30,
    "MASTER": 9999,  # Master não é cobrado por data, entra na Chave Zero
}

# ================= REGEX =================
REGEX_TEMA = re.compile(r"^##\s+(.+)", re.IGNORECASE)
REGEX_REVIEW = re.compile(
    r"^::\s*review\s*::\s*(\d{2}-\d{2}-\d{4})\s*::\s*(Turn \d+|MASTER)", re.IGNORECASE
)
REGEX_PALAVRA = re.compile(r"^-\s+(.+?)\s*:\s*(.+)")


def processar_vocabulario():
    hoje = datetime.now().date()

    alvo_principal = []
    apoio_ativo = []
    fluente = []
    definitiva_plus = []

    if not os.path.exists(ARQUIVO_MD):
        print(f"Arquivo {ARQUIVO_MD} não encontrado.")
        return

    with open(ARQUIVO_MD, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    tema_atual = None
    ultimo_turno = None
    data_prox_revisao = None

    for linha in linhas:
        linha = linha.strip()

        # Encontra o Tema
        match_tema = REGEX_TEMA.match(linha)
        if match_tema:
            tema_atual = match_tema.group(1).strip()
            ultimo_turno = None
            data_prox_revisao = None
            continue

        # Encontra a Revisão
        match_review = REGEX_REVIEW.match(linha)
        if match_review:
            data_str, turno = match_review.groups()
            data_rev = datetime.strptime(data_str, "%d-%m-%Y").date()
            ultimo_turno = turno.upper() if turno.upper() == "MASTER" else turno.title()

            if ultimo_turno in SALTOS:
                data_prox_revisao = data_rev + timedelta(days=SALTOS[ultimo_turno])
            continue

        # Encontra a Palavra
        match_palavra = REGEX_PALAVRA.match(linha)
        if match_palavra and tema_atual and ultimo_turno:
            palavra_raw = match_palavra.group(1).strip()
            mnemonica = match_palavra.group(2).strip()

            tem_estrela = "*" in palavra_raw
            palavra = palavra_raw.replace("*", "").strip()

            registro = f"{palavra} ({mnemonica})"

            if tem_estrela:
                definitiva_plus.append(registro)
            elif ultimo_turno == "MASTER":
                fluente.append(registro)
            elif data_prox_revisao and data_prox_revisao <= hoje:
                alvo_principal.append(registro)
            else:
                apoio_ativo.append(registro)

    # ================= GERAR SAÍDA PARA O TERMINAL =================
    print("=" * 60)
    print("📋 COPIE O TEXTO ABAIXO E COLE NA IA")
    print("=" * 60)
    print("\n[ALVO PRINCIPAL - REVISÃO DO DIA]")
    print(
        ", ".join(alvo_principal)
        if alvo_principal
        else "Nenhuma palavra atrasada hoje."
    )

    print("\n[APOIO ATIVO - CONSTRUÇÃO DE CONTEXTO]")
    print(", ".join(apoio_ativo) if apoio_ativo else "Nenhuma.")

    print("\n[VOCABULÁRIO FLUENTE - TRICKY QUESTIONS]")
    print(", ".join(fluente) if fluente else "Nenhuma.")

    print("\n[DEFINITIVAS PLUS - USO NATIVO]")
    print(", ".join(definitiva_plus) if definitiva_plus else "Nenhuma.")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    processar_vocabulario()
