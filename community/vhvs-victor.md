<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me</title>
    <style>
        *{
    padding: 0px;
    margin: 0px;
}

html{
    background-color: #F4F2EE;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

body{
    background-color: rgb(255, 255, 255);
    width: 700px;
    height: 550px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 25px;
    box-shadow: 0px 0px 6px 0px rgb(216, 216, 216);
}

.div_background{
    background-image: url(https://media.licdn.com/dms/image/D4D16AQFWd5jnO4Xftg/profile-displaybackgroundimage-shrink_350_1400/0/1719841270273?e=1725494400&v=beta&t=_0Djg5BXETeqwKFVSM4igON3hhzUPpv__EgNWTePSFE);
    background-size: cover;
    background-repeat: repeat;
    background-position: center left;
    width: 100%;
    height: 200px;
    border-radius: 25px 25px 0px 0px;
    
}

.div_profile{
    background-image: url(https://media.licdn.com/dms/image/D4D03AQFXl5O6OB957Q/profile-displayphoto-shrink_200_200/0/1719754902105?e=1725494400&v=beta&t=0xuMg3efIgjAlvFaT3ng-U8Zpr9e7cLWWWSdu3B65Vg);
    background-size: cover;
    width: 180px;
    height: 180px;
    border-radius: 50%;
    position: relative;
    top: 40%; 
    left: 8%;
    border: solid 5px white;
}

main.section_apresentation{
    padding: 0px 25px;
}

main.section_apresentation p{
    margin-top: -10px;
}

.section_primary{
    margin-top: 70px;
}

.section_primary .biographi{
    font-size: 1.1em;
    margin-bottom: 10px;
}

.about_me{
    font-size: 0.9em;
    padding: 10px;
}

.buttons{
    display: flex;
    margin-top: 25px;
    justify-content: center;
}

.buttons a{
    text-decoration: none;
    color: white;
    display: block;
    text-align: center;
}

.buttons .profile_linkedin{
    background-color: #004182;
    width: 150px;
    height: 25px;
}

.buttons .profile_dio{
    background-color: #5158A0;
    width: 150px;
    margin-left: 3px;
}

.buttons .profile_instagram{
    background-color: #C62E7C;
    width: 150px;
    margin-left: 3px;
}

.buttons .profile_facebook{
    background-color: #0866FF;
    width: 150px;
    margin-left: 3px;
}

h1, h2{
    color: rgb(71, 71, 71);
}

p{
    color: rgb(143, 141, 141);
}

p.create_by{
    color: gray;
    font-size: 0.6em;
    text-align: center;
    margin-top: 15px;
}

    </style>
</head>
<body>
    <header>
        <div class="div_background">
            <div class="div_profile">
                <!-- <img src="imagens/photo_2024-06-30_10-39-08.jpg" alt="Imagem-de-perfil" width="160px" height="160px"> -->
            </div>
        </div>
    </header>
    <main class="section_apresentation">
        <section class="section_primary">
            <h1 class="username">Victor Viana</h1>
            <h2 class="biographi"><strong>Engenheiro de Software em Formação | Desenvolvedor Front-end</strong></h2>
        </section>
        <section class="section_experience">
            <p class="about_me">Olá! Sou um profissional com mais de 5 anos de experiência na área comercial, atualmente em transição de carreira para a área de tecnologia enquanto curso Engenharia de Software.</p>
            <p class="about_me">Busco novos desafios na área de tecnologia, especialmente no desenvolvimento front-end. Possuo sólida experiência em <strong>HTML</strong>, <strong>CSS</strong>, <strong>JavaScript</strong> e<strong> Bootstrap</strong>, além de conhecimentos em <strong>SQL Server</strong>, <strong>TypeScript</strong>, <strong>Node.js</strong> e <strong>React</strong>.</p>
        </section>
        <section class="buttons">
            <div class="profile_linkedin">
                <a href="https://www.linkedin.com/in/victor-hugo-viana-da-silva" target="_blank">Linkedin</a>
            </div>
            <div class="profile_dio">
                <a href="https://www.dio.me/users/vhvs_victor" target="_blank">Curso DIO</a>
            </div>
            <div class="profile_instagram">
                <a href="https://www.instagram.com/vhvs.victor/" target="_blank">Instagram</a>
            </div>
            <div class="profile_facebook">
                <a href="https://www.facebook.com/victor.viana.73113/" target="_blank">Facebook</a>
            </div>
        </section>
    </main>
    <footer>
        <p class="create_by"> Create By: Victor Viana | Escola DIO - Desenvolvimento Front-end</p>
    </footer>
</body>
</html>