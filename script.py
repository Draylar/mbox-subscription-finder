import mailbox
mbox = mailbox.mbox("mail.mbox")

# Store a list of unique email addresses with 'subscribe' somewhere in the email contents
emails = set()

# Store total emails & counted emails for progress counter
total_email_count = len(mbox.items())
checked_emails = 0

# Iterate over all read mail entries
for message in mbox:
    checked_emails = checked_emails + 1
    email_from = message['from']

    # Emails come in the format :     Name <Email>   : , so we extract the email part here.
    if('<' in email_from):
        email_from = email_from[int(email_from.index("<")) + 1 : int(email_from.index(">"))]

    # Log total progress so far
    print("Progress: ", checked_emails / total_email_count)
    if('unsubscribe' in message.as_bytes().decode(encoding='UTF-8').lower()):
        emails.add(email_from);

# Print all emails found
for email in emails:
    print(email)
