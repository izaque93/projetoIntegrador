from django.db import models
from tarefas.admin import Connection

# Create your models here.
class CadastroDoacoes:
    def inserir_cadastro_doacoes(self, roupas, num_roupas, objetos, num_objetos, calcados, num_calcados, brinquedos, num_brinquedos):
        connection = Connection()

        try:
            cur = connection.conn()
            cur_aux = cur.cursor()

            SQL = f"""INSERT INTO CADASTRO_PECAS (NOME_ROUPAS, NUM_ROUPAS, NOME_OBJETOS, NUM_OBJETOS, NOME_CALCADOS, NUM_CALCADOS, NOME_BRINQUEDOS, NUM_BRINQUEDOS)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

            dados = (roupas, num_roupas, objetos, num_objetos, calcados, num_calcados, brinquedos, num_brinquedos)

            cur_aux.execute(SQL, dados)

            cur.commit()
            cur_aux.close()

            #print("Criou token", access_token, usuario_out)
            return "Inserido com sucesso"
        except Exception as e:
            print(e)