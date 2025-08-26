#!/bin/usr/env python3

import sys
import csv
import tkinter
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from tkinterweb import HtmlFrame # from tkinterweb import HtmlFrame
from tkinterweb import bindings  #tkinter só roda como executável, sem interface pyscript
class Janela(tkinter.Frame):
    """
    AXIS padrão é 100, para deslocar para cima, substraia um valor e
    para baixo, adicione um valor.

    Deslocar o AYIS para esquerda, substraia, e adicione para deslocar
    para direita
    """
    AXIS = 100 #AXIS = 100
    AYIS = 100 #AYIS = 100

    opcoesComboBox = list(range(1, 6))

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master

        self.pack(fill=tkinter.BOTH, expand=1)
        botaoSair = tkinter.Button(self, text="Sair",
                                   command=self.clickBotaoSair)
        botaoSalvar = tkinter.Button(self, text="Salvar",
                                     command=self.clickBotaoSalvar)
        botaoProximo = tkinter.Button(self, text="Proximo",
                                      command=self.clickBotaoProximo)
        botaoCarregar = tkinter.Button(self, text="Carregar",
                                       command=self.clickCarregarMatriz)

        self.setLabels()
        self.setCampos()

        botaoSalvar.place(x=self.AXIS-20, y=self.AYIS+36)
        botaoProximo.place(x=self.AXIS+45, y=self.AYIS+36)
        botaoCarregar.place(x=self.AXIS-20, y=self.AYIS+66) #+66
        botaoSair.place(x=self.AXIS+55, y=self.AYIS+66) #+66

    def setCampos(self):
        """
        Desenha os campos de entrada no Frame, e configura os 'comboboxes'(?)
        tornando-os apenas como leitura
        """
        self.textoTarefa = tkinter.Entry(self)
        self.textoTarefa.place(x=self.AXIS+10, y=self.AYIS-60)

        self.comboGravidade = Combobox(self, values=self.opcoesComboBox,
                                       state='readonly')
        self.comboGravidade.place(x=self.AXIS+10, y=self.AYIS-40)
        self.comboGravidade.current(0)

        self.comboUrgencia = Combobox(self, values=self.opcoesComboBox,
                                      state='readonly')
        self.comboUrgencia.place(x=self.AXIS+10, y=self.AYIS-20)
        self.comboUrgencia.current(0)

        self.comboTendencia = Combobox(self, values=self.opcoesComboBox,
                                       state='readonly')
        self.comboTendencia.place(x=self.AXIS+10, y=self.AYIS)
        self.comboTendencia.current(0)

    def setLabels(self):
        """
        Posiciona os labels no Frame
        """
        textFrame = "Insira a tarefa que se deseja calcular o G.U.T."
        self.labelTendencia = tkinter.Label(self, text=textFrame)
        self.labelTendencia.place(x=self.AXIS-50, y=self.AYIS-100)

        self.labelTarefa = tkinter.Label(self, text="Tarefa")
        self.labelTarefa.place(x=self.AXIS-55, y=self.AYIS-60)

        self.labelGravidade = tkinter.Label(self, text="Gravidade")
        self.labelGravidade.place(x=self.AXIS-55, y=self.AYIS-40)

        self.labelUrgencia = tkinter.Label(self, text="Urgência")
        self.labelUrgencia.place(x=self.AXIS-55, y=self.AYIS-20)

        self.labelTendencia = tkinter.Label(self, text="Tendência")
        self.labelTendencia.place(x=self.AXIS-55, y=self.AYIS)

    def clickBotaoSair(self):
        self.destroy()
        sys.exit()

    def clickBotaoProximo(self):
        tarefa = str(self.textoTarefa.get())
        gravidade = int(eval(self.comboGravidade.get()))
        urgencia = int(eval(self.comboUrgencia.get()))
        tendencia = int(eval(self.comboTendencia.get()))

        insercao(resultList, gut(tarefa, gravidade, urgencia, tendencia))

        labelSalvo = tkinter.Label(self,
                                   text=f"{len(resultList)} entrada(s) salva(s)!")
        labelSalvo.place(x=self.AXIS, y=self.AYIS+20)

        self.textoTarefa.delete(0, "end")

    def clickBotaoSalvar(self):
        tempList = []
        with open("matrixGut.csv", mode="w") as tasks:
            file = csv.writer(tasks, delimiter=",", quotechar='"',
                              quoting=csv.QUOTE_MINIMAL)
            file.writerow(["Tarefa", "Peso"])

            for i in range(len(resultList)):
                file.writerow([resultList[i][0], resultList[i][1]])
                tempList.append(
                    f"Tarefa: {resultList[i][0]} -> peso: {resultList[i][1]}")
        self.popUpTasks(tempList)

    def popUpTasks(self, taskList: list):
        showinfo("Resultado da matriz", "\n".join(taskList))

    def clickCarregarMatriz(self):
        self.arq = None
        janelaCarregar = tkinter.Toplevel(self)
        janelaCarregar.wm_title("Load...")
        janelaCarregar.geometry("300x250") #200x150

        tempLabel = tkinter.Label(janelaCarregar,
                                  text="Entre com a caminho\ndo arquivo .csv")
        tempLabel.place(x=self.AXIS-50, y=self.AYIS-80)

        tempEntry = tkinter.Entry(janelaCarregar)
        tempEntry.place(x=self.AXIS-50, y=self.AYIS-40)

        def carregarArq():
            self.arq = str(tempEntry.get())

            with open(self.arq, mode="r") as tasks:
                csvFile = csv.reader(tasks, delimiter=",")
                cabecalho = True

                for row in csvFile:
                    if not cabecalho:
                        insercao(resultList, (row[0], int(row[1])))
                    else:
                        cabecalho = False

            janelaCarregar.destroy()

        tempBotao = tkinter.Button(janelaCarregar, text="Carregar",
                                   command=carregarArq)
        tempBotao.place(x=self.AXIS-50, y=self.AYIS-18)


def gut(label: str, gravidade: int, urgencia: int, tendencia: int) -> tuple:
    """
    Função para calcular G.U.T.
    Retorna uma tupla com o nome e o peso calculado
    """
    if gravidade > 5:
        gravidade = 5
    elif gravidade < 1:
        gravidade = 1

    if urgencia > 5:
        urgencia = 5
    elif urgencia < 1:
        urgencia = 1

    if tendencia > 5:
        tendencia = 5
    elif tendencia < 1:
        tendencia = 1

    resultado = gravidade * urgencia * tendencia
    return (label, resultado)


def insercao(lista: list, novoItem: tuple):
    """
    Insere em ordem decrescente em uma lista
    """
    if len(lista) == 0:
        lista.append(novoItem)
        return

    for i in range(len(lista)):
        if novoItem not in lista and novoItem[1] >= lista[i][1]:
            lista.insert(i, novoItem)
        elif novoItem not in lista:
            lista.append(novoItem)


resultList = []
root = tkinter.Tk()
frame = HtmlFrame(root) #create HTML browser #frame = HtmlFrame(root)
#frame.load_website("https://liviarqsoares.github.io") #load a website
#frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
app = Janela(root)
app.pack(side="top", fill="both", expand=True)
root.wm_title("Matriz G.U.T.")
root.geometry("400x300") #root.geometry("290x200")
root.iconphoto(False, tkinter.PhotoImage(file='matrix.png')) #False
root.mainloop()