const fs = require('fs');
const https = require('https');

const owner = process.argv[2] || 'digitalinnovationone';
const repo = process.argv[3] || 'dio-lab-open-source';
const badgePath = `badges/badge-last-committer.svg`;

function fetchLastCommitter(callback) {
  const options = {
    hostname: 'api.github.com',
    path: `/repos/${owner}/${repo}/commits`,
    headers: { 'User-Agent': 'Node.js' }
  };

  https.get(options, (res) => {
    let data = '';
    
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
      try {
        const commits = JSON.parse(data);
        const humanCommit = commits.find(c => !c.author?.login?.includes('[bot]'));
        const username = humanCommit?.author?.login || 'Desconhecido';
        
        callback(username);
      } catch (err) {
        console.error('Erro ao processar resposta da API:', err);
      }
    });
  }).on('error', err => {
    console.error('Erro na requisição HTTPS:', err);
  });
}

function generateBadge(username) {
  const svg = `
<svg xmlns="http://www.w3.org/2000/svg" width="220" height="20">
  <rect width="140" height="20" fill="#555"/>
  <rect x="140" width="80" height="20" fill="#007ec6"/>
  <text x="10" y="14" fill="#fff" font-family="Verdana" font-size="11">último commit por</text>
  <text x="145" y="14" fill="#fff" font-family="Verdana" font-size="11">${username}</text>
</svg>
  `.trim();

  fs.mkdirSync('badges', { recursive: true });
  fs.writeFileSync(badgePath, svg);
  console.log(`✅ Badge gerado com sucesso: ${badgePath}`);
}

fetchLastCommitter(generateBadge);