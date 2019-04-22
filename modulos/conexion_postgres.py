import psycopg2


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
        cx = self.connect()
        try:
            cursor = cx.cursor()
            try:
                cursor.execute(sql, parametros)
                rows = cursor.fetchall()
                for row in rows:
                    registros.append(adapter_function(row))
            finally:
                cursor.close()
        finally:
            cx.close()
        return registros

    def select_one(self, sql, adapter_function, *parametros):
        registro = None
        cx = self.connect()
        try:
            cursor = cx.cursor()
            try:
                cursor.execute(sql, parametros)
                row = cursor.fetchone()
                if row:
                    registro = adapter_function(row)
            finally:
                cursor.close()
        finally:
            cx.close()
        return registro

    def update(self, sql, *parametros):
        cx = self.connect()
        try:
            cursor = cx.cursor()
            try:
                cursor.execute(sql, parametros)
            finally:
                cursor.close()
        finally:
            cx.close()


