from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)
    language = [ruby, python, visual_basic]
    print("Dynamically typed languages: ")
    for i in language:
        if i.is_dynamic():
            print(i.name)


main()
