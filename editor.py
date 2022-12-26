help_text = """plain bold italic header link inline-code new-line
Special commands: !help !done"""

commands = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list", "unordered-list"]

is_response_valid = True


def header(text_, level_):
    return level_ * "#" + " " + text_ + "\n"


def plain_bold_italic(response_, text_):
    if response_ == "plain":
        return text_
    elif response_ == "bold":
        return "**" + text_ + "**"
    elif response_ == "italic":
        return "*" + text_ + "*"


def new_line():
    return "\n"


def link(label_, url_):
    return f"[{label_}]({url_})"


def inline_code(text_):
    return "`" + text_ + "`"


def ordered_list(row_, elements_):
    str_ = ""
    for _ in range(1, row_ + 1):
        str_ += f"{_}. {elements_[_ - 1]}\n"

    return str_


def unordered_list(row_, elements_):
    str_ = ""
    for _ in range(1, row_ + 1):
        str_ += f"\n* {elements_[_ - 1]}"
    return str_


word = ""

while is_response_valid:
    response = input("Choose a formatter: ")
    if response in commands:
        if response == "header":
            level = int(input("Level: "))
            while not 1 <= level <= 6:
                print("The level should be within the range of 1 to 6")
                level = int(input("Level: "))
            text = input("Text: ")
            word += header(text, level)
            print(word)
            continue
        elif response in ["plain", "bold", "italic"]:
            text = input("Text: ")
            word += plain_bold_italic(response, text)
            print(word)
            continue
        elif response == "link":
            label = input("Label: ")
            url = input("URL: ")

            word = link(label, url)
            print(word)
        elif response == "inline-code":
            text = input("Text: ")
            word += inline_code(text)
            print(word)
        elif response == "ordered-list":
            row = int(input("Number of rows: "))
            while row <= 0:
                print("The number of rows should be greater than zero")
                row = int(input("Number of rows: "))
                continue

            elements = []
            for i in range(1, row + 1):
                elements.append(input(f"row #{i}: "))

            word += ordered_list(row, elements)

            print(word)
        elif response == "unordered-list":
            row = int(input("Number of rows: "))
            while row <= 0:
                print("The number of rows should be greater than zero")
                row = int(input("Number of rows:"))
                continue

            elements = []
            for i in range(1, row + 1):
                elements.append(input(f"row #{i}: "))

            word += unordered_list(row, elements)

            print(word)
        elif response == "new-line":
            word += new_line()
            print(word)
        continue
    elif response == "!done":
        with open("output.md", "w") as file:
            file.write(word)
        break
    elif response == "!help":
        print(help_text)
        continue
    else:
        print("Unknown formatting type or command")
        continue
