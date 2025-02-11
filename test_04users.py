import json  
import pytest  
import requests  

# 加载测试数据  
with open("test_04data.json") as f:  
    test_04data = json.load(f)  

@pytest.mark.parametrize("user_data", test_04data["users"])  
def test_create_user(user_data):  
    url = "https://jsonplaceholder.typicode.com/users"  
    response = requests.post(url, json=user_data)  
    assert response.status_code == 201  
    assert "id" in response.json()  