import random
import matplotlib.pyplot

contGeracaoAceita = 0
contPior = 0
contmedio17 = 0
contmedio18 = 0
contmedio19 = 0
contmedio20 = 0
contotimo27 = 0

def GeracaoAceita():
    global contGeracaoAceita
    contGeracaoAceita = contGeracaoAceita + 1

def GeracaoPior():
    global contPior
    contPior = contPior + 1

def GeracaoMedia17():
    global contmedio17
    contmedio17 = contmedio17 + 1

def GeracaoMedia18():
    global contmedio18
    contmedio18 = contmedio18 + 1

def GeracaoMedia19():
    global contmedio19
    contmedio19 = contmedio19 + 1

def GeracaoMedia20():
    global contmedio20
    contmedio20 = contmedio20 + 1

def GeracaoOtimo27():
    global contotimo20
    contotimo20 = contotimo20 + 1



def Fitness(FilsUn): # Filho Um

    #Liste Parfait

    ListaPerfeita = [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1]

    #vérifier liste parfait
    if (FilsUn == ListaPerfeita):
        print("Lista FilhoUm é compatível:")

    # Tout sauf un
    SignalSortieFilsUn = 9 + FilsUn[1] * FilsUn[4] - FilsUn[22] * FilsUn[13] + FilsUn[23] * FilsUn[3] - FilsUn[
        20] * \
                        FilsUn[9] + FilsUn[35] * FilsUn[14] - FilsUn[10] * FilsUn[25] + FilsUn[15] * FilsUn[16] + \
                        FilsUn[2] * FilsUn[32] + FilsUn[27] * FilsUn[18] + FilsUn[11] * FilsUn[33] - FilsUn[30] * \
                        FilsUn[31] - FilsUn[21] * FilsUn[24] + FilsUn[34] * FilsUn[26] - FilsUn[28] * FilsUn[6] + \
                        FilsUn[7] * FilsUn[12] - FilsUn[5] * FilsUn[8] + FilsUn[17] * FilsUn[19] - FilsUn[0] * \
                        FilsUn[
                            29] + FilsUn[22] * FilsUn[3] + FilsUn[20] * FilsUn[14] + FilsUn[25] * FilsUn[15] + \
                        FilsUn[
                            30] * FilsUn[11] + FilsUn[24] * FilsUn[18] + FilsUn[6] * FilsUn[7] + FilsUn[8] * \
                        FilsUn[
                            17] + FilsUn[0] * FilsUn[32]

    if (SignalSortieFilsUn == 27):
        print("POKEMON accepté avec mieux résultat ( SUPER ): ", SignalSortieFilsUn)
        print("DNA de POKEMON: ",FilsUn)
        GeracaoOtimo27()
        GeracaoAceita()
    elif(SignalSortieFilsUn == 20):
        print("POKEMON accepté avec un résultat ( BON )", SignalSortieFilsUn)
        print("DNA de POKEMON: ", FilsUn)
        GeracaoMedia20()
        GeracaoAceita()
    elif(SignalSortieFilsUn == 19):
        print("POKEMON accepté avec un résultat ( BON )", SignalSortieFilsUn)
        print("DNA de POKEMON: ", FilsUn)
        GeracaoMedia19()
        GeracaoAceita()
    elif(SignalSortieFilsUn == 18):
        print("POKEMON accepté avec un résultat ( BON )", SignalSortieFilsUn)
        print("DNA de POKEMON: ", FilsUn)
        GeracaoMedia18()
        GeracaoAceita()
    elif(SignalSortieFilsUn == 17):
        print("POKEMON accepté avec un résultat ( BON )", SignalSortieFilsUn)
        print("DNA de POKEMON: ", FilsUn)
        GeracaoMedia17()
        GeracaoAceita()
    elif(SignalSortieFilsUn == 4):
        print("POKEMON rejeté avec un résultat ( Pior )", SignalSortieFilsUn)
        print("DNA de POKEMON: ", FilsUn)
        GeracaoPior()
    else:
        print("POKEMON pas de classification", SignalSortieFilsUn)
    FilsUn.clear()



def Croisement(GenerationX, GenerationY,coupe): # Geração X, Geração Y, Corte
    FilsUn = []
    for i in range(0, coupe):
        FilsUn.append(GenerationX[i])
    for i in range(coupe, 36):
        FilsUn.append(GenerationY[i])
    GenerationX.clear()
    GenerationY.clear()
    Fitness(FilsUn)   # Filho UM


def Selecao(Generation,parite,coupe): #Geração , paridade , corte
    GenerationX = []
    GenerationY = []
    for compte in range(parite):
        if (Generation == []):
            break
        else:
            print("gerado vez: ", compte)
            for i in range(0, 36):
                GenerationY.append(Generation[i])
            for i in range(36, 72):
                GenerationX.append(Generation[i])
            print("")
        del (Generation[0:72])
        Croisement(GenerationX, GenerationY, coupe) # Geração X, Geração Y, Corte



def Geracao(repetition,coupe):  # Repetição , Corte
    Generation = []
    for cont in range(repetition):
        for i in range(0, 36):
            b = random.randint(0, 1)
            Generation.append(b)
    if (repetition % 2 == 0):
        parite = repetition
    else:
        parite = repetition - 1
        del (Generation[0:36])
    Selecao(Generation,parite,coupe)  #Geração , paridade , corte



# Ici commence
repetition = int(input("Escolha um número para a quantidade de cruzamento aleatório: "))
coupe = int(input("Escolha o corte:"))
Geracao(repetition,coupe)  # Repetição , Corte

print("Número de gerações Aceitas: ", contGeracaoAceita)


EstadosFitness = ["Pior 4","medio 17","medio 18","medio 19","medio 20", "Otimo 27"]

Resultad = [contPior, contmedio17, contmedio18, contmedio19, contmedio20, contotimo27]

matplotlib.pyplot.bar(EstadosFitness, Resultad)
matplotlib.pyplot.show()
