import pytest
from aluno import Aluno

# ---------- Testes de criação ----------
def test_criacao_aluno_nome():
    aluno = Aluno("Maria")
    assert aluno.nome == "Maria"
    assert aluno.notas == []

def test_criacao_aluno_sem_notas():
    aluno = Aluno("Carlos")
    assert aluno.calcular_media() == 0
    assert aluno.situacao() == "Reprovado"

# ---------- Testes de adicionar notas ----------
def test_adicionar_nota_valida():
    aluno = Aluno("João")
    aluno.adicionar_nota(8)
    assert aluno.notas == [8]

def test_adicionar_varias_notas():
    aluno = Aluno("Ana")
    aluno.adicionar_nota(5)
    aluno.adicionar_nota(9)
    assert aluno.notas == [5, 9]

def test_adicionar_nota_invalida_negativa():
    aluno = Aluno("Pedro")
    with pytest.raises(ValueError):
        aluno.adicionar_nota(-1)

def test_adicionar_nota_invalida_maior_que_10():
    aluno = Aluno("Pedro")
    with pytest.raises(ValueError):
        aluno.adicionar_nota(11)

# ---------- Testes de média ----------
def test_media_sem_notas():
    aluno = Aluno("Lucas")
    assert aluno.calcular_media() == 0

def test_media_uma_nota():
    aluno = Aluno("Lucas")
    aluno.adicionar_nota(7)
    assert aluno.calcular_media() == 7

def test_media_varias_notas():
    aluno = Aluno("Marina")
    aluno.adicionar_nota(6)
    aluno.adicionar_nota(8)
    assert aluno.calcular_media() == 7

def test_media_com_decimais():
    aluno = Aluno("Rafaela")
    aluno.adicionar_nota(5)
    aluno.adicionar_nota(6)
    aluno.adicionar_nota(7)
    assert pytest.approx(aluno.calcular_media(), 0.01) == 6.0

# ---------- Testes de situação ----------
def test_situacao_aprovado():
    aluno = Aluno("Julia")
    aluno.adicionar_nota(8)
    aluno.adicionar_nota(9)
    assert aluno.situacao() == "Aprovado"

def test_situacao_reprovado():
    aluno = Aluno("Tiago")
    aluno.adicionar_nota(3)
    aluno.adicionar_nota(4)
    assert aluno.situacao() == "Reprovado"

def test_situacao_recuperacao():
    aluno = Aluno("Carla")
    aluno.adicionar_nota(5)
    aluno.adicionar_nota(6)
    assert aluno.situacao() == "Recuperação"

def test_situacao_limite_aprovado():
    aluno = Aluno("Leo")
    aluno.adicionar_nota(7)
    aluno.adicionar_nota(7)
    assert aluno.situacao() == "Aprovado"

def test_situacao_limite_recuperacao():
    aluno = Aluno("Fernanda")
    aluno.adicionar_nota(5)
    aluno.adicionar_nota(5)
    assert aluno.situacao() == "Recuperação"

def test_situacao_limite_reprovado():
    aluno = Aluno("Bruno")
    aluno.adicionar_nota(4.9)
    aluno.adicionar_nota(5.0)
    assert aluno.situacao() == "Reprovado"

# ---------- Testes extras ----------
def test_lista_notas_vazia():
    aluno = Aluno("Silvia")
    assert aluno.notas == []

def test_media_nao_modifica_notas():
    aluno = Aluno("Mario")
    aluno.adicionar_nota(10)
    aluno.adicionar_nota(5)
    _ = aluno.calcular_media()
    assert aluno.notas == [10, 5]
