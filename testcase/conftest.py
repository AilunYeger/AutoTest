import pytest
import os
from utils.sourceLoad import data

def case_data(case_name):
    return get_data().get(case_name)

def get_data():
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'source', 'test_data.yml')
    try:
        yaml_data = data.loadYaml(file_path)
    except Exception as e:
        pytest.skip(str(e))
    else:
        return yaml_data

