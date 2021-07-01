from CLASS_Disciplina import Disciplina
from CLASS_Professor import Professor
from CLASS_Aluno import Aluno

ALUNOS=[]
ALUNOS_SEM_CLASS=[]
def f_adicionar_aluno ():
    while True:
         a1v = str(input ("(Deixe Vazio para sair) Digite o nome do aluno a ser adicionado:"   ))
         if a1v == "":
             break
         else:
             ALUNOS.append (a1v)
             ALUNOS_SEM_CLASS.append (a1v)
             ALUNOS[-1] = Aluno(a1v)

def f_remover_aluno ():
    while True:
        a2v = str(input ("(Deixe Vazio para sair) Digite o nome do aluno a ser removido:"   ))
        if a2v == "":
            break
        else:
            for i in range (0,len(ALUNOS_SEM_CLASS)):
                if a2v == str((ALUNOS_SEM_CLASS[i])):
                    ALUNOS.pop(i)
                    ALUNOS_SEM_CLASS.pop(i)
                    break

def f_adicionar_alunonota ():
    while True:
        a3v = str(input ("(Deixe Vazio para sair) Digite o nome do aluno que queira dar a nota:"   ))
        if a3v == "":
            break
        a1vN = str(input ("(Deixe Vazio para sair) Digite a nota deste aluno:"   ))
        if a1vN == "":
            break
        else:
            for i in range (0,len(ALUNOS_SEM_CLASS)):
                if a3v == str((ALUNOS_SEM_CLASS[i])):
                    ALUNOS[i].nota = a1vN
                    print("a")
                    break

f_adicionar_aluno()
f_remover_aluno()
f_adicionar_alunonota()



for i in range (0,len(ALUNOS_SEM_CLASS)):
    print ("A nota do Aluno "+ str(ALUNOS[i].name)+ " é: " +str(ALUNOS[i].nota))

