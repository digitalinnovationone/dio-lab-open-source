import inquirer from 'inquirer';
import fs from 'fs';

function generateBadgeURL({ label, color, style, logo, logoColor }) {
  const baseUrl = 'https://img.shields.io/badge/';
  const encodedLabel = encodeURIComponent(label);
  const encodedColor = color.startsWith('#') ? `%23${color.substring(1)}` : color;

  const params = new URLSearchParams();

  if (style) params.append('style', style);
  if (logo) params.append('logo', logo);
  if (logoColor) params.append('logoColor', logoColor);

  return `${baseUrl}${encodedLabel}-${encodedColor}.svg?${params.toString()}`;
}

async function run() {
  const badges = [];
  let addMore = true;

  while (addMore) {
    const answers = await inquirer.prompt([
      { type: 'input', name: 'label', message: 'Texto do badge (ex: html, css, javascript)?' },
      { type: 'input', name: 'color', message: 'Cor (nome ou hex, ex: blue ou #ED8B00)?', default: 'blue' },
      { type: 'input', name: 'style', message: 'Estilo (ex: flat, flat-square, for-the-badge)?', default: 'for-the-badge' },
      { type: 'input', name: 'logo', message: 'Logo opcional (ex: html, css, javascript)? (Deixe vazio se não quiser)' },
      { type: 'input', name: 'logoColor', message: 'Cor do logo (ex: white)? (Deixe vazio se não quiser)' },
      { type: 'confirm', name: 'addAnother', message: 'Quer adicionar outro badge?', default: true },
    ]);

    const badgeURL = generateBadgeURL(answers);
    const markdownBadge = `![${answers.label}](${badgeURL})`;
    badges.push(markdownBadge);

    addMore = answers.addAnother;
  }

  const markdownContent = badges.join('\n\n');
  fs.writeFileSync('badges.md', markdownContent);
  console.log('\n✅ Arquivo badges.md gerado com sucesso!\n');
  console.log(markdownContent);
}

run();
