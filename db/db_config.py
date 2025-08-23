import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="xoso_db",
        user="postgres",
        password="12345678"  # <- đổi thành mật khẩu bạn đặt khi cài PostgreSQL
    )