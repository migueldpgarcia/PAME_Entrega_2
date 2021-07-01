from CLASS_Disciplina import Disciplina
from CLASS_Professor import Professor
from CLASS_Aluno import Aluno

ALUNOS=[]
ALUNOS_SEM_CLASS=[]
ALUNOS_SEM_CLASS_ORDENADOS=[]
PROFESSOR= Professor("Sem Professor")
def f_adicionar_aluno ():
    while True:
         nome_aluno = str(input ("(Deixe Vazio para sair) Digite o nome do aluno a ser adicionado:"   ))
         if nome_aluno == "":
             break
         else:
             ALUNOS.append (nome_aluno)
             ALUNOS_SEM_CLASS.append (nome_aluno)
             ALUNOS[-1] = Aluno(nome_aluno)

def f_remover_aluno ():
    while True:
        nome_remover_aluno = str(input ("(Deixe Vazio para sair) Digite o nome do aluno a ser removido:"   ))
        if nome_remover_aluno == "":
            break
        else:
            QuantidadesAlunos = len (ALUNOS_SEM_CLASS)
            for i in range (0,QuantidadesAlunos):
                if nome_remover_aluno == str((ALUNOS_SEM_CLASS[i])):
                    ALUNOS.pop(i)
            for g in range (0,QuantidadesAlunos):
                if nome_remover_aluno == str(ALUNOS_SEM_CLASS[g]):
                    ALUNOS_SEM_CLASS.pop(g)
                    break

def f_adicionar_alunonota ():
    while True:
        nome_aluno_pela_nota = str(input ("(Deixe Vazio para sair) Digite o nome do aluno que queira dar a nota:"   ))
        if nome_aluno_pela_nota == "":
            break
        nota_do_aluno = str(input ("(Deixe Vazio para sair) Digite a nota deste aluno:"   ))
        if nota_do_aluno == "":
            break
        else:
            for i in range (0,len(ALUNOS_SEM_CLASS)):
                if nome_aluno_pela_nota == str((ALUNOS[i].name)):
                    ALUNOS[i].nota = nota_do_aluno
                    break

def f_adicionar_professor ():
    while True:
        nome_professor = str(input ("(Deixe Vazio para sair) Digite o nome do professor:  "))
        if nome_professor == "":
            break
        else:
            PROFESSOR.name = nome_professor

def f_alunos_ordem_alfabetica ():
    ALUNOS_SEM_CLASS_ORDENADOS = []
    ALUNOS_SEM_CLASS_ORDENADOS = ALUNOS_SEM_CLASS
    ALUNOS_SEM_CLASS_ORDENADOS.sort()
    print ("Os alunos são: " )
    for i in range (0,len(ALUNOS_SEM_CLASS_ORDENADOS)):
             print (str(ALUNOS_SEM_CLASS_ORDENADOS[i]))
    print ("O Professor é: ")
    print (str(PROFESSOR.name))

def f_mostrar_alunonota ():
    for i in range (0,len(ALUNOS_SEM_CLASS)):
             print (str(ALUNOS[i].name) + " tem nota "+ str (ALUNOS[i].nota) )




def invalid_opt():
  print("Invalid choice")

options_turma = {"A":["Adicionar Aluno",f_adicionar_aluno], "B":["Remover Aluno",f_remover_aluno], "C":["Adiocionar Professor",f_adicionar_professor], "D": ["Listar alunos", f_alunos_ordem_alfabetica], "E": ["Dar nota aos alunos da turma", f_adicionar_alunonota], "F": ["Mostrar as notas dos alunos", f_mostrar_alunonota]}

while True:
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




