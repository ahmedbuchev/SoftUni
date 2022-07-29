import re

pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

num = int(input())

for _ in range(num):
    barcode = input()
    result = re.findall(pattern, barcode)
    product_group = ""
    if result:
        for i in range(len(barcode)):
            if barcode[i].isdigit():
                product_group += barcode[i]
        if product_group:
            print(f"Product group: {product_group}")
        else:
            product_group = "00"
            print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")



