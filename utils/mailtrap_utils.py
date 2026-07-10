import mailtrap as mt


TOKEN = "96a30b86619077ef28a52d8655ca967e"
ACCOUNT_ID = 2781745
INBOX_ID = 4769793


def get_latest_email():

    client = mt.MailtrapClient(
        token=TOKEN,
        sandbox=True,
        account_id=ACCOUNT_ID,
        inbox_id=INBOX_ID
    )

    messages = client.testing_api.messages.get_list(
        INBOX_ID
    )

    if len(messages) == 0:
        print("No email received in Mailtrap")
        return None

    return messages[0]


email = get_latest_email()

print(email)