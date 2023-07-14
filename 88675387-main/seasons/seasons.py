
from datetime import date
import sys
import inflect
def main():
    convert_inp = convertinp(input("Date of Birth: "))
    if isinstance(convert_inp, date):
        delta_minutes = minutecalculat(convert_inp)
        inflector = inflect.engine()
        print(f"{inflector.number_to_words(delta_minutes, andword='').capitalize()} minutes")
    else:
        print("Invalid date")
        sys.exit(1)


def convertinp(user_input):
    try:
        modifieinp = list(map(int, user_input.split("-")))
        return date(modifieinp[0], modifieinp[1], modifieinp[2])
    except ValueError:
        return None


def minutecalculat(converteinp):
    delta_days = date.today() - converteinp
    return int(delta_days.total_seconds() / 60)


if __name__ == "__main__":
    main()