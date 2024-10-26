# Anarkus

<p align="center">
   Meu nome é Renato e estou começando neste mundo de desenvolvimento e dados. 
<p align="center">
   Não sei o que voce irá encontrar meu github de interessante agora, mas com certeza no futuro terá projetos voltados para desenvolvimento de programas e base de dados, bem como analises, pois quero muito evoluir nesta área.
<p align="center">
Este é o primeiro bootcamp, e estou adorando as aulas. 
    Atualmente, estou no segundo semestre de analise de dados, contudo quero poder desenvolver e aprimorar conhecimentos dentro de uma empresa, se possível.
<p align="center">
Obrigado pela atençao e fique livre para me indicar direção, caminhos ou principalmente oportunidades! 
</p>
<br>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cronômetro</title>
</head>
<body>
    <h1>Cronômetro</h1>
    <div id="cronometro">00:00:00</div>
    <button onclick="iniciarCronometro()">Iniciar</button>
    <button onclick="pararCronometro()">Parar</button>
    <button onclick="zerarCronometro()">Zerar</button>
    
    <script>
        let cronometro;
        let segundos = 0;
        let minutos = 0;
        let horas = 0;
        
        function atualizarCronometro() {
            segundos++;
            if (segundos == 60) {
                segundos = 0;
                minutos++;
                if (minutos == 60) {
                    minutos = 0;
                    horas++;
                }
            }
            const tempoFormatado = `${horas.toString().padStart(2, '0')}:${minutos.toString().padStart(2, '0')}:${segundos.toString().padStart(2, '0')}`;
            document.getElementById("cronometro").textContent = tempoFormatado;
        }
        
        function iniciarCronometro() {
            cronometro = setInterval(atualizarCronometro, 1000);
        }
        
        function pararCronometro() {
            clearInterval(cronometro);
        }
        
        function zerarCronometro() {
            clearInterval(cronometro);
            segundos = 0;
            minutos = 0;
            horas = 0;
            document.getElementById("cronometro").textContent = "00:00:00";
        }
    </script>
</body>
</html>

