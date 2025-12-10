import os
import psycopg2

def insert_row(data_referencia, value):
    conn = None
    cursor = None
    
    try:
        conn = psycopg2.connect(
            host = os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"])
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO valores_scraping_lme (data_referencia, valor)
            VALUES (%s, %s)
            ON CONFLICT (data_referencia) DO UPDATE
            SET valor = EXCLUDED.valor,
                data_coleta = NOW();
        """, (data_referencia, value))

        conn.commit()

    except psycopg2.Error as e:
        print("Erro ao inserir no banco:", e)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
