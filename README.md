
# JSON_BD
Solução para inserir arquivo JSON no banco de dados PostgreSQL com Python.
Pois preciso utilizar o mecanismo de busca elastic search para consultar os dados no banco e as informações nesse banco através da tabela 'movies' foi esse conteúdo do JSON.
PASSOS: 
Estruturas de pastas:

PASTA RAIZ

├── docker-compose.yml

PASTA -> python-service

│   ├── Dockerfile
│   ├── requirements.txt
│   └── insert_data.py

PASTA -> scripts

── seu_arquivo.json
    
Acompanhe os arquivos para compreender a estrutura de cada um.

No final teste no prompt de comando do terminal.
Reconstruir e Iniciar os Contêineres: docker-compose up --build -d
Verificar os Logs do Serviço Python: docker-compose logs python

