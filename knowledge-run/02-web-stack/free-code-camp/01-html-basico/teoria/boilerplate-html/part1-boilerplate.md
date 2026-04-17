# Certificação de Design Responsivo para a Web

## Entendendo o Boilerplate HTML

### O Elemento `<link>`

O elemento `<link>` é utilizado para conectar o documento HTML a recursos externos, como folhas de estilo (CSS), fontes personalizadas e ícones. Diferente de outros elementos, ele é uma tag **void** (vazia) e deve ser colocado obrigatoriamente dentro da seção `<head>`.

#### Sintaxe para CSS Externo

Separar o HTML do CSS em arquivos distintos é uma das melhores práticas do desenvolvimento web.

```html
<link rel="stylesheet" href="./styles.css" />
```

- **`rel="stylesheet"`**: Define a relação entre o arquivo e o documento (neste caso, uma folha de estilo).
- **`href="./styles.css"`**: Indica o caminho do arquivo. O prefixo `./` instrui o computador a procurar o arquivo na mesma pasta (diretório) do HTML.

---

### Outros Casos de Uso

#### 1. Fontes Externas (Google Fonts)

Você pode carregar fontes personalizadas para o seu site. Frequentemente, isso envolve múltiplos elementos `<link>` para otimizar o carregamento.

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Playwrite+CU&display=swap"
/>
```

- **`preconnect`**: Informa ao navegador para estabelecer uma conexão antecipada com o servidor da fonte, acelerando o carregamento.

#### 2. Favicon (Favorite Icon)

É o pequeno ícone que aparece na aba do navegador, ao lado do título do site, ajudando na identificação da marca.

```html
<link rel="icon" href="favicon.ico" />
```

---

### Exemplo de Estrutura no `<head>`

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Título do Site</title>

  <link rel="stylesheet" href="./styles.css" />

  <link rel="icon" href="favicon.ico" />
</head>
```

---

### Questões de Revisão

**1. Qual é o papel do elemento `link` no HTML?**

- [ ] Ele especifica o tipo de conteúdo do recurso vinculado.
- [ ] Ele determina a visibilidade do recurso vinculado na página da web.
- [ ] Define o tamanho da fonte do recurso vinculado quando exibido.
- [x] É usado para vincular a recursos externos como folhas de estilo e ícones do site.

**2. Qual é o papel do atributo `rel` dentro do elemento `link`?**

- [ ] É usado para indicar o idioma do documento vinculado.
- [x] É usado para especificar a relação entre o recurso vinculado e o documento HTML.
- [ ] É usado para definir o tipo de mídia do documento vinculado.
- [ ] É usado para determinar o tamanho do documento vinculado.

**3. O que é um favicon?**

- [ ] Um tipo de arquivo JavaScript usado para aprimorar a funcionalidade do site.
- [ ] Um tipo de fonte usada para estilizar texto em um site.
- [x] Um pequeno ícone normalmente exibido na aba do navegador ao lado do título do site.
- [ ] Um recurso de segurança usado para prevenir ataques de cross-site scripting.
