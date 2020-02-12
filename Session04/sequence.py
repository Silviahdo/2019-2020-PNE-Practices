from pathlib import Path

FILENAME = "ADA.txt"

file_contents = Path(FILENAME).read_text()
file = file_contents.split('\n')
body = "".join(file[1:])

print("The total number of bases is: ")
print(len(body))
