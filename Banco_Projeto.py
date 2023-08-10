import mysql.connector

class DataBase():
    def __init__(self, banco = "Projeto_Cadastro") -> None:
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database='Projeto_Cadastro',user='root',password='Bnas123!@#')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            # print("Conectado ao Servidor de Banco de Dados: ", db_info)
        else:
            print("Erro")  

    
    def register_company(self,empresaCadastro):
        self.connect()
        try:
            args = (empresaCadastro[0],empresaCadastro[1],empresaCadastro[2],empresaCadastro[3],empresaCadastro[4],empresaCadastro[5],empresaCadastro[6],empresaCadastro[7],empresaCadastro[8],empresaCadastro[9],empresaCadastro[10])
            self.cursor.execute('INSERT INTO empresa (cnpj,nome,logradouro,numero,complemento,bairro,municipio,uf,cep,telefone,email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', args)
            self.conn.commit()
            return("Cadastro feito, tudo OK")
        except Exception as err:
            return "ERRO",str(err)
        finally:
            self.conn.close()
            return ("Conexão encerrada com Sucesso!!!")
        
    def alterar_empresa(self, campo):
        self.connect()
        try:
            self.cursor.execute(f""" UPDATE empresa set

            CNPJ = '{campo[1]}',
            NOME = '{campo[2]}',
            LOGRADOURO = '{campo[3]}',
            NUMERO = '{campo[4]}',
            COMPLEMENTO = '{campo[5]}',
            BAIRRO = '{campo[6]}',
            MUNICIPIO = '{campo[7]}',
            UF = '{campo[8]}',
            CEP = '{campo[9]}',
            TELEFONE = '{campo[10]}',
            EMAIL = '{campo[11]}'

            WHERE id_empresa = '{campo[0]}'""")
            self.conn.commit()
            return("Alteração feita com Sucesso!!!")

        except Exception as err:
            return "ERRO",str(err)
        finally:
            self.conn.close()
            return ("Conexão encerrada com Sucesso!!!")
        
    def consulta_empresas(self):
        self.connect()
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM empresa ORDER BY id_empresa")
            empresa = cursor.fetchall()
            return empresa
        

        except Exception as err:
            return str(err)
        finally:
            self.conn.close()

    def buscar_empresas(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT * FROM empresa WHERE nome LIKE '%{texto}%' or cnpj LIKE '%{texto}%';
            """)
            result = self.cursor.fetchall()
            for linha in result:
               print(linha)
            
            return result
        except Exception as err:
            print(err)

    def delete_empresa(self,id):
        self.connect()
        try:
            self.cursor.execute(
                f"""DELETE FROM empresa WHERE id_empresa = '{id}' """
            )
            self.conn.commit()
            return "OK","Cadastro excluído com sucesso!"

        except Exception as err:
            print(err)

 
        
if __name__ == "__main__":
    db = DataBase()
    db.connect()
    db.close_connection()
