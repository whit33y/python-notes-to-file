import os
import time

while True:
    try:
        read_or_write = input('r-read\nw-write\nd-delete\ne-exit\n')
        read_or_write=read_or_write.lower()
        if read_or_write == 'r':
            file_open = open('notes.txt', 'r')
            lines_from_file = file_open.readlines()
            os.system('clear')
            for line, number in enumerate(lines_from_file):
                print(line,number)
            time.sleep(4)
            file_open.close()
        elif read_or_write == 'w':
            file_open = open('notes.txt', 'a')
            note = input('Your note: \n')
            if note.isspace() == False:
                os.system('clear')
                print('Your note: ',note)
                helper = '\n'
                note_with_newline = note + helper
                file_open.writelines(note_with_newline)
            file_open.close()
        elif read_or_write == 'd':
            try:
                lines = []
                file_open = open('notes.txt', 'r+')
                lines = file_open.readlines()
                file_open.close()
                line_to_delete = int(input('Give me num of line to delete: '))
                if line_to_delete == 0:
                    continue
                else:
                    file_open = open('notes.txt', 'w')
                    num=0
                    for line in lines:
                        if num != line_to_delete:
                            file_open.writelines(line)
                        num+=1
                    file_open.close()
            except:
                print('Something went wrong')
        elif read_or_write == 'e':
            exit()
    except ValueError:
        print('Wrong command')





# note = 'Siema\n'
# file_write = open('notes.txt', 'a')
# file_write.writelines(note)
# file_write.close()
# file_open = open('notes.txt', 'r+')
# lines_from_file = file_open.readlines()
# for line in lines_from_file:
#     print(line)