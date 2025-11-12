# Guía Profesional de Git y GitHub
Versión en Español

---

## 📖 Introducción
**Git** es un sistema de control de versiones distribuido ampliamente utilizado para rastrear cambios en archivos y coordinar el trabajo en proyectos de software.  
**GitHub** es una plataforma basada en la nube que utiliza Git para alojar repositorios y facilitar la colaboración entre desarrolladores.

---

## 🔑 Conceptos Fundamentales

### ¿Qué es Git?
Git es un sistema de control de versiones distribuido creado por **Linus Torvalds en 2005** para gestionar el desarrollo del kernel de Linux.  
Es conocido por su **eficiencia, confiabilidad** y soporte para **flujos de trabajo no lineales**.  

📚 Documentación oficial: [Git Documentation](https://git-scm.com/doc)

### ¿Qué es GitHub?
GitHub es una plataforma que utiliza Git para alojar repositorios de código.  
Además del almacenamiento, ofrece herramientas de colaboración como **pull requests, issues, revisiones de código y GitHub Actions**.  

📚 Documentación oficial: [GitHub Docs](https://docs.github.com/)

---

## ⚙️ Características de Git
- Distribuido: cada desarrollador tiene una copia completa del historial del repositorio.  
- Rápido: operaciones como commits, diffs y merges se realizan localmente.  
- Seguro: utiliza SHA-1 para garantizar la integridad.  
- Flexible: soporta múltiples flujos de trabajo e integraciones.  

## 🌐 Características de GitHub
- Colaboración: pull requests, revisiones de código y discusiones.  
- Integración continua: automatización con GitHub Actions.  
- Documentación: soporte para wikis y archivos README.  
- Comunidad: millones de proyectos y desarrolladores activos.  

📚 Guía de README: [GitHub - About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)  
📚 Guía de Repositorios: [GitHub - About Repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)

---

## 📝 Comandos Básicos de Git

- Inicializar un repositorio  
```bash
git init
Clonar un repositorio

bash
git clone <url-del-repositorio>
Verificar estado

bash
git status
Agregar archivos

bash
git add <archivo>
Hacer commit

bash
git commit -m "Mensaje del commit"
Enviar cambios

bash
git push origin <nombre-del-branch>
🚀 Comandos Avanzados de Git
Ver historial de commits

bash
git log
Crear y cambiar a un nuevo branch

bash
git checkout -b <nombre-del-branch>
Fusionar branches

bash
git merge <nombre-del-branch>
Resolver conflictos

bash
git status
git add <archivo>
git commit
Revertir un commit

bash
git revert <hash-del-commit>
Resetear a un estado anterior

bash
git reset --hard <hash-del-commit>
✅ Buenas Prácticas
Commits pequeños y frecuentes.

Mensajes de commit claros y descriptivos.

Branches separados para nuevas funcionalidades.

Revisiones de código antes de hacer merges.

📚 Guía oficial de buenas prácticas: GitHub Flow

🛠️ Recursos Adicionales de GitHub
GitHub CLI → GitHub CLI Docs

GitHub Copilot → GitHub Copilot Docs

GitHub Sponsors → GitHub Sponsors

🌍 Otras Plataformas con Documentación Oficial
Microsoft Learn (Azure DevOps & Git) → Microsoft Learn - Azure DevOps

GitLab Documentation → GitLab Docs

Atlassian Bitbucket Documentation → Bitbucket Docs

SourceForge Documentation → SourceForge Docs

GNU Savannah (Proyectos de Software Libre) → Savannah Docs

🎯 Motivación de Esta Contribución
Este guía fue creada con los siguientes objetivos:

Facilitar el aprendizaje de Git y GitHub.

Promover buenas prácticas de versionamiento y colaboración.

Servir como referencia rápida para comandos esenciales.

Contribuir con la comunidad ofreciendo material accesible y organizado.

Inspirar a los desarrolladores a explorar documentación oficial en múltiples plataformas.

📌 Conclusión
Git y GitHub son herramientas indispensables para equipos modernos. Con Git, puedes gestionar el historial de manera eficiente. Con GitHub, puedes ampliar la colaboración e integrar automatizaciones que aceleran el desarrollo. Con plataformas como Microsoft Learn, GitLab y Bitbucket, puedes ampliar tu conocimiento y adaptar flujos de trabajo a diferentes ecosistemas.