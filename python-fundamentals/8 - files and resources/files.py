ENCODING = "utf-8"
FILE_NAME = "wasteland.txt"

file = open(FILE_NAME, mode="wt", encoding=ENCODING)
file.write("first line\n")
file.write("Second line")
file.close()

read_file = open(file=FILE_NAME, mode="rt", encoding=ENCODING)
number_of_characters = 12
print(read_file.read(number_of_characters))
print(read_file.read()) # rest of file
read_file.seek(0) # go back to start

print(read_file.readline())
read_file.seek(0)
all_lines_in_list = read_file.readlines()
print(all_lines_in_list)
read_file.close()

append_file = open(file=FILE_NAME, mode="at", encoding=ENCODING)
append_file.writelines(
    ["a new line\n",
     "another"])
append_file.close()

read_again = open(file=FILE_NAME, mode="rt", encoding=ENCODING)
print(read_again.readlines())
read_again.close()
