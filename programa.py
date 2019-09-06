from banco import Banco

# Programa escrito por Rafael Santos em 05/09/2019

# Instanciando o objeto Banco
bd = Banco()

# Iniciando conexão com banco de dados
bd.conectar()

# Inserindo um registro na tabela branch1
params = [ ('B1', '1.50') ]
bd.inserir("INSERT INTO branch1 (codigo_aluno, altura) VALUES (?, ?)", params)

# Inserindo um registro na tabela branch2
params = [ ('B2', '2019-09-05', '7') ] # Lembrando que o tipo DATA no PostgreSQL é representado assim: yyyy-mm-dd
bd.inserir("INSERT INTO branch2 (codigo_materia	, data, nota) VALUES (?, ?, ?)", params)

# Inserindo um registro na tabela memvar relacionado às tabelas branch1 e branch2
params = [ ('M1', 'descrição', '100', '200', 'true', '80', 'B1', 'B2') ] 
bd.inserir("INSERT INTO memvar (codigo, descricao, quantidade1, quantidade2, sim, percentual,  codigo_aluno, codigo_materia) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", params)

# Atualizando a coluna quantidade1 na tabela memvar no registro com código M1
#bd.atualizar("UPDATE memvar SET quantidade1='40' WHERE codigo='M1'")

# Deletando o registro do código M1 na tabela memvar
#bd.atualizar("DELETE FROM memvar WHERE codigo='M1'")

# Consultando a tabela memvar relacionada a tabela branch1 e branch2
#bd.consultar("SELECT * FROM memvar AS m JOIN branch1 AS b1 ON b1.codigo_aluno=m.codigo_aluno JOIN branch2 AS b2 ON b2.codigo_materia=m.codigo_materia")
# Lembro que a consulta com JOIN em tabelas com muitos registros terá uma performance inferior

# Encerrando conexão com o banco de dados
bd.desconectar()