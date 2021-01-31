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

    def adicionar_cartas(self, cartas: list):
        if not self.ativas:
            self.ativas.append(cartas)
        elif cartas[0] == self.ativas[-1][-1] - 1:
            self.ativas[-1].extend(cartas)
        else:
            self.ativas.append(cartas)

    def remover_completo(self):
        if self.ativas:
            if len(self.ativas[-1]) == 13:
                self.ativas.remove(self.ativas[-1])
                return True
            return False

    def tirar_cartas(self, cartas: list):
        if cartas == self.ativas[-1]:
            self.ativas.remove(self.ativas[-1])
        else:
            for carta in cartas:
                self.ativas[-1].remove(carta)

    def virar_carta(self):
        if not self.ativas:
            if self.viradas:
                carta = self.viradas[-1]
                self.ativas.append([carta])
                self.viradas.remove(carta)


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
        self.montes    = self.criar_montes(self.aleatorio)
        self.pilhas    = self.criar_pilhas(self.aleatorio)
        del self.aleatorio

    def criar_listas(self, total: int) -> list:
        listas = []
        lista = ['--' for i in range(len(self.montes))]
        for _ in range(total-len(lista)):
            lista.append('  ')
        listas.append(lista)
        for lugar in self.pilhas:
            lista = []
            for _ in lugar.viradas:
                lista.append('--')
            for ativa in lugar.ativas:
                lista.append('  ')
                for carta in ativa:
                    lista.append(self.SIMBOLOS[carta])
            for _ in range(total-len(lista)):
                lista.append('  ')
            listas.append(lista)
        return listas 

    def distribuir_monte(self):
        cartas = self.montes[-1]
        for i in range(len(cartas)):
            self.pilhas[i].adicionar_cartas([cartas[i]])
        self.montes.remove(cartas)

    def maior_pilha(self) -> int:
        total  = 0
        total += len(self.montes)
        for pilha in self.pilhas:
            lenght = len(pilha.ativas) + len(pilha.viradas)
            for carta in pilha.ativas:
                lenght += len(carta)
            if lenght > total:
                total = lenght
        return total
    
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
        print()
        print()

    @staticmethod
    def criar_montes(aleatorio : list) -> list:
        a = 54
        montes = [[],[],[],[],[]]
        for i in range(5):
            montes[i] = aleatorio[a:a+10]
            a += 10
        return montes

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
    def tirar_numero() -> list:
        cartas   = [i for i in range(13) for a in range(8)]

        lista  = []
        for i in range(len(cartas)):
            rand = random.randint(0,len(cartas)-1)
            numero = cartas[rand]
            lista.append(numero)
            cartas.remove(numero)
        return lista


class Jogo():


    ENTRADA = {'a': 0,
        '2': 1, '3': 2,
        '4': 3, '5': 4,
        '6': 5, '7': 6,
        '8': 7, '9': 8,
        '10': 9, 'j': 10,
        'q': 11, 'k': 12}

    MENSAGENS = {'coluna': 'Digite numero da coluna: ',
        'zero_dez': 'Digite um número de 0 a 10.',
        'um_dez'  : 'Digite um número de 1 a 10.',
        'carta'   : 'Digite o (a) numero (letra) da carta: ',
        'win'     : 'GANHOOUUUUUUU',
        'inv'     : 'Carta inválida.'}

    def __init__(self):

        self.ambiente    = Ambiente()

        self.completos   = 0
        self.num_jogadas = 0

        self.jogar()
    
    def jogar(self):
        start = time.time()
        while True:
            now = time.time()
            self.ambiente.printar()
            if self.completos == 8:
                print(self.MENSAGENS['win'])
                break
            time_taken = now-start
            print('Jogada:', self.num_jogadas + 1, f'Tempo: {time_taken/60:.0f}min {time_taken%60:.0f}sec')
            print('Saida.')
            a = self.input_numero_coluna(True)
            if a == 0:
                self.ambiente.distribuir_monte()
            else:
                pilha  = self.ambiente.pilhas[a-1]
                bloco  = pilha.ativas[-1]
                b = self.input_numero_carta(bloco)
                print('Destino.')
                c = self.input_numero_coluna(False)
                pilha  = self.ambiente.pilhas[a-1]
                bloco  = pilha.ativas[-1]
                cartas = bloco[bloco.index(b):]
                if self.ambiente.pilhas[c-1].ativas:
                    if cartas[0] == self.ambiente.pilhas[c-1].ativas[-1][-1] - 1:
                        self.ambiente.pilhas[c-1].adicionar_cartas(cartas)
                        self.ambiente.pilhas[a-1].tirar_cartas(cartas)
                else:
                    self.ambiente.pilhas[c-1].adicionar_cartas(cartas)
                    self.ambiente.pilhas[a-1].tirar_cartas(cartas)
            self.remover_virar()
            self.num_jogadas += 1

    def remover_virar(self):
        for pilha in self.ambiente.pilhas:
            a = pilha.remover_completo()
            pilha.virar_carta()
            if a == True:
                self.completos += 1

    def input_numero_coluna(self, saida: bool=True) -> int:
        while True:
            try:
                inp = int(input(self.MENSAGENS['coluna']))
                if saida:
                    if inp >= 0 and inp <= 10:
                        break
                    else:
                        print(self.MENSAGENS['zero_dez'])
                else:
                    if inp >= 1 and inp <= 10:
                        break
                    else:
                        print(self.MENSAGENS['um_dez'])
            except:
                if saida:
                    print(self.MENSAGENS['zero_dez'])
                else:
                    print(self.MENSAGENS['um_dez'])
        return inp

    def input_numero_carta(self, bloco: list) -> int:
        if len(bloco) == 1:
            return bloco[0]
        else:
            while True:
                try:
                    imp = input(self.MENSAGENS['carta'])
                    lower = imp.lower()
                    n = self.ENTRADA[lower]
                    if n in bloco:
                        break
                    else:
                        print(self.MENSAGENS['inv'])
                except:
                    print(self.MENSAGENS['inv'])
            return n


a = Jogo()
