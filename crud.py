import psycopg2


class AppBD:
    def __init__(self):
        self.connection = psycopg2.connect(user="postgres",
                                           password='101504',
                                           host="127.0.0.1",
                                           port="5432",
                                           database="postgres")
        print('Método Construtor')

    def abrirConexao(self):
        try:
            pass
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao se conectar ao Banco de Dados", error)

    # -----------------------------------------------------------------------------
    # Selecionar todos os Produtos
    # -----------------------------------------------------------------------------
    def selecionarDados(self):
        global cursor, registros
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Selecionando todos os produtos")
            sql_select_query = """select * from public."PRODUTO" """

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)


        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)

        finally:
            # closing database connection.
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
        return registros

    # -----------------------------------------------------------------------------
    # Inserir Produto
    # -----------------------------------------------------------------------------
    def inserirDados(self, codigo, nome, preco):
        global cursor
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """ INSERT INTO public."PRODUTO" 
          ("CODIGO", "NOME", "PRECO") VALUES (%s,%s,%s)"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com successo na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            # closing database connection.
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    # -----------------------------------------------------------------------------
    # Atualizar Produto
    # -----------------------------------------------------------------------------
    def atualizarDados(self, codigo, nome, preco):
        global cursor
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registro Antes da Atualização ")
            sql_select_query = """select * from public."PRODUTO" 
            where "CODIGO" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
            # Atualizar registro
            sql_update_query = """Update public."PRODUTO" set "NOME" = %s, 
            "PRECO" = %s where "CODIGO" = %s"""
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso! ")
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from public."PRODUTO" 
            where "CODIGO" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)
        finally:
            # closing database connection.
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    # -----------------------------------------------------------------------------
    # Excluir Produto
    # -----------------------------------------------------------------------------
    def excluirDados(self, codigo):
        global cursor
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            # Atualizar registro
            sql_delete_query = """Delete from public."PRODUTO" 
            where "CODIGO" = %s"""
            cursor.execute(sql_delete_query, (codigo,))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso! ")
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)
        finally:
            # closing database connection.
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

# -----------------------------------------------------------------------------
