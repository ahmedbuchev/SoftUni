path = input().split("\\")

file_with_extension = path[-1]

file_name, file_extension = file_with_extension.split(".")

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
