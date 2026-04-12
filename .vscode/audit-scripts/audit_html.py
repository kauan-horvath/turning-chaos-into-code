# =================== THIS CODE IS AI GENERATED ==============
import os
import subprocess
import re

# GPS DINÂMICO
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
REPORT_PATH = os.path.join(SCRIPT_DIR, 'RELATORIO_HTML.md')

def run_html_audit():
    print(f"🚀 Iniciando Varredura Total de HTML em: {PROJECT_ROOT}")
    
    # 1. Busca manual de todos os arquivos .html (garante que nenhum escape)
    html_files = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        if 'node_modules' in dirs: dirs.remove('node_modules')
        if '.git' in dirs: dirs.remove('.git')
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    
    print(f"📊 {len(html_files)} arquivos encontrados. Analisando...")
    
    unique_files = {}
    
    # 2. Analisa cada arquivo individualmente para evitar que o linter pule arquivos
    for path in html_files:
        cmd = f'npx -y htmlhint "{path}" --ignore node_modules'
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        
        output = result.stdout.strip()
        if output:
            # Filtra apenas as linhas que indicam erros (contêm 'line')
            errors = [line for line in output.split('\n') if 'line' in line.lower()]
            if errors:
                unique_files[path] = errors

    # 3. Gera o relatório simplificado
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        if not unique_files:
            f.write("# ✨ ALL-FIXED\n\nSeu HTML está impecável!")
            print("✅ HTML: ALL-FIXED")
        else:
            # Ordenar: Menos erros primeiro
            sorted_files = sorted(unique_files.items(), key=lambda x: len(x[1]))
            
            f.write(f"# 🌐 RELATÓRIO DE FAXINA HTML\n\n")
            f.write(f"**Total de arquivos com pendências:** {len(sorted_files)}\n\n")
            
            for i, (path, errors) in enumerate(sorted_files, 1):
                file_name = os.path.basename(path)
                try:
                    rel_path = os.path.relpath(path, SCRIPT_DIR).replace("\\", "/")
                except:
                    rel_path = path

                f.write(f"========================================================{i:02}\n")
                f.write(f"FILE: 📄 {file_name}\n")
                f.write(f"PENDENCIAS: {len(errors)}\n")
                f.write(f"LINK: [{rel_path}]({rel_path})\n")
            
            f.write("========================================================END\n")
            print(f"❌ Finalizado! {len(sorted_files)} arquivos com problemas encontrados.")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    run_html_audit()