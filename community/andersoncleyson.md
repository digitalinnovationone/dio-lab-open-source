<head>
    <style>
        body {
            font-family: 'Courier New', monospace;
            background-color: black;
            color: white;
            padding: 20px;
        }
        .typing-container {
            font-family: 'Courier New', monospace;
            display: flex;
            flex-direction: column;
        }
        .line {
            white-space: nowrap;
            overflow: hidden;
            border-right: 2px solid white;
            font-size: 14px;
            width: 0;
        }
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }
        @keyframes blink {
            50% { border-color: transparent; }
        }
        .line::after {
            content: "";
            display: inline-block;
            width: 8px;
            height: 16px;
            background-color: white;
            animation: blink 0.7s infinite;
        }
        .line:nth-child(1) {
            animation: typing 3s steps(30, end) forwards;
        }
        .line:nth-child(2) {
            animation: typing 3s steps(30, end) forwards;
            animation-delay: 2.2s;
        }
        .line:nth-child(3) {
            animation: typing 3s steps(30, end) forwards;
            animation-delay: 4.4s;
        }
        .line:nth-child(4) {
            animation: typing 3s steps(30, end) forwards;
            animation-delay: 6.6s;
        }
        .line:nth-child(5) {
            animation: typing 1s steps(30, end) forwards;
            animation-delay: 7.0s;
        }
        .line:nth-child(6) {
            animation: typing 3s steps(30, end) forwards;
            animation-delay: 8.0s;
        }
        .line:nth-child(7) {
            animation: typing 3s steps(30, end) forwards;
            animation-delay: 8.5s;
        }
        .line:nth-child(8) {
            animation: typing 3s steps(30, end) forwards;
            animation-delay: 9.5s;
        }
        .line:nth-child(9) {
            animation: typing 3s steps(30, end) forwards;
            animation-delay: 10.5s;
        }
        .line:nth-child(10) {
            animation: typing 3s steps(30, end) forwards;
            animation-delay: 11.5s;
        }
        .line:nth-child(11) {
            animation: typing 3s steps(30, end) forwards;
            animation-delay: 12.0s;
        }
        .line:nth-child(11) {
            animation: typing 3s steps(30, end) forwards;
            animation-delay: 12.0s;
        }
    </style>
</head>
<body>

<div class="typing-container">
    <div class="line">Olá. amigo. Me chamo Anderson.</div>
    <div class="line">Sou formado em Análise e Desenvolvimento de Sistemas.</div>
    <div class="line">Atualmente trabalho na área da segurança da informação,</div>
    <div class="line">mas pretendo migrar para Desenvolvimento Back-End.</div>
    <div class="line"></div>
    <div class="line">Linguagens:</div>
    <div class="line">> JAVA</div>
    <div class="line">> GOLANG</div>
    <div class="line">> PYTHON</div>
    <div class="line"></div>
    <div class="line">Me adiciona no <a href="https://www.linkedin.com/in/anderson-cleyson/">Linkedin</a></div>

</div>

</body>
</html>
