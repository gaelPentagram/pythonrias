#BIBLIOTECAS
import json

#HEADER
text = "SISTEMA ESCOLAR v1.0"
tam = len(text)

print("+","-"*tam,"+")
print("|",text,"|")
print("+","-"*tam,"+")

#LISTAS COM OS DADOS FORNECIDOS
materias = []
alunos = []
professores = []

#FUNCAO PARA SALVAR OS DADOS DAS LISTAS NUM ARQUIVO JSON
def saveList():
    with open('dados.json', 'w') as arquivo:   #PARAMETRO 'W' = WRITE
        json.dump({'materias': materias, 'alunos': alunos, 'professores': professores}, arquivo)

#FUNCOES PARA CARREGAR OS DADOS DO ARQUIVO JSON
def loadList():
    global materias, alunos, professores
    try:   #TENTA CARREGAR O ARQUIVO DADOS.JSON
        with open('dados.json', 'r') as arquivo:   #PARAMETRO 'R' = READ
            dados = json.load(arquivo)   #IMPORTANDO AS LISTAS SALVAS NO JSON PARA AS LINHAS DE COD NO ARQUIVO.PY
            materias = dados['materias']
            alunos = dados['alunos']
            professores = dados['professores']
    except FileNotFoundError:   #CASO NÃO ENCONTRE O ARQUIVO JSON
        print("ARQUIVO DE DADOS NÃO ENCONTRADO! INICIANDO COM AS LISTAS VAZIAS.")


#MATERIAS
#FUNCAO PARA ADICIONAR DADOS A LISTA
def incMat():
    mat = input("DIGITE O NOME DA MATERIA: ")
    materias.append(mat)
    saveList()

#MENU DE MATERIAS       IREI COMENTAR APENAS ESTA FUNCAO, PORQUE O RESTANTE E UMA COPIA DA MESMA
#MENU PARA INDICAR AS FUNCIONALIDADES DO PROGRAMA
def optionMenuMat():
        print("\nMENU - MATERIAS")
        print("1 - INCLUIR\n2 - LISTAR\n3 - EXCLUIR \n4 - ATUALIZAR \n5 - VOLTAR")
        chooseMenu = input()
        if chooseMenu == "1":   #OPCAO INCLUIR
            incMat()    #CHAMA A FUNCAO PARA INCLUIR DADOS NA LISTA
            while True:  #LOOPING 
                chooseOption = input("DESEJA CADASTRAR MAIS UMA MATERIA?\n1 - SIM   2 - NAO\n")
                if chooseOption == "1":  #CHAMA A FUNCAO PARA INCLUIR DADOS NA LISTA NOVAMENTE
                    incMat()
                elif chooseOption == "2":  #VOLTA PARA O MENU DE OPCOES
                    print("RETORNANDO A PAGINA ANTERIOR...")
                    optionMenuMat()
                    break
                else:   #MENSAGEM DE ERRO E RETORNA AO MENU DE OPCOES
                    print("OPCAO INVALIDA! TENTE NOVAMENTE.")
                    optionMenuMat()
        elif chooseMenu == "2": #OPCAO LISTAR        RETORNA AS MATERIAS ADICIONADAS NA LISTA
            if len(materias) > 0:  #LE SE EXISTE DADOS DENTRO DA LISTA
                print("AS MATERIAS CADASTRADAS SÃO:")   #PRINT DA LISTA NA TELA
                print("ID - MATERIAS")
                for id, item in enumerate(materias, start=0):  
                    print(id, "-", item)
                optionMenuMat()
            else:   #MENSAGEM DE ERRO E RETORNA PARA O MENU DE OPCOES
                print("A LISTA DE MATERIAS ESTA VAZIA!")
                optionMenuMat()
        elif chooseMenu == "3":   #OPCAO DELETAR
            if len(materias) > 0:   #LE SE EXISTE DADOS DENTRO DA LISTA
                print("ID - MATERIAS")    #PRINT DA LISTA NA TELA
                for id, item in enumerate(materias, start=0):  
                    print(id, "-", item)
                delOption = int(input("DIGITE O ID DA MATERIA QUE DESEJA EXCLUIR: "))   #COLETA O INDICE DO ITEM
                del materias[delOption]   #DELETA O ITEM SELECIONADO
                saveList()
                optionMenuMat()
            else:
                print("A LISTA DE MATERIAS ESTA VAZIA!")
                optionMenuMat()
        elif chooseMenu == "4":  #OPCAO ATUALIZAR
            if len(materias) > 0:   #LE SE EXISTE DADOS DENTRO DA LISTA
                print("ID - MATERIAS")    #PRINT DA LISTA NA TELA
                for id, item in enumerate(materias, start=0):  
                    print(id, "-", item)
                attID = int(input("DIGITE O ID DO ITEM QUE DESEJA ATUALIZAR: "))   #COLETA O INDICE DO ITEM
                attItem = input("DIGITE A MUDANÇA QUE DESEJA FAZER: ")   #COLETA A ATUALIZACAO DO ITEM
                materias[attID] = attItem   #APLICA A MUDANCA NO ID SELECIONADO
                saveList()
                optionMenuMat()
            else:
                print("A LISTA DE MATERIAS ESTA VAZIA!")   #MENSAGEM DE ERRO E RETORNA PARA O MENU DE OPCOES
                optionMenuMat()
        elif chooseMenu == "5":   #RETORNA AO MENU PRINCIPAL
            print("RETORNANDO A PAGINA ANTERIOR...")
            mainMenu()
            navMainMenu()
        else:   #MENSAGEM DE ERRO E RETORNO DO MENU DE OPCOES
            print("ESCOLHA INVÁLIDA!")
            print("TENTE NOVAMENTE!")
            optionMenuMat()

