# Custom Badges
<table>
  <tr>
    <td>
      Gerador
    </td>
    <td>
       <a href="https://custom-icon-badges.demolab.com/">
          custom-icon-badges.demolab
       </a>
    </td>
  </tr>
  <tr>
    <td>
      Fonte
    </td>
    <td>
       <a href="https://github.com/DenverCoder1/custom-icon-badges?tab=readme-ov-file">
          DenverCoder1/custom-icon-badges
       </a>
    </td>
  </tr>
</table>

## Como criar uma badge com ícone personalizado

Nos baseamos na URL e parâmetros do [Shields.io](https://shields.io/badges), com a customização do [Custom Icon Badges DemoLab](https://custom-icon-badges.demolab.com/)

1. Substitua a seção ``img.shields.io`` no início da URL por ``custom-icon-badges.demolab.com``
````
https://custom-icon-badges.demolab.com/badge/
````
2. Você pode usar algum ícone preexistente [dentre esses](https://github.com/DenverCoder1/custom-icon-badges?tab=readme-ov-file#%EF%B8%8F-existing-logos)
3. Ou customizar [aqui](https://custom-icon-badges.demolab.com/)
   - carregue a imagem da logo que será usada como ícone
   - para salvar a imagem do ícone nesse site, você deve indicar o _slug_ (nome da logo)
   - depois de enviado, o ícone já estará disponível para usar na badge a partir do nome _slug_
  
     
**Exemplo:**


![Customização de Icon do DIO](https://github.com/claclaben10/dio-lab-open-source/assets/148786252/b0e530fd-ffc1-4f3a-bb07-5d51d508e097)


4. Basta voltar agora para a URL e acrescentá-lo junto aos parâmetros:
````
https://custom-icon-badges.demolab.com/badge/text-color.svg?logo=slug
````
- Substitua ``text`` pelo texto que aparecerá na badge, ``color`` pela cor da badge e ``slug`` pelo nome da logo
  - **Exemplo**: ![Badge DIO](https://custom-icon-badges.demolab.com/badge/DIO-black.svg?logo=dio1) ``https://custom-icon-badges.demolab.com/badge/DIO-black.svg?logo=dio1``
- Você ainda pode personalizar a badge mudando a cor em ``color`` ou acrescentando ``style`` no final.
  - **Exemplo**: ``DIO-blue.svg?logo=dio1&style=for-the-badge``

5. Para inserir a badge no seu arquivo README.md, você deverá usar a formatação Markdown para imagens:
   - ``![Título da Imagem](URL)``

| **Exemplo**: | **Formatação** |
| :----------: | :------------: |
| ![Badge DIO](https://custom-icon-badges.demolab.com/badge/DIO-black.svg?logo=dio1) | ````![Badge DIO](https://custom-icon-badges.demolab.com/badge/DIO-black.svg?logo=dio1)```` |
| ![Badge DIO](https://custom-icon-badges.demolab.com/badge/DIO-black.svg?logo=dio1&style=for-the-badge) | ````![Badge DIO](https://custom-icon-badges.demolab.com/badge/DIO-black.svg?logo=dio1&style=for-the-badge)```` |
| ![Badge DIO](https://custom-icon-badges.demolab.com/badge/DIO-blue.svg?logo=dio) | ````![Badge DIO](https://custom-icon-badges.demolab.com/badge/DIO-blue.svg?logo=dio)````|
| ![Badge DIO](https://custom-icon-badges.demolab.com/badge/DIO-blue.svg?logo=dio&style=for-the-badge) | ````![Badge DIO](https://custom-icon-badges.demolab.com/badge/DIO-blue.svg?logo=dio&style=for-the-badge)````|

6. Por fim, acrescente colchetes no início e fim da badge + URL (link do seu perfil) em outro parênteses:
   - ``[![Badge](https://custom-icon-badges.demolab.com/badge/DIO-black.svg?logo=dio1)](URL_do_perfil)``
  
   - **Exemplo**:
   [![Badge DIO](https://custom-icon-badges.demolab.com/badge/DIO-black.svg?logo=dio1&style=for-the-badge)](https://www.dio.me/users/elidianaandrade)
````
[![Badge DIO](https://custom-icon-badges.demolab.com/badge/DIO-black.svg?logo=dio1&style=for-the-badge)](https://www.dio.me/users/elidianaandrade)
````

## Recursos Úteis

- Leia o README.md do repositório [Custom Icon Badges by DenverCoder1](https://github.com/DenverCoder1/custom-icon-badges)
- Consulte os parâmetros para customizar sua badge no [Shields.io](https://img.shields.io/badges/static-badge)
- [Custom Icon Badges DemoLab](https://custom-icon-badges.demolab.com/)
