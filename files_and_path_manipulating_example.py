from pathlib import Path

#  Absolute path = start from the root
# ex. /usr/local/bin
# Relative path = start from this file and go somewhere else

path = Path("example")
email_path = Path("email")
if not email_path:
    email_path.mkdir()
    print("email path has been created")

#search for some file extendsion in the directory
path = Path()
#print(path.glob('*.xls'))
for file in path.glob('*.py'):
    print(file)


readme_file = open('README.md', 'r')  # r = read / w = write / a = append / r+ = read and write
print(readme_file.readline())
print(readme_file.readline())
readme_file.close()

readme_file = open('README.md', 'a')
readme_file.write('\n this is the new line')
readme_file.close()

#override the entire file (will mess up)
# readme_file = open('README.md', 'w')
# readme_file.write('\n this is the new line')
# readme_file.close()


# qriting a new file
newfile_file = open('index.html', 'w')
newfile_file.write('<p>This is a paragraph in HTML</p>')
newfile_file.close()