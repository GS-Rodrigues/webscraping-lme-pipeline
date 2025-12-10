import psycopg2

def insert_row(data_referencia, value):
    conn = None
    cursor = None
    
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='valores_scraping',
            user='postgres',
            password='postgres'
        )
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO valores_scraping (data_referencia, valor)
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
