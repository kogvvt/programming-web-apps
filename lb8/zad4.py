import imaplib
import email

def check_unread_messages(server, port, username, password):
    try:
        mail = imaplib.IMAP4_SSL(server, port)

        mail.login(username, password)

        mail.select("INBOX")

        result, data = mail.search(None, "UNSEEN")
        if result == "OK":
            message_ids = data[0].split()
            if message_ids:
                print("Unread messages found:")
                for message_id in message_ids:
                    result, message_data = mail.fetch(message_id, "(RFC822)")
                    if result == "OK":
                        raw_email = message_data[0][1]
                        email_message = email.message_from_bytes(raw_email)
                        print("Subject:", email_message["Subject"])
                        print("From:", email_message["From"])
                        if email_message.is_multipart():
                            for part in email_message.walk():
                                content_type = part.get_content_type()
                                if "text/plain" in content_type:
                                    print("Body:")
                                    print(part.get_payload(decode=True).decode())
                        else:
                            print("Body:")
                            print(email_message.get_payload(decode=True).decode())
                        mail.store(message_id, "+FLAGS", "\\Seen")
                        print("Marked as read\n")
            else:
                print("No unread messages in INBOX")
        else:
            print("Failed to fetch unread messages")

        mail.logout()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    server = "212.182.24.27"
    port = 143
    username = "pasinf2017@infumcs.edu"
    password = "P4SInf2017"
    check_unread_messages(server, port, username, password)