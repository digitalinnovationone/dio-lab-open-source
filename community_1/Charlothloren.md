<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de Section de Palestrantes</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Seu CSS - Certifique-se que o caminho está correto -->
    <link href="./style.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        <!-- Formulário de Entrada -->
        <div class="row">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-header">
                        <h5 class="card-title mb-0">Adicionar Palestrante</h5>
                    </div>
                    <div class="card-body">
                        <form id="speakerForm">
                            <div class="mb-3">
                                <label for="name" class="form-label">Nome do Palestrante</label>
                                <input type="text" class="form-control" id="name" required>
                            </div>
                            <div class="mb-3">
                                <label for="role" class="form-label">Cargo</label>
                                <input type="text" class="form-control" id="role" required>
                            </div>
                            <div class="mb-3">
                                <label for="description" class="form-label">Descrição</label>
                                <textarea class="form-control" id="description" rows="3" required></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="image" class="form-label">URL da Imagem</label>
                                <input type="url" class="form-control" id="image" required>
                            </div>
                            <button type="submit" class="btn btn-primary">Adicionar Palestrante</button>
                        </form>
                    </div>
                </div>
                <!-- Botão de Exportação -->
                <div class="mt-3">
                    <button id="exportBtn" class="btn btn-success w-100">Exportar Section</button>
                </div>
            </div>

            <!-- Preview dos Palestrantes -->
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">
                        <h5 class="card-title mb-0">Preview dos Palestrantes</h5>
                        <small class="text-muted">Visualize como os cards ficarão antes de exportar</small>
                    </div>
                    <div class="card-body">
                        <div id="speakersPreview" class="row">
                            <!-- Cards dos palestrantes serão inseridos aqui dinamicamente -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal de Exportação -->
    <div class="modal fade" id="exportModal" tabindex="-1">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Código da Section</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <div class="mb-3">
                        <label class="form-label">Código HTML Gerado:</label>
                        <textarea id="exportedCode" class="form-control" rows="10" readonly></textarea>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
                    <button type="button" class="btn btn-primary" id="copyBtn">Copiar Código</button>
                    <button type="button" class="btn btn-success" id="downloadBtn">Download HTML</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Seu JavaScript - Certifique-se que o caminho está correto -->
    <script src="./script.js"></script>

    <!-- Script de Debug -->
    <script>
        // Adicionar isso temporariamente para debug
        console.log('DOM carregado');
        document.getElementById('speakerForm').addEventListener('submit', function(e) {
            console.log('Formulário enviado');
            e.preventDefault();
            const formData = {
                name: document.getElementById('name').value,
                role: document.getElementById('role').value,
                description: document.getElementById('description').value,
                image: document.getElementById('image').value
            };
            console.log('Dados do formulário:', formData);
        });
    </script>
</body>
</html>
