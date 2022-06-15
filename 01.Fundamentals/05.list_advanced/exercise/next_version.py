current_version = input().split(".")
current_version_as_num = int("".join(current_version))
next_version_as_num = current_version_as_num + 1
next_version = str(next_version_as_num)
print(".".join(next_version))
