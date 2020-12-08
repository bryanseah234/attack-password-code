import zipfile
import itertools
z = zipfile.ZipFile('filename') #INPUT THE NAME OF YOUR ZIP FILE (MUST BE IN SAME DIRECTORY)

wordlist = []

keywords = [] #INPUT POSSIBLE KEYWORDS YOU HAVE
combinations = itertools.combinations(keywords, 2)
for combination in combinations:
    wordlist.append(combination[0]+combination[1])

with open('1.txt', 'r', encoding="utf8") as f: #INPUT THE NAME OF YOUR WORDLISTS
    words1 = f.readlines()
    for i in words1:
        wordlist.append(i)
with open('2.txt', 'r', encoding="utf8") as f: #INPUT THE NAME OF YOUR WORDLISTS 
    words2 = f.readlines()
    for j in words2:
        wordlist.append(words2)
with open('3.txt', 'r', encoding="utf8") as f: #INPUT THE NAME OF YOUR WORDLISTS
    words3 = f.readlines()
    for k in words3:
        wordlist.append(words3)

# print(wordlist)

tries = 0
for word in wordlist:
    try:
        tries += 1
        print(f'Try number {tries}...')
        word = word.strip("\n")
        z.setpassword(word.encode('ascii'))
        z.extract('This is it.docx') #NAME OF FILE(S) INSIDE ZIP
        print(f'Password is -- {word} -- after {tries}!')
    except:
        pass