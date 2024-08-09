import requests

response = requests.get("https://api.github.com/users/mohammadsyed397/repos")
complete_detail = response.json()
for i in range(len(complete_detail)):
    print(complete_detail[i]["name"])

