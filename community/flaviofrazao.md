# Olá! Me chamo Flavio Frazão. 

Esse é um readme básico criado com a intenção de aprendizado para futuros readm's dos meus projetos.

## Melhor forma de falar comigo:

 - [Linkdedin](https://www.linkedin.com/in/flaviofrazao/)
 - [Instagram](https://www.instagram.com/)
 - [Meus projetos no GitHub](https://github.com/flaviodevfrazao)

## Demonstração

Alguns scripts criados por mim:

1 - Sincronização de arquivos entre servidores

```bash
  #!/bin/bash

# Executando o comando rsync
rsync -avz --delete -e 'ssh -p 7654' /var/www/html/glpi/* user@xx.xx.xx.xx:/var/www/html/glpi
```

## Variáveis do script

`rsync` comando usado para realizar o sync

`-avz` a - compactação / v - verbose / z - analise

`--delete` deleta arquivos no destino que não estão mais na origem.

`-e 'ssh -p 7654'` força utilização da porta 7654 