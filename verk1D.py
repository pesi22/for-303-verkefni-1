def ruglingur(word):
    fylki = []
    for i in range(len(word)):
        if i % 2 == 0 and i < len(word)-1:
            if word[i+1]:
                a = word[i]+word[i+1]
                fylki.append(a)
    if len(word) % 2 != 0:
        fylki.append(word[-1:])
    x = ""
    for i in fylki:
        x = x+ i[::-1]
    print(x.upper())

word = input("type your word: ")
ruglingur(word)