# Fabiodevfull - Sistema de Pull Requests em Django

## Visão Geral
Este projeto implementa um sistema de **Pull Requests (PRs)** semelhante ao do GitHub, mas dentro de um site feito com **Django**. O objetivo é permitir que usuários contribuam com modificações, que depois podem ser revisadas e aprovadas por administradores.

## O que são Pull Requests (PRs)?
Um **Pull Request (PR)** é uma solicitação para mesclar alterações de código de um repositório em uma ramificação principal. Ele permite que desenvolvedores proponham melhorias, corrijam erros ou adicionem novas funcionalidades ao projeto. Administradores ou revisores podem analisar as mudanças antes de aprová-las e incorporá-las ao código principal.

## Minha História
Meu nome é Fábio e sempre tive paixão por tecnologia e desenvolvimento. Iniciei meus estudos em **Análise e Desenvolvimento de Sistemas** pela Estácio, mas, devido às diversas mudanças de horário no meu trabalho, precisei interromper o curso.

Posteriormente, me matriculei no curso técnico **Fullstack para Internet** no Senac. Quando estava prestes a finalizá-lo, enfrentei um problema no meu emprego que impossibilitou minha participação nas aulas presenciais. Após mudar de trabalho, novamente não consegui concluir o curso devido aos horários da nova ocupação.

Apesar dos desafios, nunca desisti. Fiz vários cursos profissionalizantes, incluindo formações na **Alura**, e sigo me aperfeiçoando. Meu objetivo para este ano é ingressar definitivamente na área de tecnologia, pois é algo que amo e pelo qual sou profundamente apaixonado.

## Funcionalidades
- Criar **Pull Requests** com sugestões de alteração.
- Listar PRs pendentes e aprovados.
- Aprovação/Rejeição de PRs por administradores.
- Controle de versão básico para acompanhamento das mudanças.

## Tecnologias Utilizadas
- **Python** + **Django** (Framework Web)
- **SQLite/PostgreSQL** (Banco de Dados)
- **HTML, CSS e JavaScript** (Interface Web)
- **Django REST Framework (DRF)** (para APIs, opcional)


from django.urls import path
from .views import list_prs

urlpatterns = [
    path('pull-requests/', list_prs, name='list_prs'),
]
```

####   Próximos Passos
- Criar templates HTML para exibir PRs.
- Implementar lógica de aprovação/rejeição.
- Adicionar autenticação para controle de permissões.
- Melhorar UI com Bootstrap ou TailwindCSS.



