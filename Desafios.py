"""
Funções construídas abaixo:
Não foram chamados os parâmetros especificamente nos desafios 2, 3 e 4, para cada função
poder ser testada(chamada) a partir da linha 93, individualmente.
"""

######################################################################

#Desafio 1

def converte_bool(bool_entrada):
    #Aqui simplesmente é usado o str, que cria uma nova string baseada no objeto dado em seu parametro
    print(str(bool_entrada))


###############################################################################################

#Desafio 2

def palavra_invertida():
    string_entrada = input("Escreva uma palavra: ")
    #Aqui é usado o slice, que possui as partes de inicio(start), fim(stop) e como e quanto anda pelo dado indicado(step)
    #Por default o inicio(start) é o final da frase, e o fim(stop) é começo da frase(em string, lista ou tupla)
    #Se usa valores negativos(no step) para andar para trás em determinadas frases, por isso é usado o -1, para ir um por um de tras para frente
    print (string_entrada[None:None:-1])


################################################################################################

#Desafio 3

def testealuno():
    #As notas são pedidas e transformadas em integers
    av1 = int(input("Primeira nota do aluno: "))
    av2 = int(input("Segunda nota do aluno: "))
    #As notas são adicionadas à lista 
    notas_obtidas = [av1, av2]   
    #A média é feita a partir do acesso das notas na lista com as posições delas
    media = (notas_obtidas[0] + notas_obtidas[1])/2    
    if media >= 4 and media < 8:    #Condição criada para verificar se a média está entre 4 e 8 
        print(f"Resultado das duas primeiras notas é {media}, então terá que fazer avaliação final...")      
        af = int(input("Nota do aluno na avaliação final: "))   
        notas_obtidas.append(af)    #É adicionadas à lista
        media_af = ((notas_obtidas[0] + notas_obtidas[1]) + notas_obtidas[2])/2 #Variável para a média com a Avaliação Final
        #Se a media nova for maior ou igual a 5, o aluno aprova.
        if  media_af >= 5:
            print(f"O aluno passou com a avaliação final, ficando com {media_af}!")
        else:
            print(f"O aluno reprovou com a avaliação final, com a nota {media_af}")  
    #Se a média for abaixo de 4, o aluno reprova direto .                      
    elif media < 4.0:
        print("O aluno reprovou direto")       
    #Se for maior que 8, aprova direto.
    else:
        print("O aluno passou direto!")


################################################################################################

#Desafio 4

def testesobreviver():
    numero_balas = int(input("Quantas balas o héroi possui?: "))
    numero_dragoes = int(input("Quantos dragões ele irá lutar?: "))
    #Se o numero das balas do heroi menos o numero dos dragoes vezes 2(porque precisam de duas balas para matar um dragao)
    #For maior ou igual a zero
    if numero_balas-(numero_dragoes*2) >= 0:
        #numero de balas novo é criado removendo as balas que ja mataram os dragoes
        numero_balas = numero_balas-(numero_dragoes*2)
        print(f"O herói abateu {numero_dragoes} dragões e sobraram {numero_balas} balas, então sobreviverá! ") 
    else:
        #É definido quantos dragoes sobram através do inverso(-) de quantos dragoes faltaram ser matados
        sobra_dragoes = -((numero_balas/2) - numero_dragoes)
        #Remove sobra dragoes para o numero de dragoes original para saber quantos foram abatidos
        print(f"O herói vai morrer... e {numero_dragoes-sobra_dragoes} dragões foram abatidos")
    

################################################################################################

#Desafio 5

array_original = []

def invertir(array_original):
    #Pega todos os caracteres da array original e multiplica por -1, para inverter os números
    array_invertida = [numero * -1 for numero in array_original]
    print(f"Essa é a array original: {array_original}")
    print(f"Essa é a array após ser invertida: {array_invertida}")


####################################################################################################

#Desafio 6

primeiro_array = []
segundo_array = []

def soma_listas(primeiro_array, segundo_array):
    array_final = []
    for i, a in enumerate(primeiro_array):
        array_final.append(primeiro_array[i] + segundo_array[i])
    print(array_final)


####################################################################################################

"""
Testes dos desafios (Apague o # para testar cada desafio, adicione denovo antes de testar o proximo)
"""


  ##Desafio 1:
#converte_bool(True)
#converte_bool(False)

  ##Desafio 2:
#palavra_invertida()

  ##Desafio 3:
#testealuno()

  ##Desafio 4:
#testesobreviver()

  ##Desafio 5:
#invertir([0, -3, -4, 20, -23, 6])

  ##Desafio 6:
#soma_listas([4, 0, 6],[3, 7, 2])