import os, sys
from parking import Parking


class ParkingCommands(object):

    def __init__(self):
        self.parking = Parking()

    def process_file(self, given_file):
        if not os.path.exists(given_file):
            print("Given file %s does not exist" % given_file)

        file_obj = open(given_file)
        try:
            while True:
                line = file_obj.readline()
                if line.endswith('\n'): line = line[:-1]
                if line == '': continue
                self.process_command(line)
        except StopIteration:
            file_obj.close()
        except Exception as ex:
            print("Error occurred while processing file %s" % ex)

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
        command, params = inputs[0], inputs[1:]
        if hasattr(self.parking, command):
            command_func = getattr(self.parking, command)
            command_func(*params)
        else:
            print("Not a valid command")


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        pk_command = ParkingCommands()
        pk_command.process_input()
    elif len(args) == 2:
        pk_command = ParkingCommands()
        pk_command.process_file(args[1])
    else:
        print(
            "Wrong number of arguments given in command.\nUsage:\n./parking_lot.py <filename> \nOR \n ./parking_lot.py")
