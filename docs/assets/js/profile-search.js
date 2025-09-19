/**
 * Sistema de Busca Avançada para Perfis DIO
 * Permite busca por tecnologias, habilidades e conteúdo dos perfis
 */

class ProfileSearchEngine {
    constructor() {
        this.profiles = [];
        this.filteredProfiles = [];
        this.searchCache = new Map();
        this.isLoading = false;
        
        this.init();
    }

    async init() {
        await this.loadProfiles();
        this.setupEventListeners();
        this.renderProfiles();
    }

    async loadProfiles() {
        if (this.isLoading) return;
        this.isLoading = true;
        
        try {
            // Busca a lista de arquivos na pasta community
            const response = await fetch('https://api.github.com/repos/digitalinnovationone/dio-lab-open-source/contents/community');
            const files = await response.json();
            
            // Filtra apenas arquivos .md
            const profileFiles = files
                .filter(file => file.name.endsWith('.md'))
                .slice(0, 100); // Limita para performance inicial
            
            // Carrega conteúdo dos perfis
            this.profiles = await Promise.all(
                profileFiles.map(async (file) => {
                    try {
                        const contentResponse = await fetch(file.download_url);
                        const content = await contentResponse.text();
                        return this.parseProfile(file.name, content);
                    } catch (error) {
                        console.warn(`Erro ao carregar ${file.name}:`, error);
                        return null;
                    }
                })
            );
            
            this.profiles = this.profiles.filter(profile => profile !== null);
            this.filteredProfiles = [...this.profiles];
            
        } catch (error) {
            console.error('Erro ao carregar perfis:', error);
            this.showError('Erro ao carregar perfis. Tente novamente.');
        } finally {
            this.isLoading = false;
        }
    }

    parseProfile(filename, content) {
        const username = filename.replace('.md', '');
        
        // Extrai informações do perfil usando regex
        const titleMatch = content.match(/^#\s+(.+)/m);
        const title = titleMatch ? titleMatch[1].replace(/[#*`]/g, '').trim() : username;
        
        // Extrai tecnologias mencionadas
        const technologies = this.extractTechnologies(content);
        
        // Extrai links de contato
        const contacts = this.extractContacts(content);
        
        // Extrai estatísticas do GitHub (se mencionadas)
        const githubStats = this.extractGitHubStats(content);
        
        // Preview do conteúdo (primeiras 200 caracteres)
        const preview = content
            .replace(/[#*`]/g, '')
            .replace(/!\[.*?\]\(.*?\)/g, '')
            .substring(0, 200)
            .trim();

        return {
            username,
            title,
            technologies,
            contacts,
            githubStats,
            preview,
            content,
            filename
        };
    }

    extractTechnologies(content) {
        const techRegex = /!\[([^\]]+)\]\([^)]+\)/g;
        const technologies = [];
        let match;
        
        while ((match = techRegex.exec(content)) !== null) {
            const tech = match[1].trim();
            if (tech && !tech.includes('badge') && !tech.includes('GitHub')) {
                technologies.push(tech);
            }
        }
        
        // Remove duplicatas e limita a 10
        return [...new Set(technologies)].slice(0, 10);
    }

    extractContacts(content) {
        const contacts = {};
        const patterns = {
            linkedin: /linkedin\.com\/in\/([^/)]+)/gi,
            github: /github\.com\/([^/)]+)/gi,
            email: /mailto:([^)]+)/gi,
            portfolio: /https?:\/\/[^\s)]+(?=.*portfolio)/gi
        };
        
        for (const [type, pattern] of Object.entries(patterns)) {
            const match = content.match(pattern);
            if (match) {
                contacts[type] = match[0];
            }
        }
        
        return contacts;
    }

    extractGitHubStats(content) {
        const statsMatch = content.match(/github-readme-stats\.vercel\.app\/api\?username=([^&]+)/);
        return statsMatch ? statsMatch[1] : null;
    }

    setupEventListeners() {
        const searchInput = document.getElementById('searchInput');
        const technologyFilter = document.getElementById('technologyFilter');
        const sortSelect = document.getElementById('sortSelect');
        
        if (searchInput) {
            searchInput.addEventListener('input', this.debounce(() => {
                this.performSearch();
            }, 300));
        }
        
        if (technologyFilter) {
            technologyFilter.addEventListener('change', () => {
                this.performSearch();
            });
        }
        
        if (sortSelect) {
            sortSelect.addEventListener('change', () => {
                this.performSearch();
            });
        }
    }

    performSearch() {
        const searchTerm = document.getElementById('searchInput')?.value.toLowerCase() || '';
        const technologyFilter = document.getElementById('technologyFilter')?.value || '';
        const sortBy = document.getElementById('sortSelect')?.value || 'username';
        
        this.filteredProfiles = this.profiles.filter(profile => {
            const matchesSearch = !searchTerm || 
                profile.username.toLowerCase().includes(searchTerm) ||
                profile.title.toLowerCase().includes(searchTerm) ||
                profile.preview.toLowerCase().includes(searchTerm) ||
                profile.technologies.some(tech => tech.toLowerCase().includes(searchTerm));
            
            const matchesTechnology = !technologyFilter || 
                profile.technologies.some(tech => tech.toLowerCase().includes(technologyFilter.toLowerCase()));
            
            return matchesSearch && matchesTechnology;
        });
        
        this.sortProfiles(sortBy);
        this.renderProfiles();
    }

    sortProfiles(sortBy) {
        this.filteredProfiles.sort((a, b) => {
            switch (sortBy) {
                case 'username':
                    return a.username.localeCompare(b.username);
                case 'title':
                    return a.title.localeCompare(b.title);
                case 'technologies':
                    return b.technologies.length - a.technologies.length;
                default:
                    return 0;
            }
        });
    }

    renderProfiles() {
        const container = document.getElementById('profilesContainer');
        if (!container) return;
        
        if (this.isLoading) {
            container.innerHTML = `
                <div class="loading-spinner">
                    <div class="spinner"></div>
                    <p>Carregando perfis...</p>
                </div>
            `;
            return;
        }
        
        if (this.filteredProfiles.length === 0) {
            container.innerHTML = `
                <div class="no-results">
                    <i class="bi bi-search"></i>
                    <h3>Nenhum perfil encontrado</h3>
                    <p>Tente ajustar os filtros de busca</p>
                </div>
            `;
            return;
        }
        
        const profilesHTML = this.filteredProfiles.map(profile => `
            <div class="profile-card" onclick="window.open('https://github.com/${profile.username}', '_blank')">
                <div class="profile-header">
                    <h3 class="profile-title">${this.escapeHtml(profile.title)}</h3>
                    <span class="profile-username">@${profile.username}</span>
                </div>
                
                <div class="profile-preview">
                    <p>${this.escapeHtml(profile.preview)}...</p>
                </div>
                
                ${profile.technologies.length > 0 ? `
                    <div class="profile-technologies">
                        ${profile.technologies.slice(0, 5).map(tech => 
                            `<span class="tech-badge">${this.escapeHtml(tech)}</span>`
                        ).join('')}
                        ${profile.technologies.length > 5 ? 
                            `<span class="tech-more">+${profile.technologies.length - 5}</span>` : ''}
                    </div>
                ` : ''}
                
                <div class="profile-actions">
                    <button class="btn-view-profile" onclick="event.stopPropagation(); this.viewProfile('${profile.username}')">
                        <i class="bi bi-eye"></i> Ver Perfil
                    </button>
                </div>
            </div>
        `).join('');
        
        container.innerHTML = `
            <div class="profiles-grid">
                ${profilesHTML}
            </div>
            <div class="search-info">
                <p>Mostrando ${this.filteredProfiles.length} de ${this.profiles.length} perfis</p>
            </div>
        `;
    }

    viewProfile(username) {
        // Abre o perfil do GitHub em nova aba
        window.open(`https://github.com/${username}`, '_blank');
    }

    showError(message) {
        const container = document.getElementById('profilesContainer');
        if (container) {
            container.innerHTML = `
                <div class="error-message">
                    <i class="bi bi-exclamation-triangle"></i>
                    <h3>Ops! Algo deu errado</h3>
                    <p>${message}</p>
                    <button onclick="location.reload()" class="btn-retry">Tentar Novamente</button>
                </div>
            `;
        }
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
}

// Inicializa o sistema de busca quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', () => {
    new ProfileSearchEngine();
});
