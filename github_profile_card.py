import requests

def generate_github_profile_card(username):
    """Gera um card em Markdown com informações de perfil do GitHub."""

    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        response.raise_for_status()
        user_data = response.json()

        card = f"""
<details>
<summary><b>{user_data['name'] or username}</b></summary>
<p align="center">
    <img src="{user_data['avatar_url']}" width="150" alt="Avatar de {user_data['name'] or username}"/>
</p>
<p align="center">
  <b>{user_data['bio'] or 'Sem bio'}</b> <br>
  Localização: {user_data['location'] or 'Não informado'} <br>
  Seguidores: {user_data['followers']} | Seguindo: {user_data['following']} <br>
  <a href="{user_data['html_url']}">Perfil do GitHub</a>
</p>
</details>
"""
        return card

    except requests.exceptions.RequestException as e:
        return f"Erro ao obter informações do perfil: {e}"
    except Exception as e:
        return f"Erro inesperado: {e}"

if __name__ == "__main__":
    username = input("Digite o nome de usuário do GitHub: ")
    card = generate_github_profile_card(username)
    print(card)
