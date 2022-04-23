# open(fileName, mode)

# Create File
fileName = input('Give file name')
fileName = f'{fileName}.txt'
file = open(fileName,'x')
print(f'Created file : {fileName}')
file.close()


# Write in file
with open(fileName, 'w') as opened_file:
    for i in range(100):
        opened_file.write(f'Look at this line {i}\n')

# Read From file
countLines = 0
with open(fileName, 'r') as opened_file:
    for line in opened_file:
        countLines += 1
        print(line)
    print(f"Number of Lines in the file > {countLines}")