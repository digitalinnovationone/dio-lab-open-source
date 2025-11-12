# Professional Guide to Git and GitHub
English Version

---

## 📖 Introduction
**Git** is a distributed version control system widely used to track changes in files and coordinate work on software projects.  
**GitHub** is a cloud-based platform that uses Git to host repositories and facilitate collaboration among developers.

---

## 🔑 Fundamental Concepts

### What is Git?
Git is a distributed version control system created by **Linus Torvalds in 2005** to manage the Linux kernel development.  
It is known for its **efficiency, reliability**, and support for **non-linear workflows**.  

📚 Official documentation: [Git Documentation](https://git-scm.com/doc)

### What is GitHub?
GitHub is a platform that uses Git to host code repositories.  
Beyond storage, it provides collaboration tools such as **pull requests, issues, code reviews, and GitHub Actions**.  

📚 Official documentation: [GitHub Docs](https://docs.github.com/)

---

## ⚙️ Git Features
- Distributed: every developer has a complete copy of the repository history.  
- Fast: operations such as commits, diffs, and merges are performed locally.  
- Secure: uses SHA-1 to ensure integrity.  
- Flexible: supports multiple workflows and integrations.  

## 🌐 GitHub Features
- Collaboration: pull requests, code reviews, and discussions.  
- Continuous Integration: automation with GitHub Actions.  
- Documentation: support for wikis and README files.  
- Community: millions of active projects and developers.  

📚 README Guide: [GitHub - About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)  
📚 Repository Guide: [GitHub - About Repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)

---

## 📝 Basic Git Commands

- Initialize a repository  
```bash
git init
Clone a repository

bash
git clone <repository-url>
Check status

bash
git status
Add files

bash
git add <file>
Commit changes

bash
git commit -m "Commit message"
Push changes

bash
git push origin <branch-name>
🚀 Advanced Git Commands
View commit history

bash
git log
Create and switch to a new branch

bash
git checkout -b <branch-name>
Merge branches

bash
git merge <branch-name>
Resolve conflicts

bash
git status
git add <file>
git commit
Revert a commit

bash
git revert <commit-hash>
Reset to a previous state

bash
git reset --hard <commit-hash>
✅ Best Practices
Small and frequent commits.

Clear and descriptive commit messages.

Separate branches for new features.

Code reviews before merging.

📚 Official best practices: GitHub Flow

🛠️ Additional GitHub Resources
GitHub CLI → GitHub CLI Docs

GitHub Copilot → GitHub Copilot Docs

GitHub Sponsors → GitHub Sponsors

🌍 Other Official Documentation Platforms
Microsoft Learn (Azure DevOps & Git) → Microsoft Learn - Azure DevOps

GitLab Documentation → GitLab Docs

Atlassian Bitbucket Documentation → Bitbucket Docs

SourceForge Documentation → SourceForge Docs

GNU Savannah (Free Software Projects) → Savannah Docs

🎯 Motivation for This Contribution
This guide was created with the following goals:

Facilitate learning Git and GitHub.

Promote best practices in version control and collaboration.

Serve as a quick reference for essential commands.

Contribute to the community by providing accessible and organized material.

Inspire developers to explore official documentation across multiple platforms.

📌 Conclusion
Git and GitHub are indispensable tools for modern teams. With Git, you can efficiently manage project history. With GitHub, you can expand collaboration and integrate automations that accelerate development. With platforms like Microsoft Learn, GitLab, and Bitbucket, you can broaden your knowledge and adapt workflows to different ecosystems.