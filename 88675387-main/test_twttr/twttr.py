def main():
    user_input = input("Input: ")
    user_input_short = shorten(user_input)
    print(user_input_short)


def shorten(word):
    output = ""
    for letter in word:
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            output += letter
    return output


if __name__ == "__main__":
    main() 