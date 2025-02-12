"""

app que premite add alunos
    calcular a media de cada aluno
    listar alunos
    Mostrar melhor e pior nota
    registar notas de alunos
    deve ser possivel saber que professor deu a nota


escola
    lista Alunos
    Lista de professores

    listar_alunos()
    melhor_nota(UFCD)
    pior_nota(UFCD)

    registar notas de alunos(aluno, professor, nota)


nota
    nota
    UFCD
    professor

registar Alunos
    nome
    email
    turma
    lista de notas
    calc_media()

registar professores
    nome
    email

"""


from Escola import Escola



es = Escola('Escola Secundaria de Vila Nova de Gaia', [], [])


print(es.__dir__())
