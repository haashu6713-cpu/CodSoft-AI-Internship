from datetime import datetime

print("=" * 50)
print("        MY SIMPLE CHATBOT")
print("=" * 50)

name = input("Enter your name: ")

print("\n" + " " * 28 + f"Bot: Hi {name}! 😊")
print(" " * 28 + "Bot: We can chat now.")
print(" " * 28 + "Bot: Type 'bye' to stop.\n")

while True:

    message = input(f"{name}: ").lower()

    # greetings
    if message == "hi" or message == "hello":
        print(" " * 28 + "Bot: Hello ")

    elif message == "hey":
        print(" " * 28 + "Bot: Heyy!")

    elif message == "good morning":
        print(" " * 28 + "Bot: Good morning ")

    elif message == "good evening":
        print(" " * 28 + "Bot: Good evening ")

    # basic questions
    elif message == "how are you":
        print(" " * 28 + "Bot: I'm good. What about you?")

    elif message == "what is your name":
        print(" " * 28 + "Bot: My name is Simple Chatbot.")

    elif message == "who made you":
        print(" " * 28 + "Bot: A student made me using Python ")

    elif message == "what can you do":
        print(" " * 28 + "Bot: I can chat and answer simple questions.")

    elif message == "are you real":
        print(" " * 28 + "Bot: Nope I'm just a chatbot.")

    elif message == "where are you from":
        print(" " * 28 + "Bot: I live inside Python code ")

    # date and time
    elif message == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print(" " * 28 + f"Bot: Current time is {current_time}")

    elif message == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(" " * 28 + f"Bot: Today's date is {current_date}")

    # fun responses
    elif message == "tell me a joke":
        print(" " * 28 + "Bot: Why do programmers hate bugs?")
        print(" " * 28 + "Bot: Because they bug them ")

    elif message == "favorite color":
        print(" " * 28 + "Bot: I like blue ")

    elif message == "favorite food":
        print(" " * 28 + "Bot: I don't eat  but pizza sounds good!")

    elif message == "do you like music":
        print(" " * 28 + "Bot: Yes  but I can't listen properly.")

    elif message == "are you smart":
        print(" " * 28 + "Bot: A little bit ")

    elif message == "thank you":
        print(" " * 28 + "Bot: Welcome ")

    elif message == "bye":
        print(" " * 28 + f"Bot: Bye {name}! Have a nice day ")
        break

    else:
        print(" " * 28 + "Bot: Sorry, I didn't understand that.")