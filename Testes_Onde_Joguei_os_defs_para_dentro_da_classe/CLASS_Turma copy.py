from CLASS_Professor import Professor
from CLASS_Aluno import Aluno

class Turma:
    ALUNOS=[]
    ALUNOS_SEM_CLASS=[]
    ALUNOS_SEM_CLASS_ORDENADOS=[]
    PROFESSOR= Professor("Sem Professor")
    def __init__(self, name):
        self.name = name
    
    def f_adicionar_aluno ():
        while True:
            nome_aluno = str(input ("(Deixe Vazio para sair) Digite o nome do aluno a ser adicionado:"   ))
            if nome_aluno == "":
                break
            else:
                a = Aluno(nome_aluno)
                ALUNOS.append (nome_aluno)
                ALUNOS_SEM_CLASS.append (nome_aluno)
             

    def f_remover_aluno (t):
        while True:
            nome_remover_aluno = str(input ("(Deixe Vazio para sair) Digite o nome do aluno a ser removido:"   ))
            if nome_remover_aluno == "":
                break
            else:
                QuantidadesAlunos = len (ALUNOS_SEM_CLASS)
                for i in range (0,QuantidadesAlunos):
                    if nome_remover_aluno == str((ALUNOS[i].name)):
                        ALUNOS.pop(i)
                        break
                for g in range (0,QuantidadesAlunos):
                    if nome_remover_aluno == str(ALUNOS_SEM_CLASS[g]):
                        ALUNOS_SEM_CLASS.pop(g)
                        break

    def f_adicionar_alunonota (t):
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

    def f_adicionar_professor (t):
        while True:
            nome_professor = str(input ("(Deixe Vazio para sair) Digite o nome do professor:  "))
            if nome_professor == "":
                break
            else:
                PROFESSOR.name = nome_professor

    def f_alunos_ordem_alfabetica (t):
        ALUNOS_SEM_CLASS_ORDENADOS = []
        ALUNOS_SEM_CLASS_ORDENADOS = ALUNOS_SEM_CLASS
        ALUNOS_SEM_CLASS_ORDENADOS.sort()
        print ("Os alunos são: " )
        for i in range (0,len(ALUNOS_SEM_CLASS_ORDENADOS)):
                print (str(ALUNOS_SEM_CLASS_ORDENADOS[i]))
        print ("O Professor é: ")
        print (str(PROFESSOR.name))

    def f_mostrar_alunonota (t):
        for i in range (0,len(ALUNOS_SEM_CLASS)):
                print (str(ALUNOS[i].name) + " tem nota "+ str (ALUNOS[i].nota) )
