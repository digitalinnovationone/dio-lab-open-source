// api/banner.svg.ts
export default function handler(req: any, res: any) {
  const { name = "Visitante" } = req.query;
  const safe = String(name).slice(0, 60);

  res.setHeader("Content-Type", "image/svg+xml");
  res.setHeader("Cache-Control", "max-age=0, s-maxage=600"); // 10min no CDN

  const svg = `
<svg width="720" height="160" viewBox="0 0 720 160" xmlns="http://www.w3.org/2000/svg">
  <style>
    @keyframes dash { to { stroke-dashoffset: 0; } }
    @keyframes blink { 50% { opacity: 0; } }
    .line {
      stroke: #30A3DC; stroke-width: 6; fill: none;
      stroke-dasharray: 900; stroke-dashoffset: 900;
      animation: dash 2.5s ease-in-out forwards;
    }
    .txt {
      font: 700 28px system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
      fill: #E94D5F;
    }
    .cursor {
      font: 700 28px system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
      fill: #E94D5F; animation: blink 1s step-end infinite;
    }
  </style>

  <rect width="100%" height="100%" fill="#000"/>
  <path class="line" d="M20 120 C 180 10, 300 190, 460 90 S 640 20, 700 120"/>
  <text class="txt" x="24" y="60">Olá, eu sou ${safe}</text>
  <text class="txt" x="24" y="100">Desenvolvedor Full-Stack</text>
  <text class="cursor" x="420" y="60">|</text>
</svg>`;
  res.status(200).send(svg);
}
