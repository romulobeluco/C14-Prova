from aluno import Aluno

if __name__ == "__main__":
    aluno = Aluno("João")
    aluno.adicionar_nota(8)
    aluno.adicionar_nota(6)
    print(f"Aluno: {aluno.nome}")
    print(f"Média: {aluno.calcular_media():.2f}")
    print(f"Situação: {aluno.situacao()}")
