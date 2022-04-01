import os
import re
import sys


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


def check_s7(string):
    if re.search(r'(def|class) {2,}', string):
        return False
    return True


def check_s8(string):
    if 'class' in string:
        if not bool(re.match(r'class +[A-Z][a-z]+([A-Z][a-z]+)?(\([A-Z][a-z]+[A-Z][a-z]+\))?:', string)):
            return False
    return True


def check_s9(string):
    if 'def' in string:
        if not bool(re.search(r'def +[a-z_0-9]+\(\):', string)):
            return False
    return True


def parse_file(path):
    with open(path) as file:
        counter = 0
        counter_empty_line = 0

        lines = file.readlines()
        for line in lines:
            counter += 1
            line_without_new_line = line.rstrip('\n')

            if not check_s1(line_without_new_line):
                print(f'{path}: Line {counter}: S001 Too long')
            if not check_s2(line_without_new_line):
                print(f'{path}: Line {counter}: S002 Wrong indentation')
            if not check_s3(line_without_new_line):
                print(f'{path}: Line {counter}: S003 Unnecessary semicolon')
            if not check_s4(line_without_new_line):
                print(f'{path}: Line {counter}: S004 At least two spaces required before inline comments')
            if not check_s5(line_without_new_line):
                print(f'{path}: Line {counter}: S005 TODO found')
            if not check_s6(line_without_new_line, counter_empty_line):
                print(f'{path}: Line {counter}: S006 More than two blank lines')
            if not check_s7(line_without_new_line):
                print(f"{path}: Line {counter}: S007 Too many spaces after 'class'")
            if not check_s8(line_without_new_line):
                print(f"{path}: Line {counter}: S008 Class name 'user' should use CamelCase")
            if not check_s9(line_without_new_line):
                print(f"{path}: Line {counter}: S009 Function name 'Print2' should use snake_case")
            if not line_without_new_line:
                counter_empty_line += 1
            else:
                counter_empty_line = 0


def main():
    args = sys.argv
    argument = args[1]
    if argument.endswith('.py'):
        parse_file(argument)
    else:
        list_files = sorted(os.listdir(argument))
        for file_name in list_files:
            if file_name.endswith('.py'):
                parse_file(argument + '/' + file_name)


if __name__ == '__main__':
    main()
