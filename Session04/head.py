from pathlib import Path

FILENAME = "RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()
header = file_contents.split('\n')

print("First line of the RNU6_269P.txt file: ")
print(header[0])