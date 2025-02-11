import requests  

# GET请求示例  
response = requests.get("https://reqres.in/api/users/2")  
print("状态码：", response.status_code)  
print("响应数据：", response.json())  

# POST请求示例  
data = {"name": "John", "job": "leader"}  
response = requests.post("https://reqres.in/api/users", json=data)  
print("创建用户ID：", response.json()["id"])  