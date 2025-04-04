# Sistema de Gerenciamento de Transporte Escolar

## 📄 Descrição do Projeto
Este é um sistema desenvolvido para auxiliar a Secretaria de Educação na gestão dos alunos transportados pela rede municipal de ensino. Com ele, é possível:

- Cadastrar alunos com todos os dados necessários
- Gerar relatórios em PDF
- Emitir carteirinhas individuais com foto
- Pesquisar, editar e excluir alunos cadastrados
- Armazenar dados em banco de dados local (SQLite)

O sistema possui uma interface gráfica feita com **Tkinter**, e gera documentos PDF utilizando a biblioteca **FPDF**.

---

## 💡 Tecnologias Utilizadas
- Python 3
- Tkinter (interface gráfica)
- SQLite3 (banco de dados leve e local)
- FPDF (geração de PDF)

---

## 🚀 Funcionalidades
- 📋 **Cadastro completo de aluno**: nome, endereço, rota, motorista, pais, telefone, observações e foto
- 📄 **Geração de relatório** geral em PDF
- 🪪 **Geração de carteirinhas** individuais com foto em PDF
- 🔍 **Pesquisa com filtros** por nome e rota
- ✏️ **Edição** de dados do aluno diretamente pela interface
- 🗑️ **Exclusão** de aluno com confirmação

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

3. **Instale as dependências** (executar no terminal - fora do Python interativo):
```bash
pip install fpdf
```

4. **Execute o sistema**:
✅ Opção 1 — Usar o botão ▶️ "Run Python File" no VS Code (canto superior direito)

✅ Opção 2 — Rodar pelo terminal manualmente:
```bash
python interface_grafica.py
```

---

## 📂 Banco de Dados
O banco de dados é criado automaticamente com o nome `transporte_escolar.db`.

### 🛡️ Atualização automática da estrutura

O sistema contém um trecho que garante a existência da tabela e da coluna `foto`, mesmo que o banco já exista:
```python
cursor.execute("PRAGMA table_info(alunos)")
colunas = [col[1] for col in cursor.fetchall()]
if "foto" not in colunas:
    cursor.execute("ALTER TABLE alunos ADD COLUMN foto TEXT")
```
Isso garante compatibilidade entre os membros do grupo e previne erros.

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
- Geração de executável (.exe) para uso em máquinas sem Python

---

🚀 Projeto em constante evolução, Grupo!!! Que a Força esteja com vocês! 💪
