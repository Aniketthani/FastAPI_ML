import requests

data={
  "sepal_length": 10,
  "sepal_width": 15,
  "petal_length": 7,
  "petal_width": 9
}

response=requests.post("http://127.0.0.1:8000/predict",json=data)


print(response.content)