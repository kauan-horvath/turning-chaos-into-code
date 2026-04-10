# ==========================================
# PAINEL DE CONTROLE - PREENCHA AQUI
# ==========================================

B1 = {"label": "English", 
      "txt": "Full_Fluency", 
      "color": "orange", 
      "logo": "googletranslate"}

B2 = {"label": "Software", 
      "txt": "Dentrix_Expert", 
      "color": "blue", 
      "logo": "serverless"}

# Para os simples, basta não colocar o "label"
B3 = {"txt": "Voluntary_Instructor", 
      "color": "green", 
      "logo": "gitbook"}

B4 = {"txt": "Applied_Semiotics", 
      "color": "502D80", 
      "logo": "strapi"}

# ==========================================
# MOTOR (NÃO MEXER)
# ==========================================

def build_html(b, index):
    label_part = f"{b.get('label')}-" if b.get('label') else ""
    url = f"https://img.shields.io/badge/{label_part}{b['txt']}-{b['color']}?style=flat-square&logo={b['logo']}&logoColor=white"
    
    # Formatação exata do HTML solicitada
    return f'<img src="{url}" \n     alt="Stats {index:02d}" style="margin-right: 5px; margin-bottom: 5px;">'

print("\n\n")
print(build_html(B1, 1) + "\n")
print(build_html(B2, 2) + "\n")
print(build_html(B3, 3) + "\n")
print(build_html(B4, 4))
print("\n\n")