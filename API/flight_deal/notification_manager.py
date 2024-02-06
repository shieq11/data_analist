from twilio.rest import Client

TWILIO_SID = "AC13b4d703e9bd7502191df26f04a37929"
TWILIO_AUTH_TOKEN = "cc1e0ec60c0ee2aec61101f46b0d0f37"
TWILIO_VIRTUAL_NUMBER = "+12134863846"
TWILIO_VERIFIED_NUMBER = "+31686288377"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "stefankorba50@gmail.com"
MY_PASSWORD = "0Q1j!b4aBWY+HPq2"
class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )