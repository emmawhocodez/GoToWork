import smtplib
import random
import config

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    affirmations = []

    with open(config.affirmations_file) as f:
        for line in f:
            line = line.strip()
            affirmations.append(line)

    random_int = random.randint(0, len(affirmations) - 1)
    random_affirmation = affirmations[random_int]

    sender = config.sender
    recipient = config.recipient
    title = "Go To Work!"
    content = f'FROM {sender}\nTO: {recipient}\nSUBJECT: {title}\n\n{random_affirmation}'

    smtp_server = "smtp.mail.yahoo.com"
    server = smtplib.SMTP(smtp_server, 587)

    try:
        server.ehlo()
        server.starttls()
        server.login(config.username, config.password)
        server.sendmail(sender, recipient, content)
        server.close()

    except Exception as e:
        server.close()


