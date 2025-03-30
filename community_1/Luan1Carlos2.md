#### ler arquivo começando do final e atualizando sempre, sem o "+F" apenas vai para o final
>less +GF
#### contar quantidade de linhas do stdout  ou arquivo
>wc -l
#### listar processos em arvore
>ps axjf
#### uso de pasta
>ncdu
#### retorna apenas a segunda coluna de uma saida de dados
>awk '{print $2}'
#### mostra se é necessário reiniciar  algum serviço ou realizar reboot
>sudo dnf needs-restarting -sr
#### mostra lista de IPs em interfaces ativas disponíveis
>ip -br a | grep "UP" | awk '{print $3}' | sed 's/\/.*//'
#### mostra IP da interface da rota default
>ip route | awk 'NR==1{print $9}'
#### criar usuário
>useradd -m -s /bin/bash usuario
#### adiciona conteudo no final de arquivo
>sed -i '$aconteudo' /pasta/arquivo
#### cresce o xfs pra o tamanho máximo
>xfs_growfs /dev/algo -d
#### listar erros de selinux
>journalctl -t setroubleshoot
#### substitui todas as ocorrências em todos os arquivos
>sed -i -e 's/a/b/g' /foo/bar/*.conf
#### 20 maiores arquivos/pastas da pasta atual
>du --max-depth=1 2> /dev/null | sort -n -r | head -n20
#### salvar vim com sudo
>w !sudo tee %
#### converter ova para qcow2
>virt-v2v -i ova PNET_4.2.10.ova -o libvirt -of qcow2
#### console a partir do shell linux
>sudo cu -s 115200 -l /dev/ttyUSB0 --nostop --parity=none
#### Criar image qcow2 usando outra como base
>qemu-img create -fqcow2 -F qcow2 -b ubuntu.qcow2 ub2tu.qcow2
#### Forçar uso de certo tipo de chave de troca no ssh
>ssh -oKexAlgorithms=diffie-hellman-group-exchange-sha1 root@0.0.0.0
#### Forçar uso de certo tipo de algoritimo de chave no ssh
>ssh -oHostKeyAlgorithms=ssh-dss root@0.0.0.0
### Converter imagem de disco usando qemu-img
>qemu-img convert -f qcow2 -O qcow2 /var/lib/libvirt/images/win2k19-en.qcow2 /home/publico/destino.qcow2
### Apagar arquivos mais velhos que 30 dias
>find -maxdepth 1 -mtime +30 -exec rm -rf {} +;
### Redimensionar imagem
>qemu-img resize focal-server-cloudimg-amd64-disk-kvm.img 50g
### Sobrescrever local pelo remoto no git
>git fetch --prune origin  
>git reset --hard origin/main 
>git clean -f -d
