import string
with open("Text.txt",'r') as file:
    r=file.read()
lword=r.lower()
translator = str.maketrans('', '', string.punctuation)
word = lword.translate(translator)
w=word.split()
word_count={}
for _ in w:
    if _ in word_count:
        word_count[_]+=1
    else:
        word_count[_]=1
s_word=sorted(word_count.keys())
for _ in s_word:
    print(f"{_}:{word_count[_]}")