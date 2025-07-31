
# cracked esteve aqui.

O bolo de banana com calda de caramelo é uma sugestão fácil de preparar, e muito deliciosa, para o lanche da tarde.

O preparo é descomplicado, sem segredo nenhum e fica pronto rapidinho. Veja como fazer!


## Instalação

De preferencia no forno.

```bash
class BoloDeBanana:
    def __init__(self):
        self.calda = {"açúcar": 2, "água_quente": 0.5}  # em xícaras
        self.massa = {
            "ovos": 3,
            "açúcar": 2,
            "leite_quente": 1,
            "farinha_trigo": 2,
            "fermento": 1,  # em colheres de sopa
        }
        self.bananas = 6  # bananas fatiadas
        self.canela = "a gosto"  # canela em pó
        self.temperatura_forno = 180  # graus Celsius
        self.tempo_assar = 30  # minutos

    def preparar_calda(self):
        print("Passo 1: Preparando a calda...")
        print("Derretendo 2 xícaras de açúcar em fogo baixo até ficar dourado.")
        print("Adicionando meia xícara de água quente e mexendo bem.")
        print("Deixe descansar enquanto prepara a massa.")
        
    def preparar_massa(self):
        print("\nPasso 2: Preparando a massa...")
        print("Bata os ovos e o açúcar por 5 minutos até ficar bem cremoso.")
        print("Adicione 1 xícara de leite quente, 2 xícaras de farinha de trigo e 1 colher de fermento em pó.")
        print("Misture tudo com um fouet até ficar homogêneo.")
    
    def montar_bolo(self):
        print("\nPasso 3: Montando o bolo...")
        print(f"Na forma com a calda, coloque {self.bananas} bananas fatiadas.")
        print("Despeje a massa sobre as bananas e polvilhe canela a gosto.")
        
    def assar(self):
        print("\nPasso 4: Assando o bolo...")
        print(f"Leve para assar em forno preaquecido a {self.temperatura_forno} graus Celsius por {self.tempo_assar} minutos.")
    
    def desenformar_e_servir(self):
        print("\nPasso 5: Finalizando...")
        print("Desenforme o bolo enquanto ele ainda está morno.")
        print("Sirva imediatamente. Aproveite o bolo de banana!")

def preparar_bolo_de_banana():
    bolo = BoloDeBanana()
    bolo.preparar_calda()
    bolo.preparar_massa()
    bolo.montar_bolo()
    bolo.assar()
    bolo.desenformar_e_servir()

# Executando a receita
preparar_bolo_de_banana()


```
    
## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de bolosgostosos@gmail.com

