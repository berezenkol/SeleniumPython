"""
File I/O
I - Input
O- Output

4 modes to use in python with files:
'w' - Write-Only Mode
'r' - Read-Only Mode
'r+' - Read & Write Mode
'a' - Append Mode
 """

# ex. of 'w'
# my_list = [1,2,3]
# my_file = open('C:/Users/Liudmila/Desktop/Luda/PYTHON/firstfile.txt', 'w')
#
# for item in my_list:
#     my_file.write(str(item) + '\n')   # 1.write function accepts ONLY strings:  2. + '\n' - \n adds the new line
#
# my_file.close()            # very important to close the fie at the end




# ex. of 'r' - how to read a file using python
# Reading an intire file -> .read()
# Reading line by line   -> .readline()


# my_fyle_toread = open('C:/Users/Liudmila/Desktop/Luda/PYTHON/secondfile.txt', 'r')
# print(str(my_fyle_toread.read()))
# my_fyle_toread.close()
#
# print('How to use .readline()--------------->')
#
# my_fyle_toread = open('C:/Users/Liudmila/Desktop/Luda/PYTHON/secondfile.txt', 'r')
# print(str(my_fyle_toread.readline()))    # first line read
# in order to read the second line just copy the code responsible for the first line and so on
# print(str(my_fyle_toread.readline()))    # second line read
# print(str(my_fyle_toread.readline()))    # third line read
#
# my_fyle_toread.close()

#______________________________________________#

"""
With/As keywords : used to close the file automatically if we forgot to write the .close() function
"""
# EXAMPLE WITH .CLOSE()
# third_file_write = open('C:/Users/Liudmila/Desktop/Luda/PYTHON/thirdfile.txt', 'w')
# third_file_write.write('It is very cool option I have learned today)))')
# third_file_write.close()
#
# third_file_read = open('C:/Users/Liudmila/Desktop/Luda/PYTHON/thirdfile.txt', 'r')
# print(str(third_file_read.read()))

# NOW WE WILL USE THE WITH/AS KEYWORDS TO WRITE THE CODE instead of using .close()

# with open('C:/Users/Liudmila/Desktop/Luda/PYTHON/with_as_file.txt', 'w') as file_to_write:
#     file_to_write.write('This is how we use WITH/AS instead of .close()')
#
# with open('C:/Users/Liudmila/Desktop/Luda/PYTHON/with_as_file.txt','r') as file_to_read:
#     print(str(file_to_read.read()))
#____________________________________________________________________________________________#
with open('C:/Users/Liudmila/Desktop/Luda/Portnov/session 11-12.txt', 'r') as file_to_practice:
    print(str(file_to_practice.read()))

