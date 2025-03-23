Challenge “Pipeline de Telecomunicaciones”

Contexto: 
Telecom es una empresa de telecomunicaciones que opera a nivel nacional. Ofrecen servicios de internet, telefonía y TV por suscripción. La empresa está en proceso de modernizar su infraestructura de datos para optimizar el manejo de información sobre sus clientes, servicios contratados y facturación.
Actualmente, los datos de la empresa están distribuidos en diferentes fuentes, como bases de datos locales, archivos CSV y sistemas heredados. Esto dificulta la obtención de insights y genera problemas de rendimiento en los procesos de
facturación y análisis de clientes.
Telecom ha decidido adoptar una solución basada en la nube utilizando los servicios de AWS para implementar un pipeline de datos que automatice la ingesta, transformación y almacenamiento de información relevante en un Data Lake y un Data Warehouse. El Data Lake almacenará los datos en su forma original, mientras que el Data Warehouse permitirá realizar consultas optimizadas y análisis estructurados de los datos transformados.



Paso a Paso 

Paso 1. Configurar Entorno Local
    Istalar:Python 3.x,
            AWS CLI,
            pip install boto3  -> import boto3
            Git (configurar)
    En VSc: extensiones: Python (verificar interprete: ultima Version)
                        AWS toolkit (configurar credeciales)
                        git (GitLens)    

Paso 2. Carga bucket s3
    crer archivo 'example_data.csv' con los datos requeridos
    configurar servicio de CloudWhatch en AWS para advertencias de gastos
    asegurar usuario root con MFA
    crear un usuario IAM (user_s3-carga-data) solo con permisos personalizado para cargas en s3 (permisos_de_carga_en_s3.json)
        crear claves de accesos para este usuario IAM, y lo configurar cuenta en VSc
    crear un bucket desde VS code y subí el archivo 'example_data.csv' a travez de la consola de VS 
        'aws s3 cp example_data.csv s3://telecom-datalake-first/data/'

Paso 3.Configurar AWS Glue
a) AWS Glue, Crear Crawler
Configurar un rol de IAM con permisos sobre s3, Glue y IAM (para poder crear rol de glue)
Uso del servicio de AWS Glue
    Crear un Crawler que apunte al archivo del bucket s3
    Crear la base de datos de salida
    Revisar y Ejecutar el Crawler
b) Crear una carpeta en el bucket donde guardar un script (glue_etl_script.py)
crear el script glue_etl_script.py en VSc y subir en el destino 
    > aws s3 cp glue_etl_script.py s3://telecom-datalake-first/scripts/

crear carpeta 'transformed_data' como destino para el proximo paso.

Paso 4. Amazon Redshift 
Configurar Usuario IAM con permisos necesarios.
En el editor de comandos de Redshift crear tabla: 
    CREATE TABLE telecom_transformed (
        id_cliente INT,
        nombre_cliente VARCHAR(256),
        plan VARCHAR(255),
        fecha_inicio DATE,
        fecha_fin DATE,
        monto DECIMAL(19, 2),
        monto_total DECIMAL(10, 2)
    );
Ejecutar

Paso 5. Amazon Dynamodb
crear tabla "pipeline-config"
    clave primaria "id_pipeline"
crear script de python "dynamodb_logger.py" y con la biblioteca boto3 interactuar con el servicio. 
    El script toma los datos del log y los escribe en la tabla "pipeline-config", registrando las actividades del pipeline.

Paso 6. Amazon Athena
 configurar athena para buscar datos de s3 a travez de consuta sql.
    > select * from example_data.csv;

 Paso 7. Aws Glue Workflow
 Desde Aws Glue, configurar y crear un workflow. 
 Añadir una tarea para ejecutar automaticamente.

 

