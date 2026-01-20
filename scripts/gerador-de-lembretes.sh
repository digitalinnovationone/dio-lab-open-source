#!/bin/bash

lembretes_file="lembretes.txt"

exibir_lembrete() {
    notify-send "Lembrete!" "$1"
    zenity --info --title="Lembrete" --text="$1" --width=200 --height=100 --timeout=10
    paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga
}

salvar_lembrete() {
    echo "$1;$2" >> "$lembretes_file"
}

limpar_lembretes_passados() {
    while IFS=';' read -r horario mensagem; do
        hora_atual=$(date +%H:%M)
        minutos_atual=$(date -d "$hora_atual" +%s)
        minutos_lembrete=$(date -d "$horario" +%s)
        tempo_restante=$((minutos_lembrete - minutos_atual))

        if [ $tempo_restante -le 0 ]; then
            sed -i "/$horario;$mensagem/d" "$lembretes_file"
            echo "Lembrete '$mensagem' ($horario) removido do arquivo."
        fi
    done < "$lembretes_file"
}

verificar_lembretes() {
    while IFS=';' read -r horario mensagem; do
        hora_atual=$(date +%H:%M)
        minutos_atual=$(date -d "$hora_atual" +%s)
        minutos_lembrete=$(date -d "$horario" +%s)
        tempo_restante=$((minutos_lembrete - minutos_atual))

        if [ $tempo_restante -le 0 ]; then
            echo "O horário do lembrete '$mensagem' ($horario) já passou."
        else
            (sleep $tempo_restante && exibir_lembrete "$mensagem") &
            echo "Lembrete definido para '$mensagem' às $horario"
        fi
    done < "$lembretes_file"
}

if [ ! -f "$lembretes_file" ]; then
    touch "$lembretes_file"
fi

if [ $# -eq 0 ]; then
    limpar_lembretes_passados
    verificar_lembretes
    exit 0
fi

if [ $# -lt 2 ]; then
    echo "Uso: $0 <horário no formato HH:MM> <mensagem>"
    exit 1
fi

horario="$1"
mensagem="$2"

hora_atual=$(date +%H:%M)
minutos_atual=$(date -d "$hora_atual" +%s)
minutos_lembrete=$(date -d "$horario" +%s)
tempo_restante=$((minutos_lembrete - minutos_atual))

if [ $tempo_restante -le 0 ]; then
    echo "O horário do lembrete já passou."
    exit 1
fi

salvar_lembrete "$horario" "$mensagem"
echo "Lembrete adicionado para '$mensagem' às $horario"

limpar_lembretes_passados
verificar_lembretes
exit 0
