readme_file = open('README.md', 'r')  # r = read / w = write / a = append / r+ = read and write
print(readme_file.readline())
print(readme_file.readline())
readme_file.close()