import boto3
from prettytable import PrettyTable

# Cria o cliente EC2
ec2 = boto3.client('ec2')

# Consulta todos os volumes EC2
volumes = ec2.describe_volumes()

# Cria a tabela
table = PrettyTable()
table.field_names = ['Volume ID', 'Availability Zone', 'Volume Type', 'State', 'Snapshot ID','Encrypt', 'Size']

# Percorre os volumes EC2 e adiciona as informações na tabela
for volume in volumes['Volumes']:
    volume_id = volume['VolumeId']
    availability_zone = volume['AvailabilityZone']
    volume_type = volume['VolumeType']
    state = volume['State']
    snapshot_id = volume['SnapshotId']
    #snapshot_state = volume['SnapshotState']
    #device_name = volume['Attachments'][0]['Device']
    encrypt = volume['Encrypted']
    size = volume['Size']
    
    table.add_row([volume_id, availability_zone, volume_type, state, snapshot_id, encrypt, size])

# Imprime a tabela
print(table)
