import requests

URL = "https://codehs.com/student/5481664/section/742213/assignment/186782676"
page = requests.get(URL)

results = page.text
print(results)