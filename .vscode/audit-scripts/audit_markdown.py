# =================== THIS CODE IS AI GENERATED ==============
import os
import subprocess
import re

# GPS DINÂMICO
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
REPORT_PATH = os.path.join(SCRIPT_DIR, 'RELATORIO_MARKDOWN.md')

def run_markdown_audit():
    print(f"🚀 Iniciando Varredura Total de Markdown em: {PROJECT_ROOT}")
    
    # 1. Busca manual de todos os arquivos .md
    md_files = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        for skip in ['.git', 'node_modules', '.private']:
            if skip in dirs:
                dirs.remove(skip)
        
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    
    total_found = len(md_files)
    print(f"📊 {total_found} arquivos encontrados. Analisando estrutura...")
    
    unique_files = {}
    
    # 2. Analisa cada arquivo via markdownlint
    # Usamos o '-y' para não travar e analisamos um por um para garantir precisão
    for path in md_files:
        cmd = f'npx -y markdownlint-cli "{path}"'
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        
        # O markdownlint joga os erros no stderr
        raw_errors = result.stderr.strip()
        
        if raw_errors:
            lines = raw_errors.split('\n')
            # Filtra apenas linhas que seguem o padrão de erro (contém o path)
            clean_errors = [line for line in lines if path in line]
            if clean_errors:
                unique_files[path] = clean_errors

    # 3. Gera o relatório simplificado e ordenado
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        if not unique_files:
            f.write("# ✨ ALL-FIXED\n\nNenhuma sujeira encontrada no Markdown!")
            print("✅ Markdown: ALL-FIXED")
        else:
            # Ordenar: Menos pendências primeiro para "Quick Wins"
            sorted_files = sorted(unique_files.items(), key=lambda x: len(x[1]))
            
            f.write(f"# 📝 RELATÓRIO DE FAXINA MARKDOWN\n\n")
            f.write(f"**Arquivos analisados:** {total_found}\n")
            f.write(f"**Arquivos com pendências:** {len(sorted_files)}\n\n---\n\n")
            
            for i, (path, errors) in enumerate(sorted_files, 1):
                file_name = os.path.basename(path)
                try:
                    rel_path = os.path.relpath(path, SCRIPT_DIR).replace("\\", "/")
                except:
                    rel_path = path

                # Formatação simplificada solicitada
                f.write(f"========================================================{i:02}\n")
                f.write(f"FILE: 📄 {file_name}\n")
                f.write(f"PENDENCIAS: {len(errors)}\n")
                f.write(f"LINK: [{rel_path}]({rel_path})\n")
            
            f.write("========================================================END\n")
            print(f"❌ Finalizado! {len(sorted_files)} arquivos Markdown com problemas.")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    run_markdown_audit()