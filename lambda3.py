import boto3
import psycopg2
import json

secretsmanager = boto3.client('secretsmanager')

"""O boto3 permite fazer a integração python com os serviços existentes da amazon"""

def get_database_credentials(secret_name):
    """Pegando as credenciais do banco de dados do Secrets Manager."""
    response = secretsmanager.get_secret_value(SecretId=secret_name)
    secret = json.loads(response['SecretString'])
    return secret

def lambda_handler(event, context):
    # resgatando credenciais do banco de dados
    db_credentials = get_database_credentials('YourSecretName')

    # Conectar ao banco de dados
    try:
        connection = psycopg2.connect(
            dbname=db_credentials['dbname'],
            user=db_credentials['username'],
            password=db_credentials['password'],
            host=db_credentials['host'],
            port=db_credentials['port']
        )