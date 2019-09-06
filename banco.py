import pyodbc

# Classe implementada por Rafael Santos em 05/09/2019
# Baseado na documentação do pyodbc em: https://github.com/mkleehammer/pyodbc/wiki/Getting-started

class Banco:

    # Método de conexão com banco de dados usando o driver OBDC
    def conectar(self):
        global cnxn
        global cursor
        # Parâmetros para fazer a conexão
        parametros = ("DRIVER={PostgreSQL ODBC Driver(ANSI)};"
        "DATABASE=simulador;"
        "UID=postgres;"
        "PWD=abc.1234;"
        "SERVER=localhost;"
        "PORT=5432;")
        # Conectando ao banco de dados com os parâmetros acima
        cnxn = pyodbc.connect(parametros)

        # Criando um cursor para a conexão com o banco de dados
        cursor = cnxn.cursor()

    # Método para fazer um SELECT
    def consultar(self, sql):
        cursor.execute(sql)
        row = cursor.fetchone()
        print(row) 
        cursor.close()

    # Método para fazer um INSERT INTO
    def inserir(self, sql, params):
        cursor.executemany(sql, params)
        cnxn.commit()

    # Método para fazer um UPDATE
    def atualizar(self, sql):
        cursor.execute(sql)
        cnxn.commit()

    # Método para fazer um DELETE
    def deletar(self, sql):
        cursor.execute(sql)
        cnxn.commit()

    # Método para terminar a conexão com o banco de dados
    def desconectar(self):
        cnxn.close()

        