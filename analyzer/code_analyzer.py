import re


def is_there_comment(string):
    if '#' in string:
        return True
    return False


def check_s1(string):
    if len(string) > 78:
        return False
    return True


def check_s2(string):
    if string and string[0] == " ":
        if not string:
            return False
        counter = 0
        for char in string:
            if char == ' ':
                counter += 1
            else:
                break
        return counter % 4 == 0
    return True


def check_s3(string):
    if string:
        if not is_there_comment(string) and string.strip()[-1] == ';':
            return False
        if is_there_comment(string) and string.index('#') > 0:
            code, comment = string.split('#', 1)
            code = code.strip()
            if code[-1] == ';':
                return False
    return True


def check_s4(string):
    if string and is_there_comment(string):
        first_sharp_position = string.index('#')
        if first_sharp_position != 0:
            code, comment = string.split('#', 1)
            if code[-1] != ' ' or code[-2] != ' ':
                return False
    return True


def check_s5(string):
    if string and is_there_comment(string):
        code, comment = string.split('#', 1)
        if re.search('todo', comment, re.I):
            return False
    return True


def check_s6(string, counter_empty_line):
    if string:
        if counter_empty_line > 2:
            return False
    return True


def main():
    path = input()

    with open(path) as file:
        counter = 0
        counter_empty_line = 0

        lines = file.readlines()
        for line in lines:
            counter += 1
            line_without_new_line = line.rstrip('\n')

            if not check_s1(line_without_new_line):
                print(f'Line {counter}: S001 Too long')
            if not check_s2(line_without_new_line):
                print(f'Line {counter}: S002 Wrong indentation')
            if not check_s3(line_without_new_line):
                print(f'Line {counter}: S003 Unnecessary semicolon')
            if not check_s4(line_without_new_line):
                print(f'Line {counter}: S004 At least two spaces required before inline comments')
            if not check_s5(line_without_new_line):
                print(f'Line {counter}: S005 TODO found')
            if not check_s6(line_without_new_line, counter_empty_line):
                counter_empty_line = 0
                print(f'Line {counter}: S006 More than two blank lines')

            if not line_without_new_line:
                counter_empty_line += 1


if __name__ == '__main__':
    main()
