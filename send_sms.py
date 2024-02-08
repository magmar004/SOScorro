from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "AC48afc639c87adb25a7bb6df59b38988f"
auth_token  = "40e4070ee4a8ede2611170e08f38b10a"

client = Client(account_sid, auth_token)


def crear_mensaje(link):
    message = client.messages.create(
    to="+595981415894",
    from_="+12672744332",
    body=f"BUENAS ESTOY EN PELIGRO Y NECESITO AYUDA! Mi ubicacion es: {link} ")

    return message
    
    