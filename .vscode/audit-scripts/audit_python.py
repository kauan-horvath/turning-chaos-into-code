# =================== THIS CODE IS AI GENERATED ==============
import os
import subprocess
import re  # Voltamos com ele para extrair o código do erro!

# GPS DINÂMICO
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
REPORT_PATH = os.path.join(SCRIPT_DIR, "RELATORIO_PYTHON.md")


def run_python_audit():
    print(f"🚀 Iniciando Varredura Total de Python em: {PROJECT_ROOT}")

    # 1. Busca manual de todos os arquivos .py
    py_files = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        # Ignora pastas desnecessárias
        for skip in [
            ".git",
            "__pycache__",
            ".private",
            "node_modules",
            "audit-scripts",
        ]:
            if skip in dirs:
                dirs.remove(skip)

        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))

    print(f"📊 {len(py_files)} arquivos encontrados. Analisando PEP 8...")

    unique_files = {}

    # 2. Analisa os arquivos via Flake8
    for path in py_files:
        cmd = [
            "python",
            "-m",
            "flake8",
            path,
            "--max-line-length=120",
            # O Escudo Definitivo: Ignora E501, F401 e os conflitos do Black (W503, E203)
            "--extend-ignore=E501,F401,W503,E203",
            "--format=%(path)s:%(row)d:%(col)d:%(code)s %(text)s",
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        raw_errors = result.stdout.strip()

        if raw_errors:
            lines = raw_errors.split("\n")
            unique_files[path] = lines

    # 3. Gera o relatório simplificado e ordenado
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        if not unique_files:
            f.write("# ✨ ALL-FIXED\n\nPython está seguindo os padrões PEP 8!")
            print("✅ Python: ALL-FIXED")
        else:
            sorted_files = sorted(unique_files.items(), key=lambda x: len(x[1]))

            f.write("# 🐍 RELATÓRIO DE FAXINA PYTHON\n\n")
            f.write(f"**Total de arquivos com pendências:** {len(sorted_files)}\n\n")

            for i, (path, errors) in enumerate(sorted_files, 1):
                file_name = os.path.basename(path)
                try:
                    rel_path = os.path.relpath(path, SCRIPT_DIR).replace("\\", "/")
                except ValueError:
                    rel_path = path

                # Magia para extrair apenas o código do erro (ex: E203, W503)
                error_codes = set()
                for e in errors:
                    match = re.search(r"([A-Z]\d{3})", e)
                    if match:
                        error_codes.add(match.group(1))

                # Cria a micro-tag, ex: " [W503, F841]"
                codes_str = f" [{', '.join(error_codes)}]" if error_codes else ""

                # Formatação solicitada
                f.write(
                    f"========================================================{i:02}\n"
                )
                f.write(f"FILE: 📄 {file_name}\n")
                # Agora você sabe exatamente o que está pegando!
                f.write(f"PENDENCIAS: {len(errors)}{codes_str}\n")
                f.write(f"LINK: [{rel_path}]({rel_path})\n")

            f.write("========================================================END\n")
            print(f"❌ Finalizado! {len(sorted_files)} arquivos Python com problemas.")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    run_python_audit()
