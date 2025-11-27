# Olá devs 👋

Bem vindo(a) ao meu perfil.

## Mais sobre mim


```js
class Developer {
  constructor() {
    this.#set();
  }
  #props = {
    name: "",
    acknowledgements: "",
    skills: {
      languages: [],
      frameworks: [],
      primarySkillset: [],
    },
  };

  get() {
    return { props: this.#props };
  }
  #set() {
    this.#props.name = "Marco Damasceno";
    this.#props.acknowledgements = "Developer Web";
    this.#props.skills.languages = ["C#","Javascript"];
    this.#props.skills.frameworks = ["Angular", "React", "Next", "Vue"];
    this.#props.skills.primarySkillset = [
      "Comunicação,Resolução de problemas,Adaptabilidade,Proatividade,Foco,Empatia,Criatividade",
    ];
  }
}

class Person extends Developer {
  constructor() {
    super();

    const attributes = this.get().props;

    return attributes;
  }
}

const marco = new Person();
```

<img align="right" width="300" src="https://i.pinimg.com/originals/21/11/61/21116158daaeb1459b4ec0758505e1ad.gif" />


## Linguagens e ferramentas

<img src="https://skillicons.dev/icons?i=git,js,mysql,mongodb,angular,react,vue,tailwind,next,sass,vscode" />

## Status

<a href="https://github.com/encodedbrain">
 <img align="center" src="https://github-readme-stats.vercel.app/api?username=encodedbrain&show_icons=true&theme=dracula&line_height=27" alt="marco damasceno github stats"/>
</a>

[linkedin]: https://www.linkedin.com/in/marcodmc/

<br>

## Rede sociais
👔 [LinkedIn][linkedin]

## Contato


[marco damaceno](mailto:marcodmc0101@gmail.com?subject=[GitHub]%20Source%20Han%20Sans)
