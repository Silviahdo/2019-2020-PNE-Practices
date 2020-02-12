from pathlib import Path

FILENAME = "RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()
file = file_contents.split('\n')
body = "".join(file[1:])

print("Body of the U5.txt file:")
print(body)