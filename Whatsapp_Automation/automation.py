# Twilio----> library to send Whatsapp messages to users
# Datetime----> to schedule messages
# Time----> to add delays in the program

#1.twilio client setup
#2.user inputs.
#3. scheduling logic
#4.sending messages using twilio client

# Step 1: Import necessary libraries
from twilio.rest import Client # client---->whatsapp msg send krne k liye
from datetime import datetime,timedelta #datetime----> time manage krne k liye,timedelta-->time difference calculate krne k liye
import time
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


# Step2: Get credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
account_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, account_token)

# Step 3: designing the function to send whatsapp message
def send_whatsapp_message(to, message):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # This is Twilio's sandbox number for WhatsApp
            body=message,
            to=f'whatsapp:{to}'
        )
        print(f"Message sent to {to} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"Failed to send message to {to}. Error: {str(e)}")

#step 4: User inputs
to = input("Enter the recipient's WhatsApp number with country code (e.g., +1234567890): ")
message= input("Enter the message you want to send: ")

#step 5: parsing date and time and calculating delay
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ")

#datetime object create krna
scheduled_datetime_str = datetime.strptime(f"{date_str} {time_str}","%Y-%m-%d %H:%M")
current_datetime = datetime.now()

print("Current system time:", current_datetime.strftime('%Y-%m-%d %H:%M'))
print("Scheduled time:", scheduled_datetime_str.strftime('%Y-%m-%d %H:%M'))

#calculating delay
time_difference = scheduled_datetime_str - current_datetime
delay_in_seconds = time_difference.total_seconds()

if delay_in_seconds<=0:
    print("Scheduled time is in the past. Please enter a future date and time.")
    
else:
    print(f"Message scheduled to be sent at {scheduled_datetime_str.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(delay_in_seconds) #program ko delay krdo
    send_whatsapp_message(to, message) #message bhej do