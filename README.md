
# 🎓 Projeto C14 - Prova de Python

[![CI/CD Pipeline](https://github.com/romulobeluco/C14-Prova/actions/workflows/ci.yml/badge.svg)](https://github.com/romulobeluco/C14-Prova/actions)

## 📖 Descrição
Este projeto é uma prova de Python que inclui:
- 🧑‍🏫 Implementação de uma classe `Aluno` para controle de notas.
- ✅ Testes unitários utilizando `pytest`.
- ⚙️ Pipeline de CI/CD configurado com GitHub Actions, incluindo:
  - 🔍 Execução de testes automatizados
  - 📦 Empacotamento do projeto
  - 📧 Notificação por e-mail

## 👥 Integrantes
- **Rômulo Coutinho Beluco**
- **Matheus Augusto**

---

## 📂 Estrutura do Projeto

```

C14-Prova/
├── aluno.py              # 📘 Implementação da classe Aluno
├── requirements.txt      # 📦 Dependências do projeto
├── setup.py              # ⚙️ Configuração para build/empacotamento
├── tests/                # 🧪 Pasta com os testes unitários
│   └── test_aluno.py     # Arquivo de testes da classe Aluno
└── .github/
└── workflows/        # 🔄 Configuração do GitHub Actions (CI/CD)
└── ci.yml

````

---

## 🖥️ Como rodar o projeto localmente

1. **📂 Clonar o repositório:**
```bash
git clone https://github.com/romulobeluco/C14-Prova.git
cd C14-Prova
````

2. **📦 Instalar dependências:**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. **🧪 Rodar os testes com pytest:**

```bash
pytest -v
```

4. **📦 Empacotar o projeto (opcional):**

```bash
python -m build
```

5. **👨‍💻 Executar a classe Aluno manualmente (exemplo):**

```bash
python
>>> from aluno import Aluno
>>> aluno = Aluno("Maria")
>>> aluno.adicionar_nota(8)
>>> aluno.calcular_media()
>>> aluno.situacao()
```

---

## 🚀 CI/CD (GitHub Actions)

O projeto conta com um **pipeline automatizado** configurado no GitHub Actions:

* 🔹 **Job de Testes (`tests`)**
  Executa todos os testes unitários com `pytest` e salva um relatório.

* 🔹 **Job de Build (`build`)**
  Cria o pacote Python do projeto (`.whl` e `.tar.gz`), garantindo que o código pode ser distribuído.

* 🔹 **Job de Notificação (`notify`)**
  Após o sucesso dos jobs anteriores, envia um **e-mail de notificação** para os desenvolvedores informando o status da execução.

Todos os jobs são executados automaticamente **a cada push ou pull request na branch `main`**, garantindo qualidade e automação no ciclo de desenvolvimento. ✅
