# Certificação de Design Responsivo para a Web

## Entendendo Atributos HTML

### Qual o Papel do HTML na Web?

**HTML** (_Hypertext Markup Language_) é a linguagem de marcação padrão para criar páginas web. Ela é responsável por todo o conteúdo que você vê ao visitar um site: parágrafos, títulos, links, imagens e vídeos.

#### Estrutura Básica de Elementos

O HTML representa a estrutura de uma página por meio de **elementos**. A maioria deles possui uma tag de abertura e uma de fechamento (também chamadas de tags de início e fim).

**Exemplo:**

```html
<h1>Main heading element</h1>
<p>I am a paragraph element.</p>
```

As tags são delimitadas pelos sinais de menor (`<`) e maior (`>`). Por convenção, utilizamos sempre letras minúsculas. O que diferencia a tag de fechamento é a barra (`/`) imediatamente após o sinal de menor.

---

### Elementos Void (Vazios)

Alguns elementos não possuem tag de fechamento nem conteúdo interno. Eles são conhecidos como **elementos void**.

**Exemplo de imagem:**

```html
<img />
```

Você também pode encontrar a sintaxe de auto-fechamento (muito usada por formatadores como o Prettier):

```html
<img />
```

_Nota: A especificação HTML considera a barra `/` em elementos void desnecessária, mas ela é comum no desenvolvimento real e não causa erros._

---

### Atributos HTML

Atributos são valores especiais inseridos dentro da tag de abertura para ajustar o comportamento do elemento. No caso de imagens, os principais são:

1. **`src` (source):** Especifica o local (URL) da imagem.
2. **`alt` (alternative text):** Fornece uma descrição textual da imagem (importante para acessibilidade e caso o carregamento falhe).

**Exemplo prático:**

```html
<img
  src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"
  alt="Two tabby kittens sleeping together on a couch."
/>
```

---

### A Tríade da Web: HTML, CSS e JavaScript

Para sites profissionais, o HTML raramente trabalha sozinho. Uma analogia comum é comparar a construção de um site com a de um prédio:

- **HTML (Estrutura):** Os blocos, concreto e vigas. Define a base e a força do edifício.
- **CSS (Estilo):** O design interior, cores e acabamentos. Deixa a casa bonita.
- **JavaScript (Interatividade):** Os sistemas elétrico e hidráulico. Garante que as coisas funcionem (luzes acendam, água corra).

---

### Questões de Revisão

**1. O que significa HTML?**

- [ ] Linguagem HyperText Maker
- [ ] Linguagem de Marcação de Textos
- [ ] Linguagem de Marcação HyperText
- [x] Linguagem de Marcação de Hipertexto

**2. Qual das seguintes é a sintaxe correta para uma tag de fechamento?**

- [ ] `<;p>`
- [ ] `<p>`
- [x] `</p>`
- [ ] `<///p/>`

**3. Qual dos seguintes é um atributo válido usado dentro do elemento `img`?**

- [x] `src`
- [ ] `bold`
- [ ] `closing`
- [ ] `div`
