"""
Bernardo Paulsen
Jogo Paciencia

"""
import os
import random
import time

class Pilha():

    def __init__(self,
        ativas  : list ,
        viradas : list):

        self.ativas  = [ativas]
        self.viradas = viradas

    def virar_carta(self):
        if not self.ativas:
            if self.viradas:
                carta = self.viradas[-1]
                self.ativas.append([carta])
                self.viradas.remove(carta)

    def adicionar_cartas(self,cartas):
        if not self.ativas:
            self.ativas.append(cartas)
        elif cartas[0] == self.ativas[-1][-1] - 1:
            self.ativas[-1].extend(cartas)
        else:
            self.ativas.append(cartas)

    def tirar_cartas(self,cartas):
        if cartas == self.ativas[-1]:
            self.ativas.remove(self.ativas[-1])
        else:
            for carta in cartas:
                self.ativas[-1].remove(carta)

    def remover_completo(self):
        if self.ativas:
            if len(self.ativas[-1]) == 13:
                self.ativas.remove(self.ativas[-1])
                return True
            return False



class Ambiente():

    SIMBOLOS =  {0:' A',
        1:' 2',  2:' 3',
        3:' 4',  4:' 5',
        5:' 6',  6:' 7',
        7:' 8',  8:' 9',
        9:'10',  10:' J',
        11:' Q', 12:' K'}

    def __init__(self):

        self.aleatorio = self.tirar_numero()
        self.pilhas    = self.criar_pilhas(self.aleatorio)
        self.montes    = self.criar_montes(self.aleatorio)
        del self.aleatorio


    def distribuir_monte(self):
        cartas = self.montes[-1]
        for i in range(len(cartas)):
            self.pilhas[i].adicionar_cartas([cartas[i]])
        self.montes.remove(cartas)


    @staticmethod
    def criar_pilhas(aleatorio):
        lugar = [6,6,6,6,5,5,5,5,5,5]
        mesa  = [[] for i in range(10)]
        a     = 0
        for i, n in zip(range(len(lugar)),lugar):
            mesa[i]  = Pilha(aleatorio[a+n-1:a+n],aleatorio[a:a+n-1])
            a       += n
        return mesa

    @staticmethod
    def tirar_numero():
        cartas   = [i for i in range(13) for a in range(8)]
        lista  = []
        for i in range(len(cartas)):
            rand = random.randint(0,len(cartas)-1)
            numero = cartas[rand]
            lista.append(numero)
            cartas.remove(numero)
        return lista

    @staticmethod
    def criar_montes(aleatorio):
        a = 54
        montes = [[],[],[],[],[]]
        for i in range(5):
            montes[i] = aleatorio[a:a+10]
            a += 10
        return montes

    
    def maior_pilha(self):
        total  = 0
        total += len(self.montes)
        for pilha in self.pilhas:
            lenght = len(pilha.ativas) + len(pilha.viradas)
            for carta in pilha.ativas:
                lenght += len(carta)
            if lenght > total:
                total = lenght
        return total

    def criar_listas(self,total):
        listas = []
        lista = ['--' for i in range(len(self.montes))]
        for i in range(total-len(lista)):
            lista.append('  ')
        listas.append(lista)
        for lugar in self.pilhas:
            lista = []
            for virada in lugar.viradas:
                lista.append('--')
            for ativa in lugar.ativas:
                lista.append('  ')
                for carta in ativa:
                    lista.append(self.SIMBOLOS[carta])
            for i in range(total-len(lista)):
                lista.append('  ')
            listas.append(lista)
        return listas 
    
    def printar(self):
        total  = self.maior_pilha()
        listas = self.criar_listas(total)
        os.system('clear')
        for i in range(11):
            if i < 10:
                print(f'{i} ',end='  ')
            if i == 10:
                print(f'{i}')
        print()
        for i in range(total):
            for lista in listas:
                print(lista[i],end='  ')
            print()


class Jogo():

    def __init__(self):
        
        self.ambiente = Ambiente()

        self.jogar()
    
    def jogar(self):

        completos = 0

        while True:
            self.ambiente.printar()
            if completos == 8:
                print('GANHOOUUUUUUU')
                break
            try:
                print()
                print()
                a = self.input_numero_coluna()
                if a == 0:
                    self.ambiente.distribuir_monte()
                elif a > 10:
                    break
                else:
                    try:
                        b = self.input_numero_carta()
                        c = self.input_numero_coluna()
                        pilha  = self.ambiente.pilhas[a-1]
                        bloco  = pilha.ativas[-1]
                        cartas = bloco[bloco.index(b-1):]
                        self.ambiente.pilhas[c-1].adicionar_cartas(cartas)
                        self.ambiente.pilhas[a-1].tirar_cartas(cartas)
                    except:
                        pass
            except: pass
            for pilha in self.ambiente.pilhas:
                a = pilha.remover_completo()
                pilha.virar_carta()
                if a == True:
                    completos += 1


    def input_numero_coluna(self):
        return int(input('Digite numero da coluna: '))

    def input_numero_carta(self):
        imp = input('Digite o (a) numero (letra) da carta: ')
        lower = imp.lower()
        if lower == 'a':
            return 1
        if lower == 'j':
            return 11
        if lower == 'q':
            return 12
        if lower == 'k':
            return 13
        else:
            return int(imp)



a = Jogo()
