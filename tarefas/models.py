from sqlite3 import connect
from django.db import models
from tarefas.admin import Connection
from requests import post

MAILGUN_DOMAIN = "sandboxe80cb48bb99b4c79ae4b0702219685dd.mailgun.org"
MAILGUN_API_KEY = "71746b5b3464bee0171695390e5fe564-50f43e91-8c9aad6b"
FROM_TITLE = "No-reply"
FROM_EMAIL = "no-reply@projetointegrador.com"

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

    def enviar_email(self, message, name, email, subject):
        # return requests.post("https://api.mailgun.net/v3/sandboxe80cb48bb99b4c79ae4b0702219685dd.mailgun.org",
		# auth=("api", "71746b5b3464bee0171695390e5fe564-50f43e91-8c9aad6b"),
		# data={"from": "Excited User <mailgun@gmail.com>",
		# 	"to": "willartes@gmail.com",
		# 	"subject": "Hello",
		# 	"text": "Testing some Mailgun awesomness!"})
        return post('https://api.mailgun.net/v3/{}/messages'.format(MAILGUN_DOMAIN),
                    auth=('api', MAILGUN_API_KEY),
                    data={'from': '{} <{}> '.format(FROM_TITLE, FROM_EMAIL), 'cc': 'juliocartier@gmail.com', 'bcc': 'jecolle@gmail.com', 'to': 'willartes@gmail.com',
                          'subject': f'{subject} Email Enviado: {email} Nome: {name}',
                          'text': f'{message}',
                          'html': f'<html> <p> \
                              {message}</p></html>'
                              }
                    )

    def cadastroComCep(self, cep, rua, numero, complemento, bairro, cidade, uf, email, password):
        connection = Connection()
        try:
            cur = connection.conn()
            cur_aux = cur.cursor()
            SQL = f"""INSERT INTO CADASTRO(CEP, RUA, NUMERO, COMPLEMENTO, BAIRRO, CIDADE, UF, EMAIL, PASSWORD)
                                            VALUES(%S, %S, %S, %S, %S, %S, %S, %S, %S);"""
            dados = (cep, rua, numero, complemento, bairro, cidade, uf, email, password)
            cur_aux.execute(SQL, dados)

            cur.commit()
            cur_aux.close()
            return "Inseridos com sucesso"
        except Exception as e:
            print(e)