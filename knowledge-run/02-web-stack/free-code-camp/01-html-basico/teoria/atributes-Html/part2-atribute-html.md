# Certificação de Design Responsivo para a Web

## Entendendo Atributos HTML

### O que são atributos e como eles funcionam?

Um **atributo** é um valor inserido dentro da tag de abertura de um elemento HTML. Eles servem para fornecer informações extras ou especificar o comportamento de um elemento.

**Sintaxe Básica:**

```html
<elemento atributo="valor"></elemento>
```

O nome do atributo é seguido por um sinal de igual (`=`) e o valor fica entre aspas (pode ser texto ou número).

---

### Exemplos Comuns de Atributos

#### 1. Elemento Âncora (`<a>`)

Usado para criar links (hyperlinks).

- **`href`**: Especifica o destino (URL). Sem ele, o link não funciona.
- **`target="_blank"`**: Abre o link em uma nova aba.

```html
<a href="https://www.freecodecamp.org" target="_blank">Visit freeCodeCamp</a>
```

#### 2. Elemento de Imagem (`<img>`)

- **`src`**: Atributo obrigatório que define o arquivo de imagem.
- **`alt`**: Texto alternativo para **acessibilidade** (garante que pessoas com deficiência ou com conexões lentas entendam o conteúdo).

```html
<img
  src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"
  alt="Two tabby kittens sleeping together on a couch."
/>
```

---

### Atributos Booleanos

Alguns atributos possuem uma sintaxe única: eles não precisam de um valor (como `="algo"`). Se o nome do atributo estiver presente na tag, ele é considerado verdadeiro (ativo).

- **`checked`**: Define que uma caixa de seleção (_checkbox_) deve iniciar marcada.
- **`disabled`**: Desabilita o elemento, impedindo a interação do usuário.
- **`readonly`**: O campo é apenas para leitura.
- **`required`**: Torna o preenchimento do campo obrigatório.

**Exemplos:**

```html
<input type="checkbox" checked />

<input type="text" disabled />
```

---

### Questões de Revisão

**1. Qual dos seguintes é um exemplo de um atributo booleano?**

- [ ] `src`
- [ ] `href`
- [x] `disabled`
- [ ] `alt`

**2. Qual é o papel de um atributo em HTML?**

- [x] Atributos fornecem informações adicionais e ajudam a definir o comportamento dos elementos HTML.
- [ ] Os atributos mudam a cor de fundo de um elemento.
- [ ] Os atributos alteram o tamanho da fonte de um elemento.
- [ ] Atributos adicionam funcionalidade JavaScript a um elemento.

**3. Qual das seguintes é a sintaxe correta para um atributo booleano?**

- [x] `<input type="checkbox" checked>`
- [ ] `<input type="checkbox" checked="on">`
- [ ] `<input type="checkbox" checked="off">`
- [ ] `<input type="checkbox" checked="isChecked">`
