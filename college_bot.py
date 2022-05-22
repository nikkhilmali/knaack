import random
college_name = "Techno India NJR Institute of Technology"
bot_name = "Knaack"
mood = "horny"
resp = {
    "What's your college name?": [
        "Techno India NJR Institute of Technology"],
    "What's your name?": [
        "They call me {0}".format(bot_name),
        "I usually go by {0}".format(bot_name),
        "My name is the {0}".format(bot_name)],
    "How are you?": [
        "I'm feeling {0}".format(mood),
        "{0}! How about you?".format(mood),
        "I am {0}! How about yourself?".format(mood), ],
    "": [
        "Hi! Are you there?",
        "What do you mean by these?",
    ],
    "default": ["This is a default message"]
}


def res(message):
    if message in resp:
        bot_message = random.choice(resp[message])
    else:
        bot_message = random.choice(resp["default"])
    return bot_message


def real(xtext):
    if "college" in xtext:
        ytext = "What's your college name?"
    elif "name" in xtext:
        ytext = "What's your name?"
    elif "mood" in xtext:
        ytext = "how are you?"
    else:
        ytext = ""
    return ytext


def send_message(message):
    print(message)
    response = res(message)
    print(response)


while 1:
    my_input = input()
    my_input = my_input.lower()
    related_text = real(my_input)
    send_message(related_text)
    if my_input == "exit" or my_input == "stop":
        break
