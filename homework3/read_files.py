with open('referat.txt', 'r', encoding='utf-8') as f:
    numb_of_words = 0
    for line in f:
        print(line)
        words_in_row = len(line.split())
        numb_of_words += words_in_row
    f.seek(0)
    text = f.read()
    print(text)
    
print(f'Всего в тексте {numb_of_words} слов')

text = text.replace('.','!')

with open('referat2.txt', 'w', encoding='utf-8') as ref2:
    ref2.write(text)