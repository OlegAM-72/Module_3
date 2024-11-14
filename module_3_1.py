calls = 0 # для суммы обращений
calls_1 = 0
calls_2 = 0
def count_calls():
    calls = calls_1 + calls_2
    return  calls


def string_info(string):
    global calls_1
    calls_1 += 1
    typle_str = len(string),string.upper(),string
    return typle_str


def is_contains(n, m):
    global calls_2
    calls_2 += 1
    m = list(map(str.upper, m))
    if n.upper() in m:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(count_calls())

