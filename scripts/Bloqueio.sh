#!/bin/bash

#finaliza o plasmashell

killall plasmashell &>/dev/null

# Verifica a conectividade com a internet antes de iniciar
if ! ping -c 4 127.0.0.1; then
    echo "Sem conectividade com a internet. Continuando mesmo assim..."
fi

# Verifica se o processo "plasmashell" está em execução. Se não estiver, inicia-o.
plasmashell &>/dev/null &


# Nome da aplicação a ser monitorada (substitua pelo nome correto)
APP_NAME="sunshine"

# Comando para bloquear a tela (verifique o correto para o seu sistema)
LOCK_SCREEN_CMD="xdg-screensaver lock"

# Verifica se o comando para bloquear a tela está disponível
if ! command -v ${LOCK_SCREEN_CMD%% *} &>/dev/null; then
    echo "Comando para bloquear a tela não encontrado: $LOCK_SCREEN_CMD"
    exit 1
fi

# Aguarda a inicialização da aplicação
while ! pgrep -x "$APP_NAME" > /dev/null; do
    sleep 1
done

# Bloqueia a tela após a inicialização da aplicação
$LOCK_SCREEN_CMD

# Encerra o script após o bloqueio
exit 0
