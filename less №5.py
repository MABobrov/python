"""Задание 1"""

def describe_number():
    number = int(input("Введите целое число: "))
    if number < 0 and number % 2 == 0:
        return "отрицательное четное число"
    elif number < 0:
        return "отрицательное нечетное число"
    elif number == 0:
        return "нулевое число"
    elif number > 0 and number % 2 == 0:
        return "положительное четное число"
    else: 
        return "положительное нечетное число"

print(describe_number())


"""Задание 2"""

def word_analysis():
    word = input("Введите слово из маленьких латинских букв: ")
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    consonants = 0
    
    for letter in word:
        if letter in vowels:
            vowels[letter] += 1
        else:
            consonants += 1
    
    for vowel in vowels:
        print(f"{vowel}: {vowels[vowel] if vowels[vowel] != 0 else False}")

    print(f"Количество согласных букв: {consonants}")

word_analysis()


"""Задание 3"""

def investment_decision():
    min_investment = int(input("Минимальная сумма инвестиций: "))
    Mike_budget = int(input("Бюджет Майкла: "))
    Ivan_budget = int(input("Бюджет Ивана: "))

    if Mike_budget >= min_investment and Ivan_budget >= min_investment:
        return 2
    elif Mike_budget >= min_investment:
        return "Mike"
    elif Ivan_budget >= min_investment:
        return "Ivan"
    elif Mike_budget + Ivan_budget >= min_investment:
        return 1
    else:
        return 0

print(investment_decision())
