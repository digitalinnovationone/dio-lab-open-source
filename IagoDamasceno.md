
# Dicas e Truques para Projetos Fullstack com C#, Java codando no VSCode

## Apresentação

Me chamo Iago, atualmente trabalho como administrativo e curso Engenharia da computação, busco conhecimento para me aprimorar e mudar minha área de atuação.

Meu portifólio é bem simples estou começando agora.

- [GitHub](https://github.com/IagoDamasceno)

Envio algumas sugestões para melhorar a produtividade no VSCode e seu entendimento sobre as linguagens usadas no bootcamp.


## Dicas para C#

1. **Utilize `var` com moderação**: Embora o uso de `var` possa tornar o código mais limpo, é importante usá-lo com cuidado para evitar perda de clareza sobre o tipo da variável.

2. **Async e Await**: Aproveite as palavras-chave `async` e `await` para escrever código assíncrono de forma mais simples e eficiente, melhorando a responsividade da aplicação.

3. **Null-conditional Operators**: Use o operador `?.` para evitar exceções `NullReferenceException` ao acessar membros de objetos que podem ser nulos.

   ```csharp
   string name = person?.Name;
    ```
    ```
    Console.WriteLine($"O nome é {name}");
    ```
    
## Dicas para Java

### Streams API: 
Aproveite a API de Streams introduzida no Java 8 para manipulação eficiente de coleções, tornando o código mais expressivo e conciso.

```
List<String> names = users.stream()
                          .filter(u -> u.getAge() > 18)
                          .map(User::getName)
                          .collect(Collectors.toList());
```

### Lambdas e Functional Interfaces: 
Utilize lambdas e interfaces funcionais para escrever código mais limpo e evitar boilerplate.

```
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
names.forEach(name -> System.out.println(name));
```
### Optional Class: 
Utilize a classe Optional para lidar de forma mais segura com valores que podem ser nulos.

```
Optional<User> user = findUserById(id);
user.ifPresent(u -> System.out.println(u.getName()));
```
### Pattern Matching (Java 16+): 
Use o pattern matching para simplificar o código quando trabalhar com instâncias de tipos variados.

```
if (obj instanceof Strings) {
    System.out.println(s.toLowerCase());
}
```


## Dicas para VSCode
### Atalhos de Teclado:

#### Ctrl + P: Rápido acesso a arquivos abertos ou recentes.
#### Ctrl + Shift + P: Acessa a paleta de comandos para executar comandos rapidamente.
#### Ctrl + /: Comentar ou descomentar linhas de código.

### Extensões Úteis:

#### C#: Suporta funcionalidades como IntelliSense, debugging e formatação de código.
#### Java Extension Pack: Inclui suporte completo para desenvolvimento Java no VSCode, com funcionalidades como IntelliSense, linting e debugging.

### Configurações de Formatação Automática:

Defina a formatação automática ao salvar para manter o código limpo e padronizado. Adicione isso ao seu settings.json:

```
"editor.formatOnSave": true,
"files.autoSave": "afterDelay"
```
### Snippets Personalizados:

#### Crie snippets de código para reutilização de blocos de código frequentes.
 Use o comando Preferences: Configure User Snippets na paleta de comandos para configurar.

##  Espero que lhe ajude a melhorar sua produtividade.
