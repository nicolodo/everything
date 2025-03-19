
# ex9 Messages

messages = [
    'hi how are you doing?',
    'whats up',
    'that was really funny what you just said there',
    'hohoho merry christmas',
    'brilliant',
    'philantropy',
    'phlogiston was a great idea'
]

def ex9():
    showMessages(messages)

def showMessages(messages):
    for msg in messages:
        print(msg)

def sendMessages(unsentMsgs, sentMsgs):
    while unsentMsgs:
        currentMsg = unsentMsgs.pop()
        print(currentMsg)
        sentMsgs.append(currentMsg)

def unsentSentCheck(unsentMsgs,sentMsgs):
    print(f"unsent: {unsentMsgs}")
    print(f"sent: {sentMsgs}")

# sending messages ex 10

def ex10():
    unsentMessages = messages[:] # ex 11 archive test
    sentMessages = []
    sendMessages(unsentMessages,sentMessages)
    # unsentSentCheck(unsentMessages,sentMessages)
    unsentSentCheck(messages,sentMessages) # ex11 archive test

# archived messages
ex10()