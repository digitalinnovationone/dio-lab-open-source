<div class="container">

  <div class="card">
        <div class="card-wrapper">
        <p>Marcelo Wilborn</p>
        <a href="https://github.com/marcelo-wilborn">
            <div class="github">
                    <img class="githubImg" src="https://img.freepik.com/icones-gratis/github_318-566791.jpg?t=st=1692150035~exp=1692150635~hmac=36682407c69a89cdf5e3ccdac0b4ac7a53af551adafefb066a825d903d68ccf7" alt="github img">
                    <p>Github</p>
            </div>
            </a>
            <a href="https://www.linkedin.com/in/marcelo-wilborn-213a78238/">
                <div class="linkedin">
                    <img id="linkedinImg" src="https://cdn.icon-icons.com/icons2/2248/PNG/512/linkedin_icon_135436.png" alt="linkedin img">
                    <p>Linkedin</p>
                </div>
            </a>
    </div>
  </div>
</div>

<style>
   * {
    margin: 0;
}
a {
    text-decoration: none;
    
}
  a:hover {
    text-decoration: none;
  }

body {
    height: 200vh;
}

.container {
    position: fixed;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    background: linear-gradient(to bottom, rgb(72, 57, 57), rgb(71, 62, 62), rgb(72, 57, 57));
}

.container .card {
    width: 500px;
    height: 600px;
    border: 3px solid black;
    background-image: url('https://encurtador.com.br/bvBNX');
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    display: flex;
    justify-content: center;
    filter: grayscale(0.7);
    color: white;
    transition: all 1s linear;
}

.card-wrapper {
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
}

.card-wrapper::before {
    content: '';
    position: absolute;
    width: 325px;
    height: 350px;
    border: 1px solid rgb(253, 253, 253);
    border-radius: 12px;
    opacity: 0.1;
    transition: 1s;
}

.card:hover .card-wrapper::before {
    width: 400px;
    height: 400px;
    opacity: 1;
}

.card-wrapper {
    font-size: 35px;
    letter-spacing: 5px;
    margin: 0;
    transition: 1s;
}

.card-wrapper h2 {
    text-transform: uppercase;
}

.card-wrapper p {
    transition: 2s;
    visibility: hidden;
    opacity: 0;
    font-size: 35px;
    text-transform: capitalize;
    color: rgb(0,0,0);
    margin-top: 25px;
}

.card:hover {
    filter: unset;
    transition: 0.7s;
}

.card:hover .card-wrapper p {
    opacity: 1;
    visibility: visible;
    font-size: 21px;
}

.github, .linkedin {
    display: flex;
    align-items: center;
    margin-right: 20px;
    cursor: pointer;
    position: relative;
}

.github img{
    width: 40px;
    height: auto;
    margin-right: 10px;
    opacity: 0;
    transition: opacity 0.5s, filter 0.3s;
}
.linkedin img {
    width: 50px;
    height: auto;
    margin-right: 10px;
    opacity: 0;
    transition: opacity 0.5s, filter 0.3s;
}

.card:hover .github img, .card:hover .linkedin img {
    opacity: 1;
    filter: brightness(1.2);
}

.github p, .linkedin p {
    margin: 0;
}

.github:hover p, .linkedin:hover p {
    color: white;
}

</style>
