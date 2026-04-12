import os

# 1. MAPEAMENTO DE CORREÇÕES
REPLACEMENTS = {
    ">>00-access-python-artigas-home.md": "00-access-vasconcelos-home.md",
}
# 2. CONFIGURAÇÕES
TARGET_DIRECTORY = "./knowledge-run"
EXTENSIONS = (".md",)


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def execute_replacement(is_dry_run: bool):
    """Executa a varredura e substituição. Se is_dry_run for True, não salva."""
    clear_terminal()
    mode_label = "🔍 MODO SIMULAÇÃO" if is_dry_run else "⚠️ MODO REAL (ALTERANDO)"
    print(f"{mode_label}\n" + "=" * 40)

    count_files = 0
    count_changes = 0

    for root, dirs, files in os.walk(TARGET_DIRECTORY):
        for file in files:
            if file.endswith(EXTENSIONS):
                file_path = os.path.join(root, file)
                breadcrumb = (
                    root.replace("./", "").replace("\\", " > ").replace("/", " > ")
                )

                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                new_lines = []
                file_changed = False

                for i, line in enumerate(lines):
                    new_line = line
                    for old, new in REPLACEMENTS.items():
                        if old in line:
                            contexto = (
                                line.strip()[:60] + "..."
                                if len(line.strip()) > 60
                                else line.strip()
                            )

                            print(f"📍 Encontrado em: {breadcrumb} > {file}")
                            print(f'   Original: "{contexto}"')
                            print(f"   -> Sugestão: '{old}' por '{new}'\n")

                            new_line = new_line.replace(old, new)
                            file_changed = True
                            count_changes += 1
                    new_lines.append(new_line)

                if file_changed:
                    count_files += 1
                    if not is_dry_run:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.writelines(new_lines)

    print("=" * 40)
    print(f"📂 Arquivos com ocorrências: {count_files}")
    print(f"🔄 Total de substituições: {count_changes}")

    return count_changes


def mass_replace():
    clear_terminal()
    print("--- 🛠️ LABORATORY LINK-FIXER v2.0 ---")
    print("1 - Simulação (Dry Run)")
    print("2 - Execução Real (Mudar Arquivos)")
    print("3 - Sair")

    choice = input("\nEscolha o modo (1, 2 ou 3): ")

    if choice == "3":
        return

    # Se escolher 1, é dry_run. Se escolher 2, não é.
    is_dry_run = choice == "1"

    changes_found = execute_replacement(is_dry_run)

    # Se rodou simulação e achou coisas, pergunta se quer aplicar
    if is_dry_run and changes_found > 0:
        confirm = input(
            "\n💡 Simulação terminada. Deseja aplicar as mudanças agora? (1-Sim / 2-Não): "
        )
        if confirm == "1":
            print("Executando aplicação real...")
            execute_replacement(is_dry_run=False)


if __name__ == "__main__":
    mass_replace()
