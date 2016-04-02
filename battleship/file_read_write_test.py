

opening_files_txt = """You should immediately notice that we import another handy command named exists. \n
This returns True if a file exists, based on its name in a string as an argument. \n
It returns False if not. We'll be using this function in the second half of this book to do lots of things, \n
but right now you should see how you can import it. \n

Using import is a way to get tons of free code other better (well, usually) \n
programmers have written so you do not have to write it. """

new_file = r'C:\Users\okwen\dev\gitrepos\python\battleship\open_test.py'

object_new_file = open(new_file, 'w')

object_new_file.write(opening_files_txt)

object_new_file.close()


object_new_file = open(new_file, 'r')

for line in new_file:
    if line != '':
        print(object_new_file.readline())
    if line == '':
        print('Finished reading file')
        
object_new_file.close()
