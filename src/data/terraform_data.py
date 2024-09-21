import pandas as pd

class TerraformData:
    def __init__(self, terraform_id, planet_id, start_time, end_time, terraform_params, metrics):
        self.terraform_id = terraform_id
        self.planet_id = planet_id
        self.start_time = start_time
        self.end_time = end_time
        self.terraform_params = terraform_params
        self.metrics = metrics

    def to_dict(self):
        return {
            'terraform_id': self.terraform_id,
            'planet_id': self.planet_id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'terraform_params': self.terraform_params,
            'metrics': self.metrics
        }

class TerraformDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.data = self.load_data()

    def load_data(self):
        data = []
        with open(self.db_file, 'r') as f:
            for line in f:
                terraform_id, planet_id, start_time, end_time, terraform_params, metrics = line.strip().split(',')
                data.append(TerraformData(terraform_id, planet_id, start_time, end_time, terraform_params, metrics))
        return data

    def get_data(self, terraform_id):
        for data in self.data:
            if data.terraform_id == terraform_id:
                return data
        return None

    def add_data(self, data):
        self.data.append(data)
        with open(self.db_file, 'a') as f:
            f.write(','.join([data.terraform_id, data.planet_id, data.start_time, data.end_time, data.terraform_params, data.metrics]) + '\n')

# Example usage
db = TerraformDatabase('terraform_data.csv')
data = db.get_data('TERRAFORM-1')
print(data.to_dict())

new_data = TerraformData('TERRAFORM-2', 'KEPLER-62F', '2022-01-01', '2022-01-31', '0.5,0.8,250', '0.9,0.8,0.7')
db.add_data(new_data)
