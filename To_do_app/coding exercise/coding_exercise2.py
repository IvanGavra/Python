filenames = ['doc.txt', 'report.txt', 'presentation.txt']
lines = ["hello", "hello", "hello"]

for filename, line in zip(filenames, lines):
    file = open(f'{filename}', 'w')
    file.write(line)
