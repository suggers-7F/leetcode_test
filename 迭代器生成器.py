



# 现在有一个需求，求一段文字中，每个单词出现的位置。
def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text, 1):
        if letter == ' ':
            yield index


def index_words_1(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text, 1):
        print(index,letter)
        if letter == ' ':
            result.append(index)
    return result


text = "asdfasdf asdfafds ,asdf a,asd ,asdf "
for i in index_words(text):
    print(i)
print(index_words_1(""))



# 斐波拉契
def fib(num):
    a,b,c = 0,1,0
    while c<num:
        yield b
        a,b = b,a+b
        c+=1

for i in fib(10):
    print(i)
