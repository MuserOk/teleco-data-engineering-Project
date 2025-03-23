import boto3
from datetime import datetime

# Conectar con DynamoDB
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")  
table = dynamodb.Table('pipeline-config')
try:
    # Insertar un log
    response = table.put_item(
        Item={
            'id_pipeline': 'pipeline_001',
            'status': 'Success',
            'timestamp': datetime.utcnow().isoformat()
        }
    ) 
    print("Log registrado con éxito:", response)
except Exception as e:
    print(f"Error ak ragistrar log:{e}")



#python insert_log.py   #para ejecutar