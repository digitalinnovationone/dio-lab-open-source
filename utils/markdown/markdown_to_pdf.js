const fs = require('fs');
const axios = require('axios');
const pdf = require('markdown-pdf');

if (process.argv.length < 4) {
    console.error('Uso: node utils/markdown/markdown_to_pdf.js <url-do-readme> <caminho-do-pdf-output>');
    process.exit(1);
}

const readmeUrl = process.argv[2];
const outputFile = process.argv[3]; 


async function fetchReadme(url) {
    try {
        const response = await axios.get(url);
        return response.data;
    } catch (error) {
        console.error(`Erro ao buscar o README: ${error.message}`);
        process.exit(1);
    }
}


async function convertMarkdownToPdf() {
    const markdownContent = await fetchReadme(readmeUrl);

    
    const tempFile = 'temp_readme.md';
    fs.writeFileSync(tempFile, markdownContent);

    pdf().from(tempFile).to(outputFile, (err) => {
        
        fs.unlinkSync(tempFile);
        if (err) {
            console.error(`Erro ao gerar PDF: ${err.message}`);
        } else {
            console.log(`PDF gerado com sucesso: ${outputFile}`);
        }
    });
}


convertMarkdownToPdf();
