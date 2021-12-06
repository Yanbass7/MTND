class Linguagem:
    def __init__(self):
        self.estados = []
        self.simb = []
        self.alfabPilha = []
        self.dicionario = dict()
        self.wordTeste = []
        self.estadosFinais = []
        self.pilhaTransicoes = []
        self.limitEsquerda = ''
        self.simbBranco = ''

    def lerTrans(self, num):
        for i in range (0, num):
            trans = input().split()
            self.criarDic(trans)

    def criarDic(self, trans):
        dupla = trans[0]+trans[1]
        if(dupla in self.dicionario):
            self.dicionario[dupla] = self.dicionario[dupla] + [[trans[2],trans[3], trans[4]]]
        else:
            novaTrans = {trans[0]+trans[1]:[[trans[2],trans[3], trans[4]]]}
            self.dicionario.update(novaTrans)


    def escrever(self, fita, caractere, registrador):
      nova_fita = fita.copy()
      nova_fita[registrador] = caractere
      return nova_fita

    def mover(self, fita, registrador, direcao):
      if(direcao == 'I'):
        return registrador
      elif(direcao == 'E'):
        if(registrador == 0):
          return registrador
        return registrador - 1
      elif(direcao == 'D'):
        if(len(fita)-1 == registrador):
          fita.append(self.simbBranco)
        return  registrador + 1

    def validarTransicao(self, estadoAtual, fita, registrador, pilhaTrans):
        parou = True
        caractereLido = fita[registrador]
        if((estadoAtual+caractereLido) in self.dicionario):
          parou = False
          duplas = self.dicionario.get(estadoAtual+caractereLido)
          for dupla in duplas:
           novoRegistrador = self.mover(fita, registrador, dupla[2])
           pilhaTrans.append([dupla[0], self.escrever(fita, dupla[1], registrador), novoRegistrador])
        
        return parou

   

    def isAccepted(self, estado, parou):
      if(parou and estado in self.estadosFinais):
        return True
      else:
        return False


    def percorrerPilhaTrans(self, palavra, estadoInicial):
        fita = list(palavra)
        fita.insert(0, self.limitEsquerda)
        fita.append(self.simbBranco)
        self.pilhaTrans = [[estadoInicial, fita, 1]]
        aceita = False
        while (not (len(self.pilhaTrans)==0)):
            novaPilhaTrans = []
            for pilha in self.pilhaTrans:  
              parou = self.validarTransicao(pilha[0], pilha[1], pilha[2], novaPilhaTrans)
              if(self.isAccepted(pilha[0], parou)):
                aceita = True
                break

            if(aceita):
              break
            self.pilhaTrans = novaPilhaTrans
       
        
        if(aceita):
            print('S')
        else:
            print('N')
            

L1 = Linguagem()
L1.estados = input()
L1.simb = input()
L1.alfabPilha = input()
L1.limitEsquerda = input()
L1.simbBranco = input()
numeroTransicoes = int(input())
L1.lerTrans(numeroTransicoes)
estadoInicial = input()
L1.estadosFinais = input().split()
L1.wordTeste = input().split()


for words in L1.wordTeste:
   
    L1.percorrerPilhaTrans(words, estadoInicial)