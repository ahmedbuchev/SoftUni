text = input()

emotions = []

for index in range(len(text)):
    if text[index] == ":":
        emotions.append(text[index] + text[index + 1])

for emo in emotions:
    print(emo)
