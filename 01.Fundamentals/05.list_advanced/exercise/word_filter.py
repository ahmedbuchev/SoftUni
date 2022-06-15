words = input().split()
end_list = [word for word in words if len(word) % 2 == 0]
print("\n".join(end_list))
