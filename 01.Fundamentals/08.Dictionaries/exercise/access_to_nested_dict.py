result = {"Ahmed": {"male": 24}, "asdf":{"woman": 33}}
for key, value in result.items():
    for k, v in value.items():
        print(k, v)
