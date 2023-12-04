#!/usr/bin/env python3
from math import sqrt
from decimal import Decimal, getcontext
getcontext().prec = 3

class Ondas:
    def __init__(self, T, t, n, f, lb, V, v, F, mi, m, l):
        self.T = T # período
        self.t = t # tempo
        self.n = n # número de oscilações
        self.f = f # frequência
        self.lb = lb # comprimento da onda (lambda)
        self.V = V # velocidade de propagação da onda
        self.v = v # velocidade da onda em cordas
        self.F = F # força de tração na corda
        self.mi = mi # densidade linear de massa
        self.m = m # massa da corda
        self.l = l # comprimento da corda

    @classmethod
    def lista(cls):
        print('\n\nA lista estará da seguinte maneira:\nabreviação: o que significa\nDigite no formato abreviação:valor')
        print('T: Período (s)\nt: Tempo (s)\nn: Número de oscilações\nf: Frequência (Hz)\nlb: Comprimento da onda (m)')
        print('V: Velocidade de propagação da onda (m/s)\nv: Velocidade da onda em cordas (m/s)\nF: Força de tração na corda N')
        print('mi: Densidade linear de massa (kg/m)\nm: Massa da corda (kg)\nl: Comprimento da corda (m)')

    @classmethod
    def anotar(cls, nome, resultado):
        a = f'Resultados\n\nPeríodo: {resultado["T"]} s\nTempo: {resultado["t"]} s\nNúmero de oscilações: {resultado["n"]}\n'
        b = f'Frequência: {resultado["f"]} Hz\nComprimento da onda: {resultado["lb"]} m\nVelocidade de propagação da onda: {resultado["V"]} m/s\n'
        c = f'Velocidade da onda em cordas: {resultado["v"]} m/s\nForça de tração na corda: {resultado["F"]} N\n'
        d = f'Densidade linear de massa: {resultado["mi"]} kg/m\nMassa da corda: {resultado["m"]} kg\nComprimento da corda: {resultado["l"]} m'
        texto = a + b + c + d + '\n'
        with open(f'{nome}.txt', 'w', encoding='utf-8') as f: f.write(texto)

    def solve(self):
        for _ in range(2):
            self._periodo()
            self._tempo()
            self._n()
            self._frequencia()
            self._vpo()
            self._lambda()
            self._voc()
            self._forca()
            self._mi()
            self._massa()
            self._comprimento()

        result = {
           'T': self.T,
           't': self.t,
           'n': self.n,
           'f': self.f,
           'lb': self.lb,
           'V': self.V,
           'v': self.v,
           'F': self.F,
           'mi': self.mi,
           'm': self.m,
           'l': self.l
        }

        return result

    def _periodo(self):
        if not self.T:
            try:
                self.T = self.t / self.n
            except (ValueError, TypeError):
                try:
                    self.T = self.f ** -1
                except (ValueError, TypeError):
                    try:
                        self.T = self.lb / self.V
                    except (ValueError, TypeError):
                        self.T = None

    def _tempo(self):
        if not self.t:
            try:
                self.t = self.T * self.n
            except (ValueError, TypeError):
                try:
                    self.t = self.n / self.f
                except (ValueError, TypeError):
                    self.t = None

    def _n(self):
        if not self.n:
            try:
                self.n = self.t / self.T
            except (ValueError, TypeError):
                try:
                    self.n = self.f * self.t
                except (ValueError, TypeError):
                    self.n = None

    def _frequencia(self):
        if not self.f:
            try:
                self.f = self.n / self.t
            except (ValueError, TypeError):
                try:
                    self.f = self.T ** -1
                except (ValueError, TypeError):
                    try:
                        self.f = self.V / self.lb
                    except (ValueError, TypeError):
                        self.f = None
    def _lambda(self):
        if not self.lb:
            try:
                self.lb = self.V / self.f
            except (ValueError, TypeError):
                try:
                    self.lb = self.V * self.T
                except (ValueError, TypeError):
                    self.lb = None

    def _vpo(self):
        if not self.V:
            try:
                self.V = self.lb * self.f
            except (ValueError, TypeError):
                try:
                    self.V = self.lb / self.T
                except (ValueError, TypeError):
                    self.V = None

    def _voc(self):
        if not self.v:
            try:
                self.v = sqrt(self.F / self.mi)
            except (ValueError, TypeError):
                self.v = None

    def _mi(self):
        if not self.mi:
            try:
                self.mi = self.m / self.l
            except (ValueError, TypeError):
                 try:
                     self.mi = self.F / (self.v ** 2)
                 except (ValueError, TypeError):
                     self.mi = None

    def _forca(self):
        if not self.F:
            try:
                self.F = (self.v ** 2) * self.mi
            except (ValueError, TypeError):
                self.F = None

    def _massa(self):
        if not self.m:
            try:
                self.m = self.mi * self.l
            except (ValueError, TypeError):
                self.m = None

    def _comprimento(self):
        if not self.l:
            try:
                self.l = self.m / self.mi
            except (ValueError, TypeError):
                self.l = None

def header(num):
    print('┅'*num)

def muda_virgula(num):
    return num.replace(',', '.')

def main():
    header(35)
    print('  Calculadora de Ondas!')
    header(35)
    print('\nDeseja ver a lista de abreviações ou quer começar agora?\n')
    print('[0] - Ver a lista de abreviações\n[1] - Começar sem ver a lista\n')
    choice = int(input('>>> '))
    if choice == 0: Ondas.lista()
    elif choice == 1: pass
    else:
        print('Insira um valor válido. Tente novamente.')
        exit()
    
    print('\nDigite as informações que você possui de acordo com a lista de abreviações. Digite "q" se tiver terminado.\n')
    
    k = ['T', 't', 'n', 'f', 'lb', 'V', 'v', 'F', 'mi', 'm', 'l']
    info = dict.fromkeys(k)
    del k

    while True:
        comp = input('>>> ').strip()

        if comp == 'q':
            break

        key, value = comp.split(':')

        if ',' in value:
            value = muda_virgula(value)

        if key in info:
            info[key] = Decimal(value)
            continue

        print('Digite uma informação válida!')

    matemaquina = Ondas(**info)
    info = matemaquina.solve()
    print('\n')
    header(35)
    print('  Resultados')
    header(35)
    print()
    print(f'  Período: {info["T"]} s')
    print(f'  Tempo: {info["t"]} s')
    print(f'  Número de oscilações: {info["n"]}')
    print(f'  Frequência: {info["f"]} Hz')
    print(f'  Comprimento da onda: {info["lb"]} m')
    print(f'  Velocidade de propagação da onda: {info["V"]} m/s')
    print(f'  Velocidade da onda em corda: {info["v"]} m/s')
    print(f'  Força de tração na corda: {info["F"]} N')
    print(f'  Densidade linear de massa: {info["mi"]} kg/m')
    print(f'  Massa da corda: {info["m"]} kg')
    print(f'  Comprimento da corda: {info["l"]} m')
    print('\n\nVocê quer escrever os resultados num arquivo de texto?\n\n[0] - Sim\n[1] - Não\n')
    choice = int(input('>>> ').strip())
    if choice == 0:
        print('\nQual será o nome do arquivo?\n')
        nome = input('>>> ').strip()
        Ondas.anotar(nome, info)
        print(f'\nResultados salvos no arquivo {nome}.txt!')
    elif choice == 1: pass
    else: print('Opção inválida. Operação cancelada.')

    print('\nObrigado por usar!\nFeito por: Cristian (aka Canário)')

if __name__ == '__main__':
    main()
