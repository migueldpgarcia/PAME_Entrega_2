from CLASS_Disciplina import Disciplina
from CLASS_Professor import Professor
from CLASS_Aluno import Aluno

ALUNOS=[]
ALUNOS_SEM_CLASS=[]
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
            for i in range (0,len(ALUNOS_SEM_CLASS)):
                if nome_remover_aluno == str((ALUNOS_SEM_CLASS[i])):
                    ALUNOS.pop(i)
                    ALUNOS_SEM_CLASS.pop(i)
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
                if nome_aluno_pela_nota == str((ALUNOS_SEM_CLASS[i])):
                    ALUNOS[i].nota = nota_do_aluno
                    print("a")
                    break

def f_adicionar_professor ():
    while True:
        nome_professor = str(input ("(Deixe Vazio para sair) Digite o nome do professor:  "))
        if nome_professor == "":
            break
        else:
            PROFESSOR.name = nome_professor

def f_alunos_ordem_alfabetica ():
    ALUNOS_SEM_CLASS.sort ()
    for i in range (0,len(ALUNOS_SEM_CLASS)):
             print (str(ALUNOS_SEM_CLASS[i]))


    



f_adicionar_aluno()
f_remover_aluno()
f_adicionar_alunonota()
f_adicionar_professor()
f_alunos_ordem_alfabetica ()




print (str(PROFESSOR.name))

