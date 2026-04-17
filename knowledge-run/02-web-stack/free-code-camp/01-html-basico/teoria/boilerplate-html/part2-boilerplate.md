# Certificação de Design Responsivo para a Web

## Entendendo o Boilerplate HTML

### O que é um HTML Boilerplate?

O **Boilerplate** é como um modelo pronto ou a "fundação de uma casa" para suas páginas web. Ele contém a estrutura básica e os elementos essenciais que todo documento HTML precisa para funcionar corretamente, economizando tempo e evitando erros de configuração.

### Anatomia do Boilerplate

#### 1. Declaração do Tipo de Documento

```html
<!DOCTYPE html>
```

Informa ao navegador que o documento está usando a versão mais atual do HTML (HTML5).

#### 2. O Elemento Raiz e Idioma

```html
<html lang="en"></html>
```

Envolve todo o conteúdo da página. O atributo `lang` especifica o idioma principal do documento.

#### 3. A Seção `<head>` (Bastidores)

Contém metadados e informações que não aparecem diretamente na página, mas são cruciais para o navegador e motores de busca.

- **`<meta charset="UTF-8" />`**: Define a codificação de caracteres (garante que acentos e símbolos apareçam corretamente).
- **`<meta name="viewport" ... />`**: Garante que o site seja responsivo (ajuste o tamanho em celulares e tablets).
- **`<title>`**: Define o texto que aparece na aba do navegador.
- **`<link>`**: Conecta arquivos CSS externos.

#### 4. A Seção `<body>` (Conteúdo Visível)

É onde você insere tudo o que o usuário verá: títulos, parágrafos, imagens e vídeos.

```html
<body>
  <h1>Título Principal</h1>
  <p>Conteúdo visível do site.</p>
</body>
```

---

### Por que o Boilerplate é importante?

- **Padronização:** Garante que o site funcione bem em diferentes navegadores.
- **Eficiência:** Permite focar no conteúdo e design imediatamente.
- **Melhores Práticas:** Inclui configurações de acessibilidade e SEO por padrão.

---

### Questões de Revisão

**1. Onde você definiria a codificação de caracteres para sua página?**

- [ ] Um elemento `meta` no `body`.
- [ ] Um elemento `head` no `body`.
- [x] Um elemento `meta` no `head`.
- [ ] No `DOCTYPE`.

**2. Onde você definiria o idioma da sua página?**

- [x] Na tag de abertura `html`.
- [ ] Um elemento `meta` no `body`.
- [ ] Um elemento `head` no `body`.
- [ ] Um elemento `meta` no `head`.

**3. Qual é a finalidade de um boilerplate?**

- [ ] Fornece uma estrutura inicial para seus websites.
- [ ] Garante que você não esteja perdendo nenhum elemento essencial.
- [ ] Permite que você comece a escrever o conteúdo da sua página mais rapidamente.
- [x] Todas as anteriores.
