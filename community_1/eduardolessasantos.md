# Olá meu nome é Eduardo Lessa e vou mostrar um pouco dos principais comandos de estilização do CSS


---

# CSS Cheat Sheet 🧠

Uma referência rápida com as propriedades mais usadas no CSS. Ideal para consultas rápidas durante o desenvolvimento.

---

## 📦 Layout

### Display
```css
display: block;        /* Elemento em bloco */
display: inline;       /* Elemento em linha */
display: inline-block; /* Misto: inline + block */
display: flex;         /* Flexbox container */
display: grid;         /* Grid container */
```

### Position
```css
position: static;     /* Padrão */
position: relative;   /* Relativo à posição original */
position: absolute;   /* Relativo ao ancestral posicionado */
position: fixed;      /* Relativo à viewport */
position: sticky;     /* Fixa ao rolar até certo ponto */
top, right, bottom, left
z-index: 10;
```

### Box Model
```css
width: 100px;
height: 50px;
padding: 10px;     /* Espaço interno */
margin: 20px;      /* Espaço externo */
border: 1px solid #000;

box-sizing: content-box;  /* Padrão */
box-sizing: border-box;   /* Inclui padding e border no tamanho total */
```

---

## 🎨 Estilização

### Cores
```css
color: #333;
background-color: lightblue;
opacity: 0.8;
```

### Fontes
```css
font-family: Arial, sans-serif;
font-size: 16px;
font-weight: bold; /* normal | bold | 100-900 */
font-style: italic;
text-align: center;
text-decoration: underline;
line-height: 1.5;
letter-spacing: 1px;
```

### Bordas e Arredondamento
```css
border: 1px solid #ccc;
border-radius: 8px;
```

### Sombras
```css
box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
text-shadow: 1px 1px 2px #000;
```

---

## 🚀 Flexbox

```css
display: flex;
flex-direction: row | column;
justify-content: flex-start | center | space-between;
align-items: stretch | center | flex-end;
gap: 10px;
```

---

## 🔲 Grid

```css
display: grid;
grid-template-columns: repeat(3, 1fr);
grid-template-rows: 100px auto;
gap: 10px;
grid-column: 1 / 3;
grid-row: 2 / 4;
```

---

## 🖱️ Interatividade

```css
cursor: pointer;
pointer-events: none;
user-select: none;
```

### Hover & States
```css
a:hover {
  color: red;
}
button:disabled {
  opacity: 0.5;
}
```

---

## 📱 Responsivo

```css
@media (max-width: 768px) {
  body {
    font-size: 14px;
  }
}
```

---

## 🌐 Outros úteis

```css
overflow: hidden | auto | scroll;
visibility: hidden | visible;
white-space: nowrap;
text-overflow: ellipsis;
transition: all 0.3s ease;
```

---

## 📚 Dica Final

Use ferramentas como [https://developer.mozilla.org/](https://developer.mozilla.org/) para documentação oficial e exemplos interativos.

---
