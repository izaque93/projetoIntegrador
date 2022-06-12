from django.contrib import admin
import psycopg2 

# Register your models here.

class Connection:

    def conn(self):

        conn = psycopg2.connect(
                host = "castor.db.elephantsql.com",
                user = "dyinyvgt",
                password = "VDO80ZzjvRwwiJJ0AfAcIpJDzHQOC9kn",
                database = "dyinyvgt")
        return conn