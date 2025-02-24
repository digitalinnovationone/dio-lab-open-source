mport requests
import time

class GitHubConfig:
    """Configurações relacionadas ao GitHub e ao repositório."""
    TOKEN = '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' # Fiquem tranquilos! O próprio GitHub revogou meu PAT ao identificar este commit ;)
    OWNER = 'digitalinnovationone'
    REPO = 'dio-lab-open-source'
    HEADERS = {
        'Authorization': f'token {TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

class ScriptConfig:
    """Configurações específicas do script."""
    DIO_LAB_WORKFLOW_TRIGGER_LABEL = 'run dio workflow'
    DELAY_SECONDS = 10

def obter_prs_abertos():
    """Retorna uma lista de todos os PRs abertos."""
    next_page = 1
    all_prs = []

    while True:
        try:
            response = requests.get(f'https://api.github.com/repos/{GitHubConfig.OWNER}/{GitHubConfig.REPO}/pulls?page={next_page}&per_page=100', headers=GitHubConfig.HEADERS)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro ao recuperar PRs: {e}")
            return []

        prs = response.json()
        all_prs.extend(prs)

        if len(prs) < 100:
            break

        next_page += 1

    print(f"Recuperados {len(all_prs)} PRs abertos no total.")
    return all_prs

def adicionar_label(pr_number):
    """Adiciona a label ao PR especificado."""
    label_data = {'labels': [ScriptConfig.DIO_LAB_WORKFLOW_TRIGGER_LABEL]}
    try:
        response = requests.post(f'https://api.github.com/repos/{GitHubConfig.OWNER}/{GitHubConfig.REPO}/issues/{pr_number}/labels', headers=GitHubConfig.HEADERS, json=label_data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao adicionar label ao PR {pr_number}: {e}")
        return None

    return response.status_code

def main():
    prs_abertos = obter_prs_abertos()
    prs_abertos.reverse()

    for pr in prs_abertos:
        pr_number = pr['number']
        labels = [label['name'] for label in pr['labels']]

        if ScriptConfig.DIO_LAB_WORKFLOW_TRIGGER_LABEL not in labels:
            status_code = adicionar_label(pr_number)
            if status_code:
                print(f"Adicionado label ao PR #{pr_number}, Resposta: {status_code}")
            time.sleep(ScriptConfig.DELAY_SECONDS)
        else:
            print(f"PR #{pr_number} já possui o label. Pulando.")

if __name__ == "__main__":
    main()
