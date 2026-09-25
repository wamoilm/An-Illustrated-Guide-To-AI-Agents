import json
from pprint import pprint
import urllib.request


url = "http://localhost:11434/api/chat"
headers = {"Content-Type": "application/json"}
request = json.dumps({
	"model": "gemma4:e4b",
	"messages": [
		{"role": "user", "content": "How are you today?"}
	],
	"stream": False,
}).encode("utf-8")

request_call = urllib.request.Request(url, data=request, headers=headers, method="POST")
response = urllib.request.urlopen(request_call).read()
# parsed_response = json.loads(response.decode("utf-8"))
# print(parsed_response["message"]["content"])

with urllib.request.urlopen(request_call) as response:
    data = json.loads(response.read())
    pprint(data)


