import random
import sys

def randomize_command_line_inputs():
    command_line_inputs = sys.argv
    command_line_inputs_no_filename = command_line_inputs[1:]
    random.shuffle(command_line_inputs_no_filename)
    print command_line_inputs_no_filename

if __name__ == '__main__':
    randomize_command_line_inputs()
