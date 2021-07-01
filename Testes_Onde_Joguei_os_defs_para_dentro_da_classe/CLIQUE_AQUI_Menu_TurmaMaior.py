from CLASS_Turma import Turma
from Menu_Turma import Menu_turma, invalid_opt


TURMAS = []
TURMAS_SEM_CLASS = []


def f_adicionar_turma ():
    while True:
         nome_turma = str(input ("(Deixe Vazio para sair) Digite o nome do turma a ser adicionado:"   ))
         if nome_turma == "":
             break
         else:
             TURMAS.append (nome_turma)
             TURMAS_SEM_CLASS.append (nome_turma)
             TURMAS[-1] = Turma(nome_turma)

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
             options_turma = {"A":["Adicionar turma",f_adicionar_turma], "B":["Remover Turma",f_remover_turma], "C":["Listar Turmas", f_listar_turmas], "D":["Selecionar Turmas", f_selecionar_turmas]}
             print ("-=-=-=-=-=-=-=-")
             for option in options_turma:
                     print(option+") "+options_turma.get(option)[0])
             print ("-=-=-=-=-=-=-=-")

             choise = input("Faça sua escolha: ")
     
             if choise == "":
                 break
             else:
                 val = options_turma.get(choise)
                 if val is not None:
                     action = val[1]
                 else:
                     action = invalid_opt

                 action()




Menu_Maior()