def string_match(regex, string):
    if not regex:
        return True
    if not string or regex[0] not in ['.', string[0]]:
        return False
    return string_match(regex[1:], string[1:])


regex, string = input().split('|')
print(string_match(regex, string))