import os

COMMUNITY_DIR = 'community'
README_FILE = 'README.md'
BEGIN_MARKER = '<!-- BEGIN CONTRIBUTORS -->'
END_MARKER = '<!-- END CONTRIBUTORS -->'

def get_profiles():
    files = sorted(os.listdir(COMMUNITY_DIR))
    profiles = [f for f in files if f.endswith('.md')]
    return profiles

def generate_index(profiles):
    lines = [f"- [{os.path.splitext(p)[0]}]({COMMUNITY_DIR}/{p})" for p in profiles]
    return '\n'.join(lines)

def update_readme(index_md):
    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    start = content.find(BEGIN_MARKER)
    end = content.find(END_MARKER)

    if start == -1 or end == -1:
        print("Marcadores não encontrados no README.")
        return

    new_content = (
        content[:start + len(BEGIN_MARKER)] + '\n\n' +
        index_md + '\n\n' +
        content[end:]
    )

    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("README.md atualizado com sucesso.")

if __name__ == "__main__":
    perfis = get_profiles()
    index_md = generate_index(perfis)
    update_readme(index_md)
