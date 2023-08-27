
#  задания №1
def is_palindrome():
    word = input("Введите строку без пробелов: ")
    if word == word[::-1]:
        return "yes"
    else:
        return "no"

print(is_palindrome())




#  задания №2

def compress_spaces():
    text = input("Введите строку, длина которой не превосходит 1000: ")
    return ' '.join(text.split())

print(compress_spaces())
