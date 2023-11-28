from dataclasses import dataclass
from FilterByArp import FilterByArp

from SetInterface import SetInterface

OUTPUT_FILE_PREFIX = "output"
MAX_LINES_PER_FILE = 10000
file_counter = 0

filename=""

if SetInterface.getlogfile(SetInterface.get_conffile()):
    filename = SetInterface.getlogfile(SetInterface.get_conffile())
else:
    filename = f"{OUTPUT_FILE_PREFIX}_{file_counter}.txt"

line_count = 0

@dataclass
class Write_to_file:
    def write_to_file(line):
        global file_counter
        global line_count
        global filename

        if line_count == 0 or line_count % MAX_LINES_PER_FILE == 0:
            file_counter += 1
            if SetInterface.getlogfile(SetInterface.get_conffile()):
                filename = f"{SetInterface.getlogfile(SetInterface.get_conffile())}_{file_counter}.txt"
            else:
                filename = f"{OUTPUT_FILE_PREFIX}_{file_counter}.txt"
            with open(filename, "w") as file:
                file.write(line)
        else:
            with open(filename, "a") as file:
                file.write(line)

        line_count+=1
        return filename