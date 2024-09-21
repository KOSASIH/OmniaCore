import boto3
import os

class CloudInfrastructure:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region):
        self.ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region)
        self.s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region)

    def create_instance(self, instance_type, ami_id, security_group_id, subnet_id):
        response = self.ec2.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            SecurityGroupIds=[security_group_id],
            SubnetId=subnet_id,
            MaxCount=1,
            MinCount=1
        )
        return response['Instances'][0]['InstanceId']

    def create_bucket(self, bucket_name):
        self.s3.create_bucket(Bucket=bucket_name)

    def upload_file(self, bucket_name, file_name, file_path):
        self.s3.upload_file(file_path, bucket_name, file_name)

    def create_security_group(self, group_name, description):
        response = self.ec2.create_security_group(GroupName=group_name, Description=description)
        return response['GroupId']

    def create_subnet(self, vpc_id, cidr_block):
        response = self.ec2.create_subnet(VpcId=vpc_id, CidrBlock=cidr_block)
        return response['Subnet']['SubnetId']

# Example usage
cloud_infrastructure = CloudInfrastructure('AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'us-west-2')
instance_id = cloud_infrastructure.create_instance('t2.micro', 'ami-abc123', 'sg-abc123', 'subnet-abc123')
print(instance_id)

bucket_name = 'my-bucket'
cloud_infrastructure.create_bucket(bucket_name)
cloud_infrastructure.upload_file(bucket_name, 'file.txt', '/path/to/file.txt')

security_group_id = cloud_infrastructure.create_security_group('my-sg', 'My security group')
print(security_group_id)

subnet_id = cloud_infrastructure.create_subnet('vpc-abc123', '10.0.1.0/24')
print(subnet_id)
