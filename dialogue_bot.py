import re
from time import sleep

"""This is my first little 'project'.
    It is simple dialogue chat bot.
    Responding on programmed returns about car dealership - support."""

class SupportBot:

    exit_commands = ("exit", "leave", "quit", "goodbye", "bye")

    def __init__(self):
        self.matching_phrases = {"pay_for_service": [r"i*.*want.*pay.*for.*service.*", r"pay.*for.*service"],
                                 "request_for_order_progress": [r"(H|h)ow.*my.*order.*look\d*.*(like)?\\?*"],
                                 "cars_on_sale": [r"[Ss]how.*me.*car.*.*on.*sales*"]}


# Function to introduce and welcome our client.
    def hello_customer(self):
        name = input("Hello, I'm a customer support of a car dealership.\n"
                     "Our establishment is located on Niepodległości 17 street.\n"
                     "Before I can help you, I need you first and last name.\n")
        help_customer = input(f"Go-ahead {name}, how can I help you with?\n")

        if help_customer in self.exit_commands:
            print(f'Thank you for the conversation.\nHave a nice day {name}')
            return
        return self.handle_conversation(help_customer)

    def handle_conversation(self, reply):
        while not self.make_exit(reply):
            reply = input("How is going?")

    def make_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                print(f"Thank you for the conversation.\nHave a nice day.")
                return True
        return False

    def match_replay(self, reply):

        for key, value in self.matching_phrases.items():
            for regex_pattern in value:
                match_regex = re.match(regex_pattern, reply)
                if match_regex and key == "pay_for_service":
                    return self.pay_service()
                if match_regex and key == "cars_on_sale":
                    return self.show_cars_on_sale()

#In the correct version the function should put through online payment
    def pay_service(self):
        print("Waiting for save connection...")
        sleep(3)
        print("Waiting for save connection... ")
        sleep(1)
        return "CONNECTION ERROR\n Try to connect later.\nSorry for trouble.\n"
    
    def show_cars_on_sale(self):
        
        parameters = input("")


SupportConversatoin = SupportBot()

SupportConversatoin.hello_customer()
