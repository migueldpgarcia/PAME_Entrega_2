from CLASS_Disciplina import Disciplina
from CLASS_Professor import Professor
from CLASS_Aluno import Aluno

ALUNOS=[]
ALUNOSNOTA=[]
def f_adicionar_aluno ():
    while True:
         a1v = str(input ("(Deixe Vazio para sair) Digite o nome do aluno a ser adicionado:"   ))
         if a1v == "":
             break
         else:
             a1 = Aluno(a1v)
             ALUNOS.append (a1.name)

def f_remover_aluno ():
    while True:
        a2v = str(input ("(Deixe Vazio para sair) Digite o nome do aluno a ser removido:"   ))
        if a2v == "":
            break
        else:
            for i in range (0,len(ALUNOS)):
                if a2v == str((ALUNOS[i])):
                    ALUNOS.pop(i)
                    break

def f_adicionar_alunonota ()
        



f_adicionar_aluno()
f_remover_aluno()
print (ALUNOS)




