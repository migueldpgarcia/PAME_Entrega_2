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
             ALUNOS.append (a1v)
             ALUNOS[-1] = Aluno(a1v)

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

def f_adicionar_alunonota ():
    while True:
        a3v = str(input ("(Deixe Vazio para sair) Digite o nome do aluno que queira dar a nota:"   ))
        a1vN = str(input ("(Deixe Vazio para sair) Digite a nota deste aluno:"   ))
        if a1vN == "":
            break
        else:
            for i in range (0, len(ALUNOS)):
                if a3v == str(ALUNOS[i]):
                    ALUNOS[i].nota = a1vN
                    print (ALUNOS[i].nota)
                    #NaoEstouConseguindoGravarANotaDoAluno
                    print (a1vN)
                    break
                else: return

f_adicionar_aluno()
f_remover_aluno()
f_adicionar_alunonota()

print (str(ALUNOS[0].name))
print (str(ALUNOS[0].nota))

