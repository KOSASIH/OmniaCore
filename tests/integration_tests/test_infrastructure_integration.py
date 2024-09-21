import pytest
from infrastructure import Infrastructure
from deployment import Deployment

@pytest.mark.django_db
def test_infrastructure_integration():
    # Test infrastructure integration with deployment
    infrastructure = Infrastructure()
    deployment = Deployment()
    input_data = {'environment': 'dev', 'instance_type': 't2.micro'}
    expected_output = {'environment': 'dev', 'instance_type': 't2.micro'}
    output = infrastructure.configure(input_data, deployment)
    assert output == expected_output

@pytest.mark.django_db
def test_deployment_integration():
    # Test deployment integration with infrastructure
    deployment = Deployment()
    infrastructure = Infrastructure()
    input_data = {'environment': 'dev', 'instance_type': 't2.micro'}
    expected_output = {'environment': 'dev', 'instance_type': 't2.micro'}
    output = deployment.deploy(input_data, infrastructure)
    assert output == expected_output