#ALUNOS
def incAlu():
    alu = input("DIGITE O NOME DO ALUNO: ")
    alunos.append(alu)
    saveList()

def optionMenuAlu():
        print("\nMENU - ALUNOS")
        print("1 - INCLUIR\n2 - LISTAR\n3 - EXCLUIR \n4 - ATUALIZAR \n5 - VOLTAR")
        chooseMenu = input()
        if chooseMenu == "1":   #OPCAO INCLUIR
            incAlu()    
            while True: 
                chooseOption = input("DESEJA CADASTRAR MAIS UM ALUNO?\n1 - SIM   2 - NAO\n")
                if chooseOption == "1":  #CHAMA A FUNCAO PARA INCLUIR DADOS NA LISTA NOVAMENTE
                    incAlu()
                elif chooseOption == "2":  #VOLTA PARA O MENU DE OPCOES
                    print("RETORNANDO A PAGINA ANTERIOR...")
                    optionMenuAlu()
                    break
                else:  
                    print("OPCAO INVALIDA! TENTE NOVAMENTE.")
                    optionMenuAlu()
        elif chooseMenu == "2": #OPCAO LISTAR
            if len(alunos) > 0:
                print("OS ALUNOS CADASTRADAS SÃO:") 
                print("ID - ALUNOS")
                for id, item in enumerate(alunos, start=0):  
                    print(id, "-", item)
                optionMenuAlu()
            else:
                print("A LISTA DE ALUNOS ESTA VAZIA!")
                optionMenuAlu()
        elif chooseMenu == "3":   #OPCAO DELETAR
            if len(alunos) > 0:
                print("ID - ALUNOS")
                for id, item in enumerate(alunos, start=0):  
                    print(id, "-", item)
                delOption = int(input("DIGITE O ID DO ALUNO QUE DESEJA EXCLUIR: ")) 
                del alunos[delOption]  
                saveList()
                optionMenuAlu()
            else:
                print("A LISTA DE ALUNOS ESTA VAZIA!")
                optionMenuAlu()
        elif chooseMenu == "4":  #OPCAO ATUALIZAR
            if len(alunos) > 0: 
                print("ID - ALUNOS")
                for id, item in enumerate(alunos, start=0):  
                    print(id, "-", item)
                attID = int(input("DIGITE O ID DO ALUNO QUE DESEJA ATUALIZAR: "))
                attItem = input("DIGITE A MUDANÇA QUE DESEJA FAZER: ")
                alunos[attID] = attItem
                saveList()
                optionMenuAlu()
            else:
                print("A LISTA DE ALUNOS ESTA VAZIA!")   #MENSAGEM DE ERRO E RETORNA PARA O MENU DE OPCOES
                optionMenuAlu()
        elif chooseMenu == "5":   #RETORNA AO MENU PRINCIPAL
            print("RETORNANDO A PAGINA ANTERIOR...")
            mainMenu()
            navMainMenu()
        else:   #MENSAGEM DE ERRO E RETORNO DO MENU DE OPCOES
            print("ESCOLHA INVÁLIDA!")
            print("TENTE NOVAMENTE!")
            optionMenuAlu()

#PROFESSORES
def incProf():
    prof = input("DIGITE O NOME DO PROFESSOR: ")
    professores.append(prof)
    saveList()

def optionMenuProf():
        print("\nMENU - PROFESSORES")
        print("1 - INCLUIR\n2 - LISTAR\n3 - EXCLUIR \n4 - ATUALIZAR \n5 - VOLTAR")
        chooseMenu = input()
        if chooseMenu == "1":   #OPCAO INCLUIR
            incProf()    
            while True: 
                chooseOption = input("DESEJA CADASTRAR MAIS UM PROFESSOR?\n1 - SIM   2 - NAO\n")
                if chooseOption == "1":  #CHAMA A FUNCAO PARA INCLUIR DADOS NA LISTA NOVAMENTE
                    incProf()
                elif chooseOption == "2":  #VOLTA PARA O MENU DE OPCOES
                    print("RETORNANDO A PAGINA ANTERIOR...")
                    optionMenuProf()
                    break
                else:  
                    print("OPCAO INVALIDA! TENTE NOVAMENTE.")
                    optionMenuProf()
        elif chooseMenu == "2": #OPCAO LISTAR
            if len(professores) > 0:
                print("OS PROFESSORES CADASTRADOS SÃO:") 
                print("ID - MATERIAS")
                for id, item in enumerate(professores, start=0):  
                    print(id, "-", item)
                optionMenuProf()
            else:
                print("A LISTA DE PROFESSORES ESTA VAZIA!")
                optionMenuProf()
        elif chooseMenu == "3":   #OPCAO DELETAR
            if len(professores) > 0:
                print("ID - PROFESSORES")
                for id, item in enumerate(professores, start=0):  
                    print(id, "-", item)
                delOption = int(input("DIGITE O ID DA MATERIA QUE DESEJA EXCLUIR: ")) 
                del professores[delOption]  
                saveList()
                optionMenuProf()
            else:
                print("A LISTA DE PROFESSORES ESTA VAZIA!")
                optionMenuProf()
        elif chooseMenu == "4":  #OPCAO ATUALIZAR
            if len(professores) > 0: 
                print("ID - PROFESSORES")
                for id, item in enumerate(professores, start=0):  
                    print(id, "-", item)
                attID = int(input("DIGITE O ID DO PROFESSOR QUE DESEJA ATUALIZAR: "))
                attItem = input("DIGITE A MUDANÇA QUE DESEJA FAZER: ")
                professores[attID] = attItem
                saveList()
                optionMenuProf()
            else:
                print("A LISTA DE PROFESSORES ESTA VAZIA!")   #MENSAGEM DE ERRO E RETORNA PARA O MENU DE OPCOES
                optionMenuProf()
        elif chooseMenu == "5":   #RETORNA AO MENU PRINCIPAL
            print("RETORNANDO A PAGINA ANTERIOR...")
            mainMenu()
            navMainMenu()
        else:   #MENSAGEM DE ERRO E RETORNO DO MENU DE OPCOES
            print("ESCOLHA INVÁLIDA!")
            print("TENTE NOVAMENTE!")
            optionMenuProf()

#FUNCAO PARA ENCERRAR O PROGRAMA
def encProg():
    print("Encerrando o programa...")
    exit()

#MENU PRINCIPAL
def mainMenu():
    print("ESCOLHA UMA OPÇÃO:\n1 - MATERIAS\n2 - ALUNOS\n3 - PROFESSORES\n4 - SAIR\n")

#ESCOLHA DE OPCAO DO MENU PRINCIPAL
def navMainMenu():
    while True:
        chooseMainMenu = input()
        if chooseMainMenu == "1":
            optionMenuMat()
        elif chooseMainMenu == "2":
            optionMenuAlu()
        elif chooseMainMenu == "3":             
            optionMenuProf()
        elif  chooseMainMenu == "4":
            encProg()
        else:   #MENSAGEM DE ERRO E RETORNO DA FUNCAO
            print("ESCOLHA INVÁLIDA!")
            print("TENTE NOVAMENTE!")
            mainMenu()
            navMainMenu()                      

#CARREGANDO DADOS
loadList()

#CHAMANDO AS FUNCOES
mainMenu()
navMainMenu()