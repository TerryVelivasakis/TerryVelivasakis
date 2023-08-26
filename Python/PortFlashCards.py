#this simple program is to help study for the Network+ exam to act as flash cards and ask which port coorelates to which servie


import random
#Create Dictionary of Protocols and their associated Port Numbers
protoport = {
"File Transfer Protocol (FTP)" : "20/21",
"Secure Shell (SSH)" : "22",
"Secure File Transfer Protocol (SFTP)": "22",
"Telnet": "23",
"Simple Mail Transfer Protocol (SMTP)":"25",
"Domain Name System (DNS)":"53",
"Dynamic Host Configuration Protocol (DHCP)":"67/68",
"Trivial File Transfer Protocol (TFTP)": "69",
"Hypertext Transfer Protocol (HTTP)" : "80",
"Post Office Protocol v3 (POP3)" : "110",
"Network Time Protocol (NTP)" : "123",
"Internet Message Access Protocol (IMAP)" : "143",
"Simple Network Management Protocol (SNMP)":"161/162",
"Lightweight Directory Access Protocol (LDAP)":"389",
"Hypertext Transfer Protocol Secure (HTTPS) [Secure Sockets Layer (SSL)]":"443",
"HTTPS [Transport Layer Security (TLS)]":"443",
"Server Message Block (SMB)":"445",
"Syslog":"514",
"SMTP TLS":"587",
"Lightweight Directory Access Protocol (over SSL) (LDAPS)":"636",
"IMAP over SSL":"993",
"POP3 over SSL":"995",
"Structured Query Language (SQL) Server":"1433",
"SQLnet":"1521",
"MySQL":"3306",
"Remote Desktop Protocol (RDP)":"3389",
"Session Initiation Protocol (SIP)":"5060/5061"
}

#convert Dictionary to list of tuples
protoportList = list(protoport.items())

#Set Variables to 0 for scoring
questions = 0
correctAnswers = 0
x=0

askedPorts = ["a","b","c"]
print (len(askedPorts))




while x == 1:
    selection = random.choice(protoportList)
    while (selection[0] in askedPorts):
        selection = random.choice(protoportList)
    askedPorts.append(selection[0])

    if (len(askedPorts < 10)):
        askedPorts.pop(0)
    answer = input (f"What port(s) does {selection[0]} run on? (exit to quit): ")
    if (answer == "exit"):
        print(f"you got {correctAnswers} out of {questions}.  {int((correctAnswers/questions)*100)}%")
        x=1
    else:
        questions += 1
        if (answer == selection[1]):
            print("Correct!")
            correctAnswers += 1
        else:
            print(f"No, the correct answer is port {selection[1]}.")


