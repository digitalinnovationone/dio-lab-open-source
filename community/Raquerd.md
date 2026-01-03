```python
# ESTRUTURA
Usuario = {'Nome':'Davi Santos Ferriera', 
        'Idade':'22', 
        'Area':'Trade Marketing', 
        'Local':'Sao Paulo',
        'Formacao':'Analise e desenvolvimento de sistemas (INCOMPLETO)',
        'Instituicao':'UniFECAF',
        'Cargo':'Auxiliar Administrativo',
        'Linguagens':['Python', 'SQL']
        }
        
# ESCREVENDO ROTEIRO
print(f"\
    \033[1mSobre mim\033[m\n \
    Meu nome é {Usuario['Nome']} tenho {Usuario['Idade']} anos, Possuo ensino superior incompleto em {Usuario['Formacao']}, cursado na instituição {Usuario['Instituicao']}. atualmente trabalho como {Usuario['Cargo']} realizando automação e manutenção de banco de dados na area de {Usuario['Area']}.\n \
    Me apaixonei por programação e banco de dados ao utilizar ferramentas pela primeira vez de forma profissional\n \
    \033[1mHabilidades\033[m\n \
    {[l for l in Usuario['Linguagens']]}\n \
    \033[1mObjetivo\033[m\n \
    Tenho como objetivo principal me dotar cada vez mais de todo tipo de conhecimento, não importa se é voltado para tecnologia ou não, o que importa é se isso vai me tornar melhor como profissional ou como pessoa.")


    
```
# RESULTADO
## Sobre mim
Meu nome é Davi Santos Ferriera tenho 22 anos, Possuo ensino superior incompleto em Analise e desenvolvimento de sistemas (INCOMPLETO), cursado na instituição UniFECAF. atualmente trabalho como Auxiliar Administrativo realizando automação e manutenção de banco de dados na area de Trade Marketing.
Me apaixonei por programação e banco de dados ao utilizar ferramentas pela primeira vez de forma profissional
### Habilidades: 
['Python', 'SQL']

## Objetivos
Tenho como objetivo principal me dotar cada vez mais de todo tipo de conhecimento, não importa se é voltado para tecnologia ou não, o que importa é se isso vai me tornar melhor como profissional ou como pessoa.
