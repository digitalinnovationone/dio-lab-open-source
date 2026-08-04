const fs = require('fs');
const markdownPdf = require('markdown-pdf');
const readline = require('readline');

// Função principal para converter Markdown para PDF
function convertMarkdownToPdf(inputFilePath, outputFilePath) {
    markdownPdf()
        .from(inputFilePath)
        .to(outputFilePath, function () {
            console.log(`PDF gerado com sucesso: ${outputFilePath}`);
        });
}

// Configuração para entrada no terminal
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Função para iniciar o processo
function main() {
    rl.question("Insira o caminho do arquivo README (ex: README.md): ", (inputFilePath) => {
        rl.question("Insira o nome do arquivo PDF de saída (ex: meu_readme.pdf): ", (outputFilePath) => {
            
            // Verificar se o arquivo existe
            if (!fs.existsSync(inputFilePath)) {
                console.error('Erro: O arquivo README não foi encontrado.');
                rl.close();
                return;
            }

            // Converter Markdown para PDF
            convertMarkdownToPdf(inputFilePath, outputFilePath);
            rl.close();
        });
    });
}

// Executar a função principal
main();
