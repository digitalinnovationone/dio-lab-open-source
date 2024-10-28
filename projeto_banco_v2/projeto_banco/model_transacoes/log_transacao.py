import textwrap
# from abc import ABC, abstractclassmethod, abstractproperty
from abc import ABC, classmethod, abstractmethod
from datetime import datetime

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado

    return envelope