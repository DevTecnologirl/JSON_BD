import json
import psycopg2

# Configurações do banco de dados PostgreSQL
db_host = 'postgres'  # Nome do serviço do PostgreSQL no Docker Compose
db_port = '5432'
db_name = 'NOME_BANCO'
db_user = 'NOME_USER'
db_password = 'SENHA'

# Função para inserir dados do JSON no PostgreSQL
def insert_data_from_json(filename):
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = conn.cursor()

        # Abrir e ler o arquivo JSON
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                # Inserção de dados na tabela movies, usando aspas duplas para "cast"
                cursor.execute(
                    'INSERT INTO movies (title, year, "cast", genres) VALUES (%s, %s, %s, %s)',
                    (item['title'], item['year'], item['cast'], item['genres'])
                )

        conn.commit()
        print('Dados inseridos com sucesso!')

    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

# Chamada da função para inserir dados do JSON
insert_data_from_json('/scripts/movies.json')
