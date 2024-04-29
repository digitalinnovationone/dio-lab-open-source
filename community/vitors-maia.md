<style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');

    * {
        font-family: "Roboto", sans-serif;
    }

    .header {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .gradient {
        position: relative;
        width: 170px;
        height: 170px;
        overflow: hidden;
        border: 5px solid #47017F;
        border-radius: 50%;
    }

    .header-img {
        width: 170px;
        height: 170px;
    }

   .gradient::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: radial-gradient(circle, rgba(0, 0, 0, 0) 50%, rgba(0, 0, 0, .9)70%);
        background-size: cover;
        background-position: center;
        mix-blend-mode: multiply;
    }

     .header-name {
        padding: 10px;
        border: none;
     }

    .header-name a{
        color: #47017F;
        font-size: 40px;
        text-shadow: 3px 3px 5px black;
        transition: .4s;
    }

    .header-name a:hover {
        text-decoration: none;
        font-size: 43px;
    }

    li a {
        color: #ffffff;
        text-decoration: underline;
    }

    li a:hover {
        color: #8704f3;
    }

    h2 {
        padding-left: 10px;
        border: none;
    }

    .border {
        border-left: 5px solid #47017F;
    }

    .address {
        display: flex;
        gap: 40px;
        list-style-type: none;
    }

     .address a {
        font-size: 15px;
     }

     .address-link {
        display: flex;
        align-items: center;
        gap: 5px;
    }

     .ico {
        width: 20px;
     }
</style>

<div class="header">
    <div class="gradient">
        <img class="header-img" src="https://i.imgur.com/1gV07Yf.jpeg" alt="Vitor Maia">
    </div>
        <h1 class="header-name"><a href="https://github.com/vitors-maia">Vitor Maia</a></h1>
</div>

<main class="main">
    <div class="border">
        <h2>Sobre:</h2>
    </div>
    <p>Olá, meu nome é Vitor. Tenho 24 anos e sou natural de Fortaleza, Ceará.</p>
    <p>Profissionalmente, dedico-me à área de desenvolvimento web, com especialização no Front-end. Tenho grande interesse em criar interfaces digitais cativantes, buscando sempre proporcionar experiências de usuário excepcionais.</p>
    <p>Estudante e entusiasta das linguagens de marcação e programação:</p>
    <ul>
        <li><a href="https://www.w3schools.com/html/default.asp">HTML</a></li>
        <li><a href="https://www.w3schools.com/css/default.asp">CSS</a></li>
        <li><a href="https://www.w3schools.com/js/default.asp">JavaScript</a></li>
        <li><a href="https://www.w3schools.com/java/default.asp">Java</a></li>   
    </ul>
    <div class="border">
        <h2>Contatos:</h2>
    </div>
    <address>
        <ul class="address">
            <li><div class="address-link"><img class="ico" src="https://cdn.iconscout.com/icon/free/png-256/free-instagram-216-721958.png" alt="Instagram"> <a href="https://www.instagram.com/vitors_maia/">Instagram</a></div></li>
            <li><div class="address-link"><img class="ico" src="https://upload.wikimedia.org/wikipedia/commons/9/90/Wbseries_linkdin.png?20211115150153" alt="LinkedIn"> <a href="www.linkedin.com/in/vitors-maia">LinkedIn</a></div></li>
            <li><div class="address-link"><img class="ico" src="https://cdn.iconscout.com/icon/free/png-256/free-github-159-721954.png" alt="GitHub"> <a href="https://www.instagram.com/vitors_maia/">GitHub</a></div></li>
        </ul>
    </address>
</main>

![Vitor GitHub stats](https://github-readme-stats.vercel.app/api?username=vitors-maia&show_icons=true&theme=tokyonight)