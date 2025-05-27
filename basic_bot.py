while True:
    msg=input("You : ")
    if "hello" in msg.lower():
        print("Bot : Hi there. How are you?")
    
    elif "hi" in msg.lower():
        print("Bot : Hi there. How are you?")
    elif "fine" in msg.lower():
        print("Bot : Good")
    elif "what about you" in msg.lower():
        print("Bot : I am fine, too. What can I help?")
    elif "bye" in msg.lower():
        print("Bot : Ok, bye. Have a good day")
        break
    else:
        print("Bot : I don't understand what are you saying")