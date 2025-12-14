<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Rafaell Graciliano — Analista de Infraestrutura</title>
  <meta name="description" content="Portfolio de Rafaell Graciliano: suporte e monitoramento, CFTV, ferramentas MONI, iVMS, Sim Next, Python e AWS iniciante. Em transição para Analista de Infraestrutura Pleno." />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root{
      --bg:#0b0e13; --panel:#121622; --soft:#1a1f2e;
      --brand:#e63946; --brand-2:#5bc0be; --text:#eaeef4; --muted:#aab2c5; --ok:#18a999; --warn:#f4a261;
      --shadow:0 10px 30px rgba(0,0,0,.35);
    }
    *{box-sizing:border-box}
    html,body{margin:0;padding:0;background:var(--bg);color:var(--text);font-family:"Inter",system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif}
    a{color:var(--brand);text-decoration:none}
    a:hover{opacity:.9}
    .wrap{max-width:1100px;margin:0 auto;padding:0 24px}
    header{
      position:relative; overflow:hidden;
      background:linear-gradient(135deg, rgba(230,57,70,.14), rgba(91,192,190,.12)), url('https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1600&auto=format&fit=crop') center/cover;
      border-bottom:1px solid #1d2335;
    }
    .hero{padding:88px 0}
    .badge{display:inline-block;background:var(--soft);color:var(--brand-2);padding:6px 12px;border-radius:999px;font-size:12px;letter-spacing:.3px;border:1px solid #263049}
    h1{font-size:44px;margin:18px 0 8px}
    .subtitle{max-width:760px;font-size:18px;color:var(--muted);line-height:1.6}
    .cta-row{margin-top:26px;display:flex;gap:12px;flex-wrap:wrap}
    .btn{display:inline-flex;align-items:center;gap:10px;padding:12px 18px;border-radius:10px;border:1px solid #2a3348;background:var(--panel);color:var(--text);box-shadow:var(--shadow)}
    .btn.primary{background:var(--brand);color:#fff;border-color:transparent}
    .btn.outline{background:transparent;border-color:#33405c}
    .btn small{color:#e1e6f3;opacity:.9}
    .section{padding:50px 0;border-bottom:1px solid #1d2335}
    .grid{display:grid;grid-template-columns:1.2fr .8fr;gap:24px}
    .card{background:var(--panel);border:1px solid #2a3348;border-radius:14px;padding:22px;box-shadow:var(--shadow)}
    .card h3{margin:0 0 12px}
    .list{display:grid;gap:14px}
    .item{display:flex;justify-content:space-between;gap:16px}
    .item .info{max-width:70%}
    .tag{display:inline-block;background:#1f2639;color:#dbe2f7;border:1px solid #2f3956;border-radius:8px;padding:4px 8px;font-size:12px;margin-right:6px;margin-top:8px}
    .pill{display:inline-block;background:#16202f;color:#a7b4d5;border:1px dashed #2b3b59;border-radius:999px;padding:4px 10px;font-size:12px;margin:6px 6px 0 0}
    .skill{margin:10px 0}
    .bar{height:10px;border-radius:999px;background:#1a2133;overflow:hidden;border:1px solid #2b3652}
    .bar > span{display:block;height:100%;background:linear-gradient(90deg, var(--brand), var(--brand-2));border-radius:999px}
    .legend{display:flex;justify-content:space-between;font-size:12px;color:var(--muted);margin-top:6px}
    .timeline{border-left:2px solid #2c3755;padding-left:16px;margin-left:6px}
    .dot{width:10px;height:10px;background:var(--brand-2);border-radius:50%;display:inline-block;margin-right:8px;vertical-align:middle;border:2px solid #203050}
    .mini{font-size:13px;color:var(--muted)}
    footer{padding:30px 0;color:var(--muted)}
    .contact{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
    .contact .card a{display:block;color:#eaeef4}
    .note{font-size:14px;color:#cfd6ea;margin-top:8px}
    .quote{border-left:4px solid var(--warn);padding:12px 16px;background:#201c14;color:#ffeedd;border-radius:10px}
    @media (max-width:900px){.grid{grid-template-columns:1fr}}
    @media (max-width:640px){h1{font-size:34px}.hero{padding:64px 0}.contact{grid-template-columns:1fr}}
  </style>
</head>
<body>

  <!-- Hero -->
  <header>
    <div class="wrap hero">
      <span class="badge">Transição para Infraestrutura Pleno</span>
      <h1>Rafaell Graciliano</h1>
      <p class="subtitle">
        Suporte Júnior em análise de infraestrutura e <strong>Supervisor de Monitoramento</strong> em centrais e CFTV,
        com experiência em MONI, iVMS e Sim Next. Em evolução contínua para <strong>Analista de Infraestrutura Pleno</strong>,
        unindo disciplina operacional, visão de risco e automação inicial em Python/AWS.
      </p>
      <div class="cta-row">
        <a class="btn primary" href="mailto:rgraciliano23@gmail.com">✉️ Fale comigo <small>(e-mail)</small></a>
        <a class="btn" href="https://www.linkedin.com/in/rafaell-graciliano-25134a1bb/" target="_blank" rel="noopener">🔗 Linkedin</a>
        <a class="btn outline" href="#experiencia">📌 Experiência</a>
        <a class="btn outline" href="#skills">🛠️ Skills</a>
      </div>
    </div>
  </header>

  <main class="wrap">

    <!-- Sobre -->
    <section class="section" id="sobre">
      <div class="grid">
        <div class="card">
          <h3>Sobre mim</h3>
          <p>
            Construí minha base na linha de frente do suporte e monitoramento, onde cada minuto importa e cada incidente
            precisa de clareza, método e responsabilidade. Trago esse rigor para a infraestrutura: documentação, observabilidade
            e melhorias incrementais que reduzem risco e tempo de resposta.
          </p>
          <div class="quote">
            “Quem sabe é você a empresa que vai me dar uma chance de mostrar meu empenho e resultado?”
          </div>
          <p class="note">Brasília — disponível para remoto e híbrido.</p>
        </div>
        <div class="card">
          <h3>Foco atual</h3>
          <div class="list">
            <div class="item">
              <div class="info">
                <strong>Infraestrutura</strong>
                <div class="mini">Sistemas, redes, monitoramento e resposta a incidentes</div>
              </div>
              <span class="tag">Pleno (objetivo)</span>
            </div>
            <div class="item">
              <div class="info">
                <strong>Automação e Cloud</strong>
                <div class="mini">Python básico, AWS fundamentos, dashboards com MetaBase</div>
              </div>
              <span class="tag">Em evolução</span>
            </div>
            <div class="item">
              <div class="info">
                <strong>Observabilidade</strong>
                <div class="mini">Zabbix básico, métricas operacionais e gráficos de saúde</div>
              </div>
              <span class="tag">Prática</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Experiência -->
    <section class="section" id="experiencia">
      <div class="grid">
        <div class="card">
          <h3>Experiência</h3>
          <div class="timeline">
            <p><span class="dot"></span><strong>Supervisor de Monitoramento & Suporte técnico intermediário</strong></p>
            <p class="mini">Centrais de monitoramento e CFTV • Ferramentas: MONI, iVMS, Sim Next</p>
            <ul>
              <li>Estabilidade operacional em ambientes 24x7 e coordenação de resposta a incidentes.</li>
              <li>Padronização de playbooks de monitoramento e melhoria de tempo de reação.</li>
              <li>Integração de alertas e triagem com equipes de campo e suporte.</li>
            </ul>
            <br>
            <p><span class="dot" style="background:var(--brand)"></span><strong>Suporte Júnior — Análise de Infraestrutura</strong></p>
            <p class="mini">Atendimento técnico, troubleshooting inicial e documentação</p>
            <ul>
              <li>Resolução de tickets nível 1/2 com foco em causa raiz e registro claro.</li>
              <li>Criação de checklists e procedimentos de recuperação em falhas recorrentes.</li>
              <li>Apoio na implantação de monitoramento e indicadores de saúde.</li>
            </ul>
          </div>
        </div>

        <div class="card">
          <h3>Ferramentas e ambientes</h3>
          <span class="pill">MONI</span>
          <span class="pill">iVMS</span>
          <span class="pill">Sim Next</span>
          <span class="pill">Zabbix (iniciante)</span>
          <span class="pill">MetaBase (iniciante)</span>
          <span class="pill">Redes (iniciante)</span>
          <span class="pill">Python (iniciante)</span>
          <span class="pill">AWS (iniciante)</span>
          <p class="note">Fortalecendo fundamentos e boas práticas de infraestrutura para atuação plena.</p>
        </div>
      </div>
    </section>

    <!-- Skills -->
    <section class="section" id="skills">
      <div class="grid">
        <div class="card">
          <h3>Competências técnicas</h3>

          <div class="skill">
            <strong>Monitoramento e resposta</strong>
            <div class="bar"><span style="width:72%"></span></div>
            <div class="legend"><span>Operação</span><span>Avançando</span></div>
          </div>

          <div class="skill">
            <strong>Zabbix</strong>
            <div class="bar"><span style="width:35%"></span></div>
            <div class="legend"><span>Fundamentos</span><span>Em curso</span></div>
          </div>

          <div class="skill">
            <strong>Redes</strong>
            <div class="bar"><span style="width:38%"></span></div>
            <div class="legend"><span>Camadas & troubleshooting</span><span>Em curso</span></div>
          </div>

          <div class="skill">
            <strong>Python</strong>
            <div class="bar"><span style="width:32%"></span></div>
            <div class="legend"><span>Automação básica</span><span>Iniciante</span></div>
          </div>

          <div class="skill">
            <strong>AWS</strong>
            <div class="bar"><span style="width:28%"></span></div>
            <div class="legend"><span>Cloud fundamentos</span><span>Iniciante</span></div>
          </div>

          <div class="skill">
            <strong>MetaBase</strong>
            <div class="bar"><span style="width:30%"></span></div>
            <div class="legend"><span>Dashboards</span><span>Iniciante</span></div>
          </div>
        </div>

        <div class="card">
          <h3>Diferenciais</h3>
          <ul class="list">
            <li class="item">
              <div class="info">
                <strong>Rigor operacional</strong>
                <div class="mini">Consistência em ambientes críticos e foco em redução de riscos.</div>
              </div>
              <span class="tag">Confiabilidade</span>
            </li>
            <li class="item">
              <div class="info">
                <strong>Documentação clara</strong>
                <div class="mini">Playbooks e registros que aceleram diagnóstico e transferência de conhecimento.</div>
              </div>
              <span class="tag">Eficiência</span>
            </li>
            <li class="item">
              <div class="info">
                <strong>Aprendizado ativo</strong>
                <div class="mini">Evolução contínua em cloud, automação e observabilidade.</div>
              </div>
              <span class="tag">Crescimento</span>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Projetos/Resultados -->
    <section class="section" id="projetos">
      <div class="grid">
        <div class="card">
          <h3>Resultados e iniciativas</h3>
          <ul>
            <li>Padronização de alertas e triagem, reduzindo tempo de reação em centrais de monitoramento.</li>
            <li>Criação de checklists de saúde de sistemas e procedimentos de contingência.</li>
            <li>Prototipagem de dashboards (MetaBase) para visão rápida de incidentes e SLA.</li>
          </ul>
          <p class="note">Disponível para detalhar métricas e exemplos práticos em entrevista.</p>
        </div>
        <div class="card">
          <h3>O que busco</h3>
          <p>Uma equipe onde disciplina, colaboração e melhoria contínua são parte da cultura. Quero contribuir com confiabilidade, documentação viva e monitoramento que antecipa problemas.</p>
          <p><strong>Objetivo:</strong> Analista de Infraestrutura Pleno.</p>
        </div>
      </div>
    </section>

    <!-- Contato -->
    <section class="section" id="contato">
      <div class="card">
        <h3>Contato</h3>
        <div class="contact">
          <div class="card">
            <strong>E-mail</strong>
            <a href="mailto:rgraciliano23@gmail.com">rgraciliano23@gmail.com</a>
            <div class="mini">Resposta rápida em horário comercial.</div>
          </div>
          <div class="card">
            <strong>LinkedIn</strong>
            <a href="https://www.linkedin.com/in/rafaell-graciliano-25134a1bb/" target="_blank" rel="noopener">/in/rafaell-graciliano-25134a1bb</a>
            <div class="mini">Conexões, oportunidades e projetos.</div>
          </div>
          <div class="card">
            <strong>Disponibilidade</strong>
            <div>Remoto | Híbrido • Brasília</div>
            <div class="mini">Pronto para processos seletivos.</div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <footer class="wrap">
    <div class="mini">© 2025 — Rafaell Graciliano. Este portfolio é uma prévia do que posso fazer quando tenho a missão certa.</div>
  </footer>

</body>
</html>