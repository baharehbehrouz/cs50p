
def main():
    div=0
    while True:
        # div=0
        user_input = input("Fraction: ")
        modified_input = user_input.split("/")

        if modified_input[0].isdigit() and modified_input[1].isdigit():
             try:
                div=convert(modified_input)
                break
             except ZeroDivisionError:
                pass
    print(gauge(div))


def convert(fraction):

    numerator = int(fraction[0])
    denominator = int(fraction[1])

    division = numerator / denominator
    if division <= 1:
       return division
    else:
        main()


def gauge(percentage):

    if percentage > 0.99:
        return  "F"
    elif percentage <= 0.1:
        return "E"
    else:
        return str(int(percentage * 100)) + "%"





if __name__ == "__main__":
    main()