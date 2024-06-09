import imaplib

def check_inbox(server, port, username, password):
    try:
        mail = imaplib.IMAP4_SSL(server, port)
        mail.login(username, password)
        mail.select("INBOX")

        result, data = mail.search(None, "ALL")
        if result == "OK":
            message_ids = data[0].split()
            num_messages = len(message_ids)
            print(f"Number of messages in INBOX: {num_messages}")
        else:
            print("Failed to fetch messages")

        mail.logout()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    server = "212.182.24.27"
    port = 143
    username = "pasinf2017@infumcs.edu"
    password = "P4SInf2017"
    check_inbox(server, port, username, password)