import pyfiglet
from termcolor import colored
text = pyfiglet.figlet_format("Happy Valentines day", font="slant")

print(colored(text, 'red'))