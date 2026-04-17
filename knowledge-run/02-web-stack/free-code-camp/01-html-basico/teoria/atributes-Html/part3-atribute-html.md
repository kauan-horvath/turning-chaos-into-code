# Certificação de Design Responsivo para a Web

## Entendendo o Boilerplate HTML

### O que é UTF-8?

**UTF-8** (_UCS Transformation Format 8_) é o padrão de codificação de caracteres mais utilizado na web. Ele funciona como um "tradutor" que permite aos computadores armazenar e exibir texto corretamente.

#### Como funciona a Codificação?

Os computadores não entendem letras ou símbolos diretamente; eles processam dados em **bytes** (unidades que consistem em **8 bits**). A codificação é o método de mapear esses dados binários para caracteres reais.

- **Unicode:** O UTF-8 suporta praticamente todos os sistemas de escrita, idiomas e símbolos técnicos do mundo.
- **Importância:** Sem ele, caracteres acentuados (como o "é" em _Café_) ou símbolos especiais podem aparecer como códigos quebrados ou interrogações.

---

### Implementação no HTML

Para garantir que seu site exiba qualquer idioma corretamente, você deve incluir o elemento `<meta>` com o atributo `charset` dentro do `<head>`.

**Sintaxe:**

```html
<meta charset="UTF-8" />
```

**Exemplo Completo:**

```html
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8" />
    <title>Exemplo de UTF-8</title>
  </head>
  <body>
    <p>Café fresquinho</p>
  </body>
</html>
```

---

### Questões de Revisão

**1. Qual atributo é usado para definir a codificação de caracteres UTF-8 para documentos HTML?**

- [ ] `pattern`
- [ ] `content`
- [x] `charset`
- [ ] `lang`

**2. O que é codificação de caracteres?**

- [x] Um método que os computadores usam para armazenar caracteres como dados.
- [ ] Uma forma de comprimir arquivos de texto.
- [ ] Ele determina a fonte usada para exibir texto em uma tela.
- [ ] Refere-se ao processo de converter linguagem falada em texto escrito.

**3. Quantos bits existem dentro de um byte?**

- [ ] 1
- [ ] 33
- [ ] 7
- [x] 8
