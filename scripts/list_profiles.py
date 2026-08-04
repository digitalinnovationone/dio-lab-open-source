import os

def list_profiles():
    profiles_dir = "profiles"
    if not os.path.exists(profiles_dir):
        print(f"A pasta '{profiles_dir}' não existe. Criando a pasta...")
        os.makedirs(profiles_dir)  # Cria a pasta se ela não existir
        print(f"Pasta '{profiles_dir}' criada com sucesso.")
        return

    print("Perfis disponíveis:")
    for filename in os.listdir(profiles_dir):
        if filename.endswith(".md"):
            print(f"- {filename[:-3]}")  # Remove a extensão .md

if __name__ == "__main__":
    list_profiles()