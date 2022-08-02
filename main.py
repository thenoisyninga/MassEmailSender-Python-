import smtplib
from email.message import EmailMessage

# These will be kept default
sender = "sarim.ahmed19621@fpseagles.com"
senderPassword = "fps@19621"

file1 = open("Subject.txt", "r+")
messageSubject = file1.read()
file1.close()

file2 = open("Body.txt", "r+")
messageBody = file2.read()
file2.close()

testRecipients = ["sarim.shiekh10gmail.com", "sarim.ahmed19621@fpseagles.com",]

notSendList = []
successCount = 0
failiureCount = 0

# Preparing Messages...
for recipient in testRecipients:
    msg = EmailMessage()
    msg['Subject'] = messageSubject
    msg['From'] = sender
    msg['To'] = recipient

    msg.set_content(messageBody)
    # Enter HTML message here....

    # Sending Messages...
    print(f'[+] Sending Message to {recipient}...')
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        # with smtplib.SMTP("localhost", 1025) as smtp:
        try:
            successCount += 1
            smtp.starttls()
            smtp.login(sender, senderPassword)
            smtp.send_message(msg)

            if recipient == "sarim.ahmed19621@fpseagles.com":
                check = input("All set?")
        except:
            notSendList.append(recipient)
            print(f"\n[-] Message was not sent to {recipient}.")
            failiureCount += 1
            successCount -= 1

print(f"{successCount} messages sent. \n{failiureCount} messages were not sent.")
print("Messages were not sent to these emails:\n")

for recipient in notSendList:
    print(recipient)
