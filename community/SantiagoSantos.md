# Evolução do *dotnet* ao longo do tempo

Este documento tem como objetivo servir como material de apoio para estudos sobre o *dotnet*, apresentando a evolução das versões e dos *frameworks* ao longo do tempo, desde o seu surgimento até o modelo atual unificado.

---

## 1. Origem do *dotnet*

O *dotnet* foi lançado pela *Microsoft* no início dos anos 2000 com a proposta de ser uma plataforma de desenvolvimento unificada, moderna e segura para aplicações *Windows* e, posteriormente, para outros sistemas operacionais.

Os principais pilares iniciais foram:

- O *CLR* (*Common Language Runtime*)
- A *BCL* (*Base Class Library*)
- Suporte a múltiplas linguagens, como *CSharp*, *VB.NET* e *FSharp*

---

## 2. *dotnet Framework* (2002 – 2019)

O *dotnet Framework* foi a primeira implementação da plataforma *dotnet*. Ele era fortemente acoplado ao sistema operacional *Windows*.

### Principais versões

- *dotnet Framework 1.0* (2002)
- *dotnet Framework 2.0* (2005)
- *dotnet Framework 3.5* (2007)
- *dotnet Framework 4.0* (2010)
- *dotnet Framework 4.8* (2019)

### Características

- Execução exclusiva em *Windows*
- Uso de *ASP.NET* para aplicações *web*
- Uso de *WPF* e *WinForms* para aplicações *desktop*
- Modelo de atualização lento e dependente do sistema operacional

> Observação: o *dotnet Framework* está atualmente em modo de manutenção, recebendo apenas correções de segurança.

---

## 3. *dotnet Core* (2016 – 2019)

O *dotnet Core* surgiu como uma reescrita da plataforma, com foco em desempenho, modularidade e compatibilidade multiplataforma.

### Principais versões

- *dotnet Core 1.0* (2016)
- *dotnet Core 2.0* (2017)
- *dotnet Core 3.1* (2019 – *LTS*)

### Características

- Compatível com *Windows*, *Linux* e *macOS*
- Código aberto (*open-source*)
- Melhor desempenho em aplicações *web*
- Introdução do *CLI* (*Command Line Interface*)

---

## 4. Unificação da plataforma: *dotnet 5*

Em 2020, a *Microsoft* iniciou a unificação das plataformas existentes (*dotnet Framework*, *dotnet Core* e *Xamarin*) em um único produto chamado simplesmente de *dotnet*.

O *dotnet 5* não substitui diretamente o *dotnet Framework*, mas se torna o caminho oficial para novos desenvolvimentos.

---

## 5. *dotnet* moderno (6, 7, 8 e superiores)

A partir do *dotnet 6*, a plataforma passou a adotar um ciclo de versões bem definido, com versões *LTS* (*Long Term Support*) e versões *STS* (*Short Term Support*).

### *dotnet 6* (2021 – *LTS*)

- Consolidação da unificação
- Melhorias significativas de desempenho
- Simplificação do modelo de *startup*

### *dotnet 7* (2022 – *STS*)

- Evoluções incrementais
- Melhorias em *ASP.NET Core* e *Entity Framework*

### *dotnet 8* (2023 – *LTS*)

- Foco em aplicações em nuvem (*cloud*)
- Melhorias em *containers*
- Avanços em *AOT* (*Ahead-of-Time Compilation*)

---

## 6. Situação atual recomendada

- Projetos novos: utilizar sempre a versão *LTS* mais recente
- Projetos legados em *dotnet Framework*: manter apenas se houver dependência exclusiva de *Windows*
- Projetos multiplataforma: utilizar *dotnet* unificado (6 ou superior)

---

## 7. Linha do tempo resumida

- 2002: Lançamento do *dotnet Framework*
- 2016: Lançamento do *dotnet Core*
- 2020: Unificação com o *dotnet 5*
- 2021 em diante: Evolução contínua do *dotnet* unificado

---

## Glossário resumido

- *dotnet*: Plataforma de desenvolvimento da *Microsoft* para criação e execução de aplicações
- *Framework*: Conjunto de bibliotecas e ferramentas que facilitam o desenvolvimento
- *CLR*: Ambiente de execução responsável pelo gerenciamento de memória e execução do código
- *BCL*: Biblioteca base de classes reutilizáveis
- *ASP.NET*: Tecnologia para desenvolvimento de aplicações *web*
- *WPF*: Tecnologia para interfaces gráficas ricas em aplicações *desktop*
- *WinForms*: Tecnologia clássica para aplicações *desktop*
- *CLI*: Interface de linha de comando
- *LTS*: Versão com suporte de longo prazo
- *STS*: Versão com suporte de curto prazo
- *Cloud*: Computação em nuvem
- *Container*: Unidade padronizada para empacotamento e execução de aplicações
- *AOT*: Técnica de compilação antecipada para melhorar desempenho

