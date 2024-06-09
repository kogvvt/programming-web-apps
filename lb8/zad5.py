import imaplib

def delete_message(server, port, username, password, message_number):
    try:
        mail = imaplib.IMAP4_SSL(server, port)
        mail.login(username, password)
        mail.select("INBOX")
        mail.store(message_number, "+FLAGS", "\\Deleted")
        mail.expunge()
        print("Message deleted successfully")
        mail.logout()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    server = "212.182.24.27"
    port = 143
    username = "pasinf2017@infumcs.edu"
    password = "P4SInf2017"
    message_number = input("Enter the message to delete: ")
    delete_message(server, port, username, password, message_number)