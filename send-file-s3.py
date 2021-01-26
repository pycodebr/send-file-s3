import boto3

# Cria o serviço com as suas credenciais da AWS #
s3 = boto3.client(
    service_name='s3',
    region_name='***REGIÃO DO SEU BUCKET***', 
    aws_access_key_id='***SUA ACCESS_KEY***', 
    aws_secret_access_key='***SUA SECRET_KEY***'
)

# Sobe o arquivo para o local desejado no S3 #
s3.upload_file(r'pycode.jpg', '***SEU BUCKET***', 'pycode.jpg')