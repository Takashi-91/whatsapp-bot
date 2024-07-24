import os
from twilio.rest import Client # type: ignore
import schedule # type: ignore
import time

# Twilio credentials
account_sid = 'ACbf37d8598be8021a923b560f28deed2'
auth_token = '8f8eb32bc3a487c0bd956ef2710ff88'
client = Client(account_sid, auth_token)

# Function to send a message
def send_message():
    message = client.messages.create(
        from_='whatsapp:+17627877142',  
        body='Your pre-set message',
        to='whatsapp:+27680783232'  
    )
    print(f'Message sent: {message.sid}')




# Schedule the message
schedule.every().day.at("10:30").do(send_message) 

while True:
    schedule.run_pending()
    time.sleep(1)
