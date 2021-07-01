

def invalid_opt():
  print("Invalid choice")

def Menu_turma(t):


     options = {"A":["Adicionar Aluno", t.f_adicionar_aluno], "B":["Remover Aluno",t.f_remover_aluno], "C":["Adiocionar Professor",t.f_adicionar_professor], "D": ["Listar alunos", t.f_alunos_ordem_alfabetica], "E": ["Dar nota aos alunos da turma", t.f_adicionar_alunonota], "F": ["Mostrar as notas dos alunos", t.f_mostrar_alunonota]}

     while True:
         print ("-=-=-=-=-=-=-=-")
         for option in options:
              print(option+") "+options.get(option)[0])
         print ("-=-=-=-=-=-=-=-")

         choise = input("(Enter para voltar)Faça sua escolha: ")
     
         if choise == "":
 
              break
         else:
              val = options.get(choise)
              if val is not None:
                  action = val[1]
              else:
                 action = invalid_opt

              action()



