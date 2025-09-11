# funcoes_extra.py

def soma_lista(numeros):
    """
    Recebe uma lista de números e retorna a soma de todos os elementos.
    
    Exemplo:
    >>> soma_lista([1, 2, 3])
    6
    """
    return sum(numeros)
  def maior_numero(numeros):
    """
    Recebe uma lista de números e retorna o maior valor.
    
    Exemplo:
    >>> maior_numero([1, 7, 3])
    7
    """
    if numeros:
        return max(numeros)
    return None

