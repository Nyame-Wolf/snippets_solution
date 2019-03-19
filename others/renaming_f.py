import os

os.chdir('/home/nyame-wolf/snippets_solutions/codewars')

# print(os.getcwd()) to find out if we are in the correct directory
fder = '/home/nyame-wolf/snippets_solutions/codewars'
for f in os.listdir(fder):
    # print(f)
    # print(os.path.splitext(f)) # split file to get a tupel of name and extension

    f_name = os.path.join(fder, f)
    if not os.path.isfile(f_name):
        continue
    oldbase = os.path.splitext(f)
    # print(file_ext)
    name = f_name.replace('.txt', '.py')
    # output =
    print(os.rename(f_name, name))
