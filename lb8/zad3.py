import imaplib

def check_all_mailboxes(server, port, username, password):
    try:
        mail = imaplib.IMAP4_SSL(server, port)
        mail.login(username, password)

        result, data = mail.list()
        if result == "OK":
            total_messages = 0
            for mailbox_info in data:
                flags, delimiter, mailbox_name = mailbox_info.decode().partition(' ')
                result, data = mail.select(mailbox_name)
                if result == "OK":
                    num_messages = int(data[0])
                    total_messages += num_messages
                    print(f"Mailbox '{mailbox_name}' has {num_messages} messages")
            print(f"Total messages across all mailboxes: {total_messages}")
        else:
            print("Failed to fetch mailbox list")

        mail.logout()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    server = "212.182.24.27"
    port = 143
    username = "pasinf2017@infumcs.edu"
    password = "P4SInf2017"
    check_all_mailboxes(server, port, username, password)