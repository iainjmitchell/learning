import sys 

ENCODING = "utf-8"
FILE_NAME = "wasteland.txt"

file = open(file=FILE_NAME, mode="rt", encoding=ENCODING)
for line in file:
    sys.stdout.write(line)
file.close()

# safer
file = open(file=FILE_NAME, mode="rt", encoding=ENCODING)
try:
    for line in file:
        sys.stdout.write(line)
finally:
    file.close()

# safer & easier
with open(file=FILE_NAME, mode="rt", encoding=ENCODING) as a_file:
    for line in a_file:
        sys.stdout.write(line)