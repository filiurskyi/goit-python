import globals
from record import ConsolePrint
from user_actions_handler import get_handler
from utils.constants import INVITE_MESSAGE, TYPE_OR_ATTRIBUTE_ERROR_MESSAGE
from utils.parser import parser


def main():
    console = console_init()
    while globals.IS_LISTENING:
        user_line = input(INVITE_MESSAGE)
        if user_line:
            command, data = parser(user_line)
            handler = get_handler(command)
            try:
                result = handler(data)
                console.output(result)
                continue
            except AttributeError:
                print(f'{TYPE_OR_ATTRIBUTE_ERROR_MESSAGE} \n{get_handler("help")()}')


def console_init():
    return ConsolePrint()


if __name__ == "__main__":
    main()
