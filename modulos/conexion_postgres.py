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
            with cx:
                with cx.cursor() as cursor:
                    cursor.execute(sql, parametros)
                    rows = cursor.fetchall()
                    for row in rows:
                        registros.append(adapter_function(row))
        finally:
            cx.close()
        return registros

    def select_one(self, sql, adapter_function, *parametros):
        registro = None
        cx = self.connect()
        try:
            with cx:
                with cx.cursor() as cursor:
                    cursor.execute(sql, parametros)
                    row = cursor.fetchone()
                    if row:
                        registro = adapter_function(row)

        finally:
            cx.close()
        return registro

    def update(self, sql, *parametros):
        cx = self.connect()
        try:
            with cx:
                with cx.cursor() as cursor:
                    cursor.execute(sql, parametros)

        finally:
            cx.close()

    @staticmethod
    def adapter_single_value(row):
        return row[0]

