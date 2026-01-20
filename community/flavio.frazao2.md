# Olá! É uma satisfação conhece-ló, me chamo Flavio Frazão.

### Esse readme serve para você me conhecer e saber quais os principais projetos que trabalho, minha expertise profissional e quais as novas tecnologias que estou me desenvolvendo. 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/flaviofrazao/) [![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/channels/@flaviofrazao/) [![Instagram](https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/flaviofrazao/) [![Gmail](https://img.shields.io/badge/Gmail-333333?style=for-the-badge&logo=gmail&logoColor=red)](mailto:flaviodevfrazao@gmail.com)

## Atualmente trabalho em uma empresa de tecnologia na área de infraestrutura. Atendo chamados de nível 2 e 3 para switches, servidores, datacenters, sistemas operacionais e firewall.

## Segue abaixo as tecnologias que conheço:

### Switches 

![Cisco](https://img.shields.io/badge/cisco-%23049fd9.svg?style=for-the-badge&logo=cisco&logoColor=black)

### Sistemas Operacionais

![Cent OS](https://img.shields.io/badge/cent%20os-002260?style=for-the-badge&logo=centos&logoColor=F0F0F0) ![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Pop!\_OS](https://img.shields.io/badge/Pop!_OS-48B9C7?style=for-the-badge&logo=Pop!_OS&logoColor=white) ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## Principais projetos que atuo:

### Atualmente desenvolvo projetos usando o GLPI que é um sistema de chamados internos e externos com área para inventário de empresas monitorando do smartphone ao servidor em nuvem. A empresa que represento integra o GLPI a um CRM que controla os chamados por ferramentas como Teams, Whatsapp e o próprio sistema CRM. 

## Demonstração

### Alguns scripts criados por mim:

## 1 - Sincronização de arquivos entre servidores

```bash
  #!/bin/bash

# Executando o comando rsync
rsync -avz --delete -e 'ssh -p 7654' /var/www/html/glpi/* user@xx.xx.xx.xx:/var/www/html/glpi
```
### Variáveis do script

`rsync` comando usado para realizar o sync

`-avz` a - compactação / v - verbose / z - analise

`--delete` deleta arquivos no destino que não estão mais na origem.

`-e 'ssh -p 7654'` força utilização da porta 7654 


## 2 - Envio de mensagem de email caso a replicação do banco de dados para de funcionar

```bash
#!/bin/bash

# Definir variáveis para credenciais MySQL
MYSQL_USER="user.root"
MYSQL_PASSWORD="pwd.root"
MYSQL_HOST="localhost"

# Verificar o status da replicação
SLAVE_STATUS=$(mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -h$MYSQL_HOST -e "SHOW SLAVE STATUS\G")

# Checar status da replicação (Slave_IO_Running e Slave_SQL_Running)
IO_RUNNING=$(echo "$SLAVE_STATUS" | grep "Slave_IO_Running: No")
SQL_RUNNING=$(echo "$SLAVE_STATUS" | grep "Slave_SQL_Running: No")

# Enviar notificação por e-mail apenas se houver erro na replicação
if [ "$IO_RUNNING" ] || [ "$SQL_RUNNING" ]; then
    echo -e "Subject: Falha na Replicação do banco Contrato DPZ MySQL\n\nA replicação falhou no servidor $(hostname). Verifique imediatamente." | ssmtp flavio.frazao@voxdatati.com.br
fi