import psycopg2

def get_data():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='valores_scraping',
            user='postgres',
            password='postgres'
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data_referencia;")
        data = cursor.fetchall()

        return data

    except psycopg2.Error as e:
        print("Erro ao consultar o banco:", e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


result = get_data()

if result:

    print(result)
