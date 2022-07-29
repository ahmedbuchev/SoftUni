import re

text = input()
pattern = r"www\.[A-Za-z0-9-]+(\.[a-z]+)+"
sites = []
while text:
    valid_sites = [el.group() for el in re.finditer(pattern, text)]
    if valid_sites:
        sites.extend(valid_sites)
    text = input()

print(*sites, sep="\n")

# Ivan Shopov
# valid_urls = []
# pattern = '((w{3})\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
# sentence = input()
# while sentence:
#     matches = re.finditer(pattern, sentence)
#     for match in matches:
#         valid_urls.append(match.group(1))
#     sentence = input()
# for valid_url in valid_urls:
#     print(valid_url)