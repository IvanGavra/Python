filenames = ["1.doc", "1.report", "1.presentation"]
print(filenames)
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)
