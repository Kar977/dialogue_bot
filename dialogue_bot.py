import re
from time import sleep

"""This is my first little 'project'.
    It is simple dialogue chat bot.
    Responding on programmed returns about car dealership - support."""

class SupportBot:

    exit_commands = ("exit", "leave", "quit", "goodbye", "bye")

    def __init__(self):
        self.matching_phrases = {"pay_for_service": [r"i*.*want.*pay.*for.*service.*", r"pay.*for.*service"]}

