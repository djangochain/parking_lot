import os, sys
from parking import Parking


class ParkingCommands(object):

    def __init__(self):
        self.parking = Parking()

    def process_input(self):
        try:
            while True:
                stdin = input("Enter command: ")
                self.process_command(stdin)
        except (KeyboardInterrupt, SystemExit):
            return
        except Exception as ex:
            print("Error occurred while processing input %s" % ex)

    def process_command(self, stdin):
        inputs = stdin.split()
        command,params = inputs[0],inputs[1:]
        if hasattr(self.parking, command):
            command_func = getattr(self.parking, command)
            command_func(*params)
        else:
            print("Not a valid command")


if __name__ == "__main__":
    pk_command = ParkingCommands()
    pk_command.process_input()
   