# import vonage
# client = vonage.Client(key="5b0f140f", secret="NBEBBAbQLQx4Y6iY")
# sms = vonage.Sms(client)
#
# responseData = sms.send_message(
#     {
#         "from": "Vonage APIs",
#         "to": "998939113123",
#         "text": "Assalomu alaykum !Bu robocode.uz dan test xabar.",
#     }
# )
#
# if responseData["messages"][0]["status"] == "0":
#     print("Message sent successfully.")
# else:
#     print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
import requests

url = "https://smsapi-com3.p.rapidapi.com/sms.do"

querystring = {"access_token":"MyeeIuND5287V2hCipGBGmsmeG8GJg2MO0uTV4Cl"}

payload = "{\n  \"to\":998939113123 \"\",\n  \"message\": Qale ishla\"\",\n  \"from\": \"\",\n  \"normalize\": \"\",\n  \"group\": \"\",\n  \"encoding\": \"\",\n  \"flash\": \"\",\n  \"test\": \"\",\n  \"details\": \"\",\n  \"date\": \"\",\n  \"date_validate\": \"\",\n  \"time_restriction\": \"follow\",\n  \"allow_duplicates\": \"\",\n  \"idx\": \"\",\n  \"check_idx\": \"\",\n  \"max_parts\": \"\",\n  \"fast\": \"\",\n  \"notify_url\": \"\",\n  \"format\": \"json\"\n}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "smsapi-com3.p.rapidapi.com",
    'x-rapidapi-key': "0202709d4emshbe87778ed9b4962p1f76cdjsn4a200e532763"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
