words = list([word.lower().split() for word in open("words.txt")][0])

words_count = {}

file = open("text.txt", "w")

line = input()
while line:
    file.write(f"{line.lower()}\n")
    line = input()

file.close()

text = list([word for word in open("text.txt", "r")])

for word in words:

    alts = [f'{word}.', f'{word},', f'-{word}', f'-{word},', f'-{word}.']

    for sentence in text:

        if word in sentence.split() or alts[0] in sentence.split() or alts[1] in sentence.split() or alts[2] in \
                sentence.split() or alts[3] in sentence.split() or alts[4] in sentence.split():

            if word not in words_count:

                words_count[word] = sentence.split().count(word) + sentence.count(alts[0]) + \
                                    sentence.count(alts[1]) + sentence.count(alts[2]) + sentence.count(alts[3]) + \
                                    sentence.count(alts[4])
                continue
            words_count[word] += sentence.split().count(word) + sentence.count(alts[0]) + \
                                 sentence.count(alts[1]) + sentence.count(alts[4])

sorted_result = sorted(words_count.items(), key=lambda x: -x[1])

result = open("result.txt", "w")

for word, count in sorted_result:
    result.write(f"{word} - {count}\n")

result.close()

show_result = list([word for word in open("result.txt", "r")])

print(''.join(show_result))