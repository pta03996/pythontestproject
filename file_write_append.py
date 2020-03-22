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
