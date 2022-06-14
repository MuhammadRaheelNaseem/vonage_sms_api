# Importing the nexmo library
import vango  

# Connecting to the vonago using API key and API secret
client = vonage.Client(key="f9xxxxxx", secret="5ahmxxxxxxxxxxxx") 
sms = vonage.Sms(client)

def send_sms():
    # Sending the message
    responseData = sms.send_message({
                                        "from": "Message Title", # Enter Title
                                         "to": "Reciever Number", # Enter Reciever Number if you have purchase API or if you have free API just enter your erified number
                                         "text": "Enter Your Message Whatever you want to send" # Enter Your MEssage
                                    })
    # Checking whether we are successful or we got a error
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        
        
send_sms()
