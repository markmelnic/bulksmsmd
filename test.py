from os import getenv
from dotenv import load_dotenv
from bulksmsmd import SMSClient

load_dotenv()

client = SMSClient(
    username=getenv("BULKSMSMD_USERNAME"),
    password=getenv("BULKSMSMD_PASSWORD"),
    sender=getenv("BULKSMSMD_SENDER"),
    proxy={"http": getenv("PROXY_URL"), "https": getenv("PROXY_URL")},
)

response = client.send_sms_simple(
    msisdn=getenv("TEST_RECIPIENT_PHONE_NUMBER"), body="Hello world!"
)

print(response)
