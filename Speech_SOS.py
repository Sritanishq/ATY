from twilio.rest import Client
import keys
#intializes account_sid and auth_token
client = Client(keys.account_sid, keys.auth_token)

#help function
def help_sos():
    #content of the message
    message = client.messages.create(
        body = "Hello this is a sample text message",
        from_ = keys.twilio_number,
        to= keys.target_no
    )