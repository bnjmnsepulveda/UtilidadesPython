import psycopg2
from datasource.model import Dialogo


class Dialogo:

    def __init__(self, pregunta=None, respuesta=None):
        self.pregunta = pregunta
        self.respuesta = respuesta

    def __str__(self):
        return '[' + self.pregunta + ' - ' + self.respuesta + ']'

def adapter(row):
    dialogo = Dialogo()
    dialogo.pregunta = row[1]
    dialogo.respuesta = row[2]
    return dialogo


class ConexionPostgres:

    def __init__(self, host, basedatos, usuario, clave):
        self.host = host
        self.basedatos = basedatos
        self.usuario = usuario
        self.clave = clave

    def connect(self):
        dsn = "dbname={} user={} password={} host={}"
        return psycopg2.connect(dsn.format(self.basedatos, self.usuario, self.clave, self.host))

    def select_all(self, sql, adapter_function, *parametros):
        registros = []
        with self.connect() as cx:
            with cx.cursor() as cursor:
                cursor.execute(sql, parametros)
                rows = cursor.fetchall()
                for row in rows:
                    registros.append(adapter_function(row))

        return registros

    def select_one(self, sql, adapter_function, *parametros):
        registro = {}
        with self.connect() as cx:
            with cx.cursor() as cursor:
                cursor.execute(sql, parametros)
                rows = cursor.fetchone()
                for row in rows:
                    registro = adapter_function(row)

        return registro

    def update(self, sql, *parametros):
        with self.connect() as cx:
            with cx.cursor() as cursor:
                cursor.execute(sql, parametros)


conexion = ConexionPostgres(host='localhost', basedatos='cckall_chatbot', usuario='postgres', clave='adp2019')
regs = conexion.select_all('SELECT * FROM dialogo', adapter)
for r in regs[0:10]:
    print(r.pregunta)
