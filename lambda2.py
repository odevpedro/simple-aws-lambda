def handler(event, context):
    http_method = event['httpMethod']

    if http_method == 'GET':
        return get_handler(event)
    elif http_method == 'POST':
        return post_handler(event)
    elif http_method == 'PUT':
        return put_handler(event)
    elif http_method == 'DELETE':
        return delete_handler(event)
    else:
        return {
            'statusCode': 400,
            'body': 'Método HTTP não suportado'
        }

def get_handler(event):
    # Logic for reading data goes here.
    # For this example, let's just return a message.
    return {
        'statusCode': 200,
        'body': 'Dados lidos com sucesso!'
    }

def post_handler(event):
    # Logic for creating data goes here.
    # You might extract data from the event['body'] to create a new item.
    return {
        'statusCode': 201,
        'body': 'Dados criados com sucesso!'
    }

def put_handler(event):
    # Logic for updating data goes here.
    # You might use data from the event['body'] to update an existing item.
    return {
        'statusCode': 200,
        'body': 'Dados atualizados com sucesso!'
    }

def delete_handler(event):
    # Logic for deleting data goes here.
    # For instance, you might use an ID from the event to delete an item.
    return {
        'statusCode': 200,
        'body': 'Dados excluídos com sucesso!'
    }
