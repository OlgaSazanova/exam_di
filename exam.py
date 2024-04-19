from utils import unzip_with_7z
import string

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW

for i in string.ascii_lowercase:
    for k in string.ascii_lowercase:   
        find_me = i+k
        if unzip_with_7z(zip_file_path, dest_path, find_me + 'bcmpda') == True:
            print('УРААААААААААА')
            print(i+k)

        else:
            continue

             
        
 
