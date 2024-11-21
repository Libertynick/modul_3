calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(slovo):
    count_calls()
    return ((len(slovo), slovo.upper(), slovo.lower()))

def is_contains(slovo, spisok):
    count_calls()
    spisok_UP = [i.upper() for i in spisok]
    return (slovo.upper() in spisok_UP)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)