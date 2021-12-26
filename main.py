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

igniteExecutiveCouncilMembers = [
    "hamna.haider19389@fpseagles.com",
    "sarim.ahmed19621@fpseagles.com",
    "zara.hasan19963@fpseagles.com",
    "alyssa20189@fpseagles.com",
    "naurays21213@fpseagles.com",
    "shanzey.aamir19391@fpseagles.com",
    "maidah.rafi19383@fpseagles.com",
    "ayma.munir20039@fpseagles.com",
    "Abbas20394@fpseagles.com",
    "Amal20378@fpseagles.com",
    "Muhammad21072@fpseagles.com",
    "Altamash20419@fpseagles.com",
    "Natasha20584@fpseagles.com",
    "Mayur21068@fpseagles.com",
    "SYEDA21296@fpseagles.com",
    "Anzila20432@fpseagles.com",
    "Yuneeb20466@fpseagles.com",
    "Shanzay20278@fpseagles.com",
    "Mustafa20368@fpseagles.com",
    "Hana20301@fpseagles.com",
    "Nitin20311@fpseagles.com",
    "dua.khan19393@fpseagles.com",
    "iqan.ahmad19395@fpseagles.com",
    "nehan.haroon19407@fpseagles.com",
    "awwab.aftab19371@fpseagles.com",
    "anusha.farooqi19390@fpseagles.com",
    "aliyah.haq19386@fpseagles.com",
    "Hassaan20357@fpseagles.com",
    "Sara20318@fpseagles.com",
    "Ahmad20444@fpseagles.com",
    "Sarrah20429@fpseagles.com",
    "Aliza20307@fpseagles.com",
    "Bayan20780@fpseagles.com",
    "Hussain20371@fpseagles.com",
    "Rohaan20362@fpseagles.com",
    "mirza.baig20050@fpseagles.com",
    "Misha20445@fpseagles.com",
    "omar.khan19397@fpseagles.com",
    "marium.ashraf19368@fpseagles.com",
    "Muhammad20985@fpseagles.com",
    "aarfa.bano19372@fpseagles.com",
    "KHADIJA21254@fpseagles.com",
    "Safwan20479@fpseagles.com",
    "Rafeeyah21051@fpseagles.com",
    "Rida21004@fpseagles.com",
    "Abdullah21159@fpseagles.com",
    "Razieh20608@fpseagles.com",
    "hassaan.tariq19373@fpseagles.com",
    "ALI21291@fpseagles.com",
    "sheheryar.salman19377@fpseagles.com",
    "hafsa20478@fpseagles.com",
    "Fawad21070@fpseagles.com",
    "Aaliyan21158@fpseagles.com",
    "Minhaj20280@fpseagles.com",
    "muhammad.taha19680@fpseagles.com",
    "KHADIJA20499@fpseagles.com",
]
clubMembers = [
    "sarim.shiekh10@gmail.com",
    "merium.mifta@fps.edu.pk",
    "sarim.ahmed19621@fpseages.com",
    "ahmad20444@fpseagles.com",
    "Ali21291@fpseagles.com",
    "alyssa20189@fpseagles.com",
    "daniyal.mehmood19985@fpseagles.com",
    "dua.khan19393@fpseagles.com",
    "fawad21070@fpseagles.com",
    "fraheemahmed2004@gmail.com",
    "hasan20291@gmail.com",
    "hassaan21131@fpseagles.com",
    "mir20290@fpseagles.com",
    "mirza.baig20050@fpseagles.com",
    "muhammad20450@fpseagles.com",
    "haris20108@fpseagles.com",
    "Muhammad20985@fpseagles.com",
    "Muhammad21091@fpseagles.com",
    "Najmuddin21165@fpseagles.com",
    "naveed21160@fpseagles.com",
    "safwan20479@fpseagles.com",
    "Taha21008@fpseagles.com",
    "zain21226@fpseagles.com",
    "Ahmed.meraj20051@fpseagles.com",
    "Iqan.ahmad19395@fpseagles.com",
    "aarfa.bano19372@fpseagles.com",
    "hassaan20357@fpseagles.com",
    "minhaj20280@fpseagles.com",
    "syed20991@fpseagles.com",
    "bareha21101@fpseagles.com",
    "bayan20780@fpseagles.com",
    "HASSAAN21229@fpseagles.com",
    "naurays21213@fpseagles.com",
    "Muhammad21155@fpseagles.com",
    "yuneeb20466@fpseagles.com",
    "shamoon21173@fpseagles.com",
    "alyssa20189@fpseagles.com",
]
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
