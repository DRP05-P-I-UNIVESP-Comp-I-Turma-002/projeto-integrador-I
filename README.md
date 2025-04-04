# Sistema de Gerenciamento de Transporte Escolar

## 📄 Descrição do Projeto
Este é um sistema desenvolvido para auxiliar a Secretaria de Educação na gestão dos alunos transportados pela rede municipal de ensino. Com ele, é possível:

- Cadastrar alunos
- Gerar relatórios em PDF
- Emitir carteirinhas individuais de transporte
- Armazenar dados em banco de dados local (SQLite)
- Anexar e registrar a foto do aluno

O sistema possui uma interface gráfica simples feita com **Tkinter**, e gera documentos PDF utilizando a biblioteca **FPDF**.

---

## 💡 Tecnologias Utilizadas
- Python 3
- Tkinter (interface gráfica)
- SQLite3 (banco de dados leve e local)
- FPDF (geração de PDF)

---

## 🚀 Funcionalidades
- Cadastro completo de aluno (nome, endereço, rota, motorista, pais, telefone, observações e foto)
- Geração de relatório geral em PDF
- Geração de carteirinhas individuais com foto em PDF
- Interface com três botões: Cadastrar, Relatório e Carteirinhas

---

## 📝 Instruções de Instalação

1. **Clone o repositório**:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. **(Opcional) Crie um ambiente virtual**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

3. **Instale as dependências**:(Deve ser executado no Prompt de Comando (CMD) ou no terminal integrado do VS Code, fora do Python)
```bash
pip install fpdf
```
Obs:❌ Não faça dentro do Python interativo (não deve aparecer >>>):
>>> pip install fpdf  # ERRADO

4. **Execute o sistema**:
✅ Opção 1 — Usar o botão de execução do VS Code
▶️ O famoso botão "Run Python File"
Ele aparece no canto superior direito do editor quando o arquivo .py está aberto.
✅ Opção 2 — Usar o terminal manualmente
Se quiser, você também pode abrir o terminal (com Ctrl + ' ou Terminal > Novo Terminal) e digitar:
```bash
python interface_grafica.py
```

---

## 📂 Banco de Dados
O banco de dados é criado automaticamente com o nome `transporte_escolar.db`.

### 🛡️ Verificação e atualização automática da estrutura

O sistema contém um trecho que garante a existência da tabela e da coluna `foto`, mesmo que o banco já tenha sido criado antes:

```python
cursor.execute("PRAGMA table_info(alunos)")
colunas = [col[1] for col in cursor.fetchall()]
if "foto" not in colunas:
    cursor.execute("ALTER TABLE alunos ADD COLUMN foto TEXT")
```

Isso garante compatibilidade entre os membros do grupo e previne erros de execução.

---

## ✉️ Contato e Autoria
Desenvolvido por alunos da **UNIVESP** para o Projeto Integrador.

> Orientador: Prof. Nome do Orientador  
> Integrantes: Nome 1, Nome 2, Nome 3...

---

## ✨ Possíveis Evoluções Futuras
- Integração com mapas para traçar rotas
- Exportação para Excel/CSV
- Controle de motoristas e veículos
- Versão web com Flask ou Django

---

🚀 Projeto em constante evolução Grupo!!! que a Força Esteja com vocês!!!

