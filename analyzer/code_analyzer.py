def analyse_line(line_number: int, text_line: str):
    if len(text_line) > 79:
        print(f'Line {line_number}: S001 Too Long')


def main():
    path = input()
    content = ''
    with open(path, 'r') as file:
        counter = 0
        while True:
            counter += 1
            line = file.readline()
            analyse_line(counter, line)
            if not line:
                break


if __name__ == '__main__':
    main()
