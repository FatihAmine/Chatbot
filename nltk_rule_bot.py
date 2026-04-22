from nltk.chat.util import Chat, reflections


pairs = [
    (r"hello", ["Hello! How can I help you?"]),
    (r"who are you\??", ["I am a simple chatbot."]),
    (r"my name is (.*)", ["Nice to meet you, %1."]),
    (r"help", ["Try: hello, who are you, my name is ... , bye"]),
    (r"bye", ["Bye!"]),
    (r"(.*)", ["I don't understand."]),
]

chatbot = Chat(pairs, reflections)

if __name__ == "__main__":
    chatbot.converse()
