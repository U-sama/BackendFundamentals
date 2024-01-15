
def read_file_sync(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

print("1")
print(read_file_sync("file.txt"))
print("2")