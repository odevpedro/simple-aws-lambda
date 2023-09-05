import mysql.connector
import boto3
import json

# Inicialize o cliente do Secrets Manager
secretsmanager = boto3.client('secretsmanager')

def get_database_credentials(secret_name):
    """Obter credenciais do banco de dados do AWS Secrets Manager."""
    response = secretsmanager.get_secret_value(SecretId=secret_name)
    secret = json.loads(response['SecretString'])
    return secret

def lambda_handler(event, context):
    # Resgatando credenciais do banco de dados
    db_credentials = get_database_credentials('YourSecretName')
    
    #conexão com o banco de dados
    connection = None
    try:
        connection = mysql.connector.connect(
            database=db_credentials['dbname'],
            user=db_credentials['username'],
            password=db_credentials['password'],
            host=db_credentials['host'],
            port=db_credentials['port']
        )

        # Determinar ação baseada no método HTTP do API Gateway
        http_method = event['httpMethod']
        
        if http_method == "GET":
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users;") #users = nome da tabela especifica
            result = cursor.fetchall()
            
            return {
                'statusCode': 200,
                'body': json.dumps(result)
            }

        # Crud

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({"error": "Unable to process the request"})
        }

    finally:
        if connection:
            connection.close()
