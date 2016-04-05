from os.path import isfile, isdir
from os import makedirs, system
import shutil

opening_files_txt = """You should immediately notice that we import another handy command named exists. \n This returns True if a file exists, based on its name in a string as an argument. \n
It returns False if not. We'll be using this function in the second half of this book to do lots of things, \n but right now you should see how you can import it. \n Using import is a way to get tons of free code other better (well, usually) \n
programmers have written so you do not have to write it. """


new_file = r'.\open_test.txt'

if isfile(new_file)  == True:
    print ('This file already exists' )
else:
    
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

sub_dir = './text/'
makedirs(sub_dir, exist_ok=True)



def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)
        

copy_file (new_file, sub_dir )        
old_filename = 'open_test'
new_filename ='copied_open_test.txt'
system('old_filename new_filename')