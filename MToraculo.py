from  CI import  ci
import sys

DicEstado = {}
DicChar = {}

FilaExec = []

def Leitura(nome):
# Abre Arquivo para leitura e cria uma lista de Linhas
    try:
        arquivo = open(nome, 'r')

        codigo = arquivo.readlines()

        arquivo.close()
# Trata Excecao quando o nome do arquivo e invalido
    except:
        print("Arquivo Invalido")
        exit(0)


# Laço para varrer cada linha do codigo
    for linha in codigo:


        if linha.startswith(';'):
            continue
    
        elif linha.startswith('\t'):
            Cria_Estados(linha)


        elif linha.startswith('\n'):
            continue

        else:
            print('Comando'+ repr(linha) +'invalido' )
            exit(0)



# Cria dicionario de Estados
def Cria_Estados(linha):
	global DicEstado
	global DicChar
	comand = linha.split()

	if (len(comand) == 5):
    	#comando normal
		lista = [comand[2],comand[3],comand[4]]	

		DicChar = {comand[1]:lista}
		DicEstadoA = {comand[0]:DicChar}

		if comand[0] in DicEstado:
			aux = DicEstado[comand[0]]
			#print('aux',aux)
			if comand[1] in aux:
				aux2 = aux[comand[1]]
				aux2 = [aux2,lista]
				aux3 = {comand[1]:aux2}
				aux.update(aux3)
				DicEstadoA = {comand[0]:aux}
				DicEstado.update(DicEstadoA)
			else:
				DicEstado[comand[0]].update(DicChar)            
		else:
			
			DicEstado.update(DicEstadoA)		
	elif(len(comand) == 6):
	#comando normal ! no fim
		lista = [comand[2],comand[3],comand[4],comand[5]]	

		DicChar = {comand[1]:lista}
		DicEstadoA = {comand[0]:DicChar}

		if comand[0] in DicEstado:
			aux = DicEstado[comand[0]]
			if comand[1] in aux:
				aux2 = aux[comand[1]]
				aux2 = [aux2,lista]
				aux3 = {comand[1]:aux2}
				aux.update(aux3)
				DicEstadoA = {comand[0]:aux}
				DicEstado.update(DicEstadoA)
			else:
				DicEstado[comand[0]].update(DicChar)            
		else:
			
			DicEstado.update(DicEstadoA)
	else:
		print('Comando:',comand,'inválido.')		


	print(DicEstado)        


def executaIntrucao(CI):

	global FilaExec

	estadoAtual = CI.get_estadoAtual()
	fita = CI.get_fita()
	posCabecote = CI.get_posCabecote() 
		
	#if()

	print(estadoAtual)
	instExec = DicEstado[estadoAtual]
	charCabecote = fita[posCabecote]

    
	if(charCabecote in instExec):
    	

		auxinstExec = instExec[charCabecote]

		if not isinstance(auxinstExec[0],list):
			auxinstExec = [auxinstExec]
			#print(auxinstExec)
		for i in auxinstExec:

			posCabecote = CI.get_posCabecote() 


	    	#coloca novo caracter na fita caso não seja para repitilo
			if (i[0] != '*'):
				fita1 = fita[0:posCabecote]
				fita2 = fita[posCabecote+1:len(fita)]
				ch = i[0]
				fita = fita1 + ch + fita2
	        
	        #verifica se tem alteracao no cabecote
			if ( i[1] == 'l'):
				posCabecote -= 1
			elif (i[1] == 'r'):
				posCabecote += 1    

	        #atribui novo estado    
			if ( i[2] == '*'):
				EstAtual = EstAtual    
			elif ( i[2] == 'halt-accept'):
				print('Palavra aceita.')
				exit(0)
			elif(i[2] == 'halt-reject'):
				print('Palavra recusada.')
				return 1
			else:	
				EstAtual = i[2]
			
			#verifica se tem breakpoint
			if ( i[len(i)-1] == '!'):
				return 1
					
			CItemp = ci(EstAtual,fita,posCabecote)
			#print('Antes de criar novo ci na fila cima ',CItemp)
			FilaExec.append(CItemp)

	
	elif('*' in instExec):
		
		instExec = instExec['*']
		#print('entrou aki quando tem *',instExec)

		posCabecote = CI.get_posCabecote() 

		#coloca novo caracter na fita caso não seja *
		if (instExec[0] != '*'):
			fita1 = fita[0:posCabecote]
			fita2 = fita[posCabecote+1:len(fita)]
			ch = instExec[0]
			fita = fita1 + ch + fita2

        #verifica se tem alteracao no cabecote
		if ( instExec[1] == 'l'):
			posCabecote -= 1
		elif (instExec[1] == 'r'):
			posCabecote += 1

		
		 #atribui novo estados
		if ( instExec[2] == '*'):
			EstAtual = EstAtual
		elif ( instExec[2] == 'halt-accept' ):
			print('Palavra aceita')
			exit(0)
		elif(instExec[2] == 'halt-reject'):
			print('Palavra rejeitada')
			return 1

		else:
			EstAtual = instExec[2]

        #verifica se tem breakpoint
		if ( instExec[len(instExec)-1] == '!'):
			return 1	

		CItemp = ci(EstAtual,fita,posCabecote)
		#print('Antes de criar novo ci na fila baixo',CItemp)
		FilaExec.append(CItemp)    



print('Simulador de Maquina de Turing com oraculo ')
print('Desenvolvido como trabalho pratico para a disciplina de Teoria da Computacao.')
print('Italo Haylander Faria Galvão, IFMG, 2019.')
print('\n')


Leitura(sys.argv[1]) 

#todas as maquinas de touring comecaram por padrao no estado 0
EstadoAtual = '0'

#recebe a palavra incial
caracterFita = '____________________'
Fita = input('Forneca a palavra inicial: ')
Fita = caracterFita + Fita + caracterFita
posCabecote = 20    




CIini = ci(EstadoAtual,Fita,posCabecote)

FilaExec.append(CIini)


while FilaExec:

	for i in FilaExec:
		print(i)
	executaIntrucao(FilaExec.pop(0))







