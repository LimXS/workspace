import requests

response=requests.get("https://api.vdian.com/oauth2/authorize?appkey=630426&redirect_uri=http://eshopgateway.mygjp.com&response_type=code&state=123")
print response.text