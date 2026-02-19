<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Igor Nunes Patricio - Profile</title>
  <style>
    body {
      background-color: #121212;
      color: #fff;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      text-align: center;
      padding: 2rem;
      margin: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      flex-direction: column;
    }

    .profile-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }

    .profile-pic {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        border: 3px solid #30A3DC;
        object-fit: cover;
        box-shadow: 0 4px 15px rgba(48, 163, 220, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .profile-pic:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(48, 163, 220, 0.6);
    }


    h1 {
      font-size: 2rem;
      margin-bottom: 1rem;
      color: #30A3DC;
    }

    .badges img {
      margin: 0.5rem;
      width: 120px;
    }

    .badges {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 1rem;
      margin: 1.5rem 0;
    }
    
    .badge-icon-button {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background-color: #1e1e1e;
      border: 2px solid #30A3DC;
      transition: all 0.3s ease;
      box-shadow: 0 4px 10px rgba(48, 163, 220, 0.2);
    }
    
    .badge-icon-button:hover {
      background-color: #30A3DC;
      transform: scale(1.1);
      box-shadow: 0 6px 14px rgba(48, 163, 220, 0.4);
    }
    
    .badge-icon-button img {
      width: 24px;
      height: 24px;
    }
    
    .badge-button {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      background-color: #1e1e1e;
      border: 2px solid #30A3DC;
      color: #ffffff;
      text-decoration: none;
      padding: 0.7rem 1.2rem;          /* Slightly more padding */
      border-radius: 10px;
      font-weight: 600;
      font-size: 1.1rem;              /* ⬅️ Increased font size */
      transition: all 0.3s ease;
      box-shadow: 0 4px 10px rgba(48, 163, 220, 0.2);
    }

    
    .badge-button:hover {
      background-color: #30A3DC;
      color: #000;
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(48, 163, 220, 0.4);
    }
    
    .badge-icon {
      width: 26px;
      height: 26px;
    }

    .about-me {
      max-width: 700px;
      margin: 0 auto;
      text-align: left;
    }
    
    .about-me h2 {
      text-align: center;
      margin-bottom: 1.5rem;
    }
    
    .about-me ul {
      list-style: none;
      padding: 0;
    }
    
    .about-me li {
      display: flex;
      align-items: center;
      gap: 0.8rem;
      margin-bottom: 1rem;
      font-size: 1.05rem;
      line-height: 1.6;
    }


    hr {
      border: none;
      height: 1px;
      background: #30A3DC;
      margin: 2rem auto;
      width: 80%;
    }

    a {
      color: #30A3DC;
      text-decoration: none;
      font-weight: bold;
    }

    ul {
      list-style: none;
      padding: 0;
      line-height: 1.8;
      font-size: 1.1rem;
    }

    footer {
      margin-top: 2rem;
      font-style: italic;
      color: #aaa;
      font-size: 1rem;
    }

    .stats-container {
      margin: 2rem 0;
    }

    .stats-container img {
      width: 100%;
      max-width: 600px;
      margin: 0.5rem 0;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
      body {
        padding: 1rem;
      }

      h1 {
        font-size: 1.5rem;
      }

      .profile-pic {
        width: 130px;
        height: 130px;
      }

      .badges img {
        width: 100px;
      }

      .stats-container img {
        max-width: 100%;
      }
    }

    .profile-frame {
         padding: 1rem;
        border-radius: 50%;
        background: linear-gradient(145deg, #1a1a1a, #101010);
        box-shadow: 10px 10px 30px #0a0a0a, -10px -10px 30px #1e1e1e;
    }


  </style>
</head>
<body>

  <!-- Profile Picture -->
  <div class="profile-container">
    <div class="profile-frame">
      <img 
        class="profile-pic" 
        src="https://media.licdn.com/dms/image/v2/D4D03AQFpVzEefV_ojg/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1692807745726?e=1749686400&v=beta&t=0elVTsPYjV8LcWSTjruHIxTMjk8C2hHwbZEYADOsIC4" 
        alt="Igor Nunes Patricio" 
      />
    </div>
  </div>


  <h1>Hi there, I'm Igor Nunes Patricio 👋</h1>

  <!-- Badges -->
  <div class="badges">
    <a href="https://www.linkedin.com/in/nunespatricioigor/" target="_blank" class="badge-button">
      <img class="badge-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" />
      LinkedIn
    </a>
    <a href="https://github.com/igornunespatricio" target="_blank" class="badge-button">
      <img class="badge-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" />
      GitHub
    </a>
  </div>

  <hr />

<!-- About Me -->
<section class="about-me">
  <h2>👨‍💻 About Me</h2>
  <ul>
    <li><span>🎯</span> Data Scientist passionate about solving problems with data</li>
    <li><span>🏢</span> Working at <strong>Airswift</strong></li>
    <li><span>🎓</span> Studied at <strong>UFRJ</strong> (Universidade Federal do Rio de Janeiro)</li>
    <li><span>🧠</span> Experienced in ML and data analysis</li>
    <li><span>🌱</span> Lifelong learner exploring new technologies</li>
  </ul>
</section>

  <hr />

  <!-- GitHub Stats -->
  <div class="stats-container">
    <h2>📊 GitHub Stats</h2>
    <img 
      src="https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api/top-langs/?username=igornunespatricio&layout=compact&bg_color=000&border_color=30A3DC&title_color=E94D5F&text_color=FFF"
      alt="Top Languages"
    />
    <img 
      src="https://streak-stats.demolab.com/?user=igornunespatricio&theme=bear&background=000&border=30A3DC&dates=FFF"
      alt="GitHub Streak"
    />
  </div>

  <hr />

  <!-- Contact -->
  <h2>📫 Connect with Me</h2>
  <p>
    💼 <a href="https://www.linkedin.com/in/nunespatricioigor/" target="_blank">LinkedIn</a><br />
    💻 <a href="https://github.com/igornunespatricio" target="_blank">GitHub</a>
  </p>

  <footer>
    Thanks for stopping by! 🚀
  </footer>

</body>
</html>
