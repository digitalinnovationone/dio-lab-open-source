<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matrix Effect</title>
    <style>
        body {
            background-color: black;
            color: #00ff00;
            font-family: monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
            margin: 0;
        }

        .matrix {
            display: inline-block;
            white-space: nowrap;
            overflow: hidden;
            animation: typing 2s steps(20) infinite, blink 0.5s step-end infinite alternate;
        }

        @keyframes typing {
            from {
                width: 0;
            }
            to {
                width: 100%;
            }
        }

        @keyframes blink {
            50% {
                border-right: 2px solid #00ff00;
            }
        }
    </style>
</head>
<body>
    <div class="matrix">Edgar Dikenge</div>
</body>
</html>
