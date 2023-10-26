import http.client
import json

conn = http.client.HTTPSConnection("n8mp8j.api.infobip.com")
payload = json.dumps({
    "messages": [
        {
            "destinations": [
                {
                    "to": "5521970272132"
                }
            ],
            "from": "InfoSMS",
            "text": "Hello World"
        }
    ]
})
headers = {
    'Authorization': 'cadf5f4399fd7c12893ef2e8d5c05538-73d3912e-4fc2-46da-9999-8cddf751431e',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/sms/2/text/advanced", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))