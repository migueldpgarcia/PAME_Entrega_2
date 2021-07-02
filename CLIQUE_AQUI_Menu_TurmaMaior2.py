from CLASS_Professor import Professor
from CLASS_Turma import Turma
from Menu_Turma2 import Menu_turma, invalid_opt


TURMAS = []
TURMAS_SEM_CLASS = []
APROFESSORES_TOTAL = Turma
MATERIA_TOTAL = []
AALUNOS_TOTAL = Turma


def f_adicionar_turma ():
    while True:
         nome_turma = str(input ("(Deixe Vazio para sair) Digite o nome do turma a ser adicionado:"   ))
         if nome_turma == "":
             break
         else:
             t = Turma(nome_turma)
             TURMAS.append (t)
             TURMAS_SEM_CLASS.append (nome_turma)

def f_remover_turma ():
    while True:
        nome_remover_turma = str(input ("(Deixe Vazio para sair) Digite o nome da turma a ser removido:"   ))
        if nome_remover_turma == "":
            break
        else:
            QuantidadesTurma = len (TURMAS_SEM_CLASS)
            for i in range (0,QuantidadesTurma):
                if nome_remover_turma == str((TURMAS[i].name)):
                    TURMAS.pop(i)
                    break
            for g in range (0,QuantidadesTurma):
                if nome_remover_turma == str(TURMAS_SEM_CLASS[g]):
                    TURMAS_SEM_CLASS.pop(g)
                    break

def f_listar_turmas ():
    print ("As Turmas são: " )
    for i in range (0,len(TURMAS_SEM_CLASS)):
             print (str(TURMAS_SEM_CLASS[i]))


def f_selecionar_turmas ():
    #input , entrar no Menu_Turma do input
    nome_da_turma = str(input("Digite o nome da turma a qual você quer selecionar: "))
    for i in range (0, len(TURMAS_SEM_CLASS)):
        if nome_da_turma == str(TURMAS[i].name):
            Menu_turma (TURMAS[i])







def Menu_Maior():
         while True:
             options_turma = {"A":["Adicionar turma",f_adicionar_turma], "B":["Remover turma",f_remover_turma], "C":["Listar turmas", f_listar_turmas], "D":["Selecionar turma", f_selecionar_turmas]}
             print ("-=-=-=-=-=-=-=-")
             for option in options_turma:
                     print(option+") "+options_turma.get(option)[0])
             print ("-=-=-=-=-=-=-=-")

             choise = input("(Enter para voltar) Faça sua escolha: ")
     
             if choise == "":
                 break
             else:
                 val = options_turma.get(choise)
                 if val is not None:
                     action = val[1]
                 else:
                     action = invalid_opt

                 action()

def f_nova_materia():
    g = str(input("(Enter para sair) Digite o nome da materia a ser cadastrada: "))
    MATERIA_TOTAL.append (" "+g)
    print ("Materia " +g+ " cadastrada.")

def f_lista_materia():
    StringMATERIATOTAL = ''.join([str(item) for item in (MATERIA_TOTAL)])
    print (StringMATERIATOTAL)

def f_cadastro_professor():

    g = str(input("(Enter para sair) Digite o nome do professor a ser cadastrado: "))
    APROFESSORES_TOTAL.PROFESSORES_TOTAL.append (" "+g)
    print ("Professor " +g+ " cadastrado.")

def f_lista_professores ():
    StringPROFESSORESTOTAL= ''.join([str(item) for item in (APROFESSORES_TOTAL.PROFESSORES_TOTAL)])
    print ("Os professores são: ")
    print (StringPROFESSORESTOTAL)

def f_cadastrar_novo_aluno():
    g = str(input("(Enter para sair) Digite o nome do aluno a ser cadastrado: "))
    AALUNOS_TOTAL.ALUNOSTOTAL.append (" "+g)
    print ("Aluno " +g+ " cadastrado.")


def f_lista_cadastro_alunos ():
    if len(AALUNOS_TOTAL.ALUNOSTOTAL) == 0:
        print ("Nao há alunos cadastrados")
    else:

         StringALUNOSTOTAL= ''.join([str(item) for item in (AALUNOS_TOTAL.ALUNOSTOTAL)])
         print ("Os alunos cadastrados são: ")
         print (StringALUNOSTOTAL)
    
   


def Menu_Principal ():
        while True:
            options_PRINCIPAL = {"A":["Cadastro de uma nova matéria",f_nova_materia], "B":["Cadastro de um novo professor",f_cadastro_professor], "C":["Cadastro de um novo aluno", f_cadastrar_novo_aluno], "D":["Mostrar todos as matérias cadastradas", f_lista_materia], "E": ["Mostrar todos os professores cadastrados", f_lista_professores], "F": ["Mostrar todos os alunos cadastrados", f_lista_cadastro_alunos ], "G": ["Abrir Menu de Turmas", Menu_Maior]}
            print ("-=-=-=-=-=-=-=-")
            for option in options_PRINCIPAL:
                print(option+") "+options_PRINCIPAL.get(option)[0])
            print ("-=-=-=-=-=-=-=-")
            choise = input("(Enter para fechar o programa) Faça sua escolha: ")
            if choise == "":
                break
            else:
                val = options_PRINCIPAL.get(choise)
                if val is not None:
                    action = val[1]
                else:
                    action = invalid_opt

                action()








Menu_Principal()