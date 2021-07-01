from CLASS_Professor import Professor

class Turma:
    ALUNOS=["feijao"]
    ALUNOS_SEM_CLASS=[]
    ALUNOS_SEM_CLASS_ORDENADOS=[]
    PROFESSOR= Professor("Sem Professor")
    def __init__(self, name):
        self.name = name