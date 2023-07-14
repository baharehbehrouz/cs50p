from seasons import convertinp, minutecalculat
from datetime import date


def test_seasons():
    assert convertinp("1989-09-11") == date(1989, 9, 11)
    assert minutecalculat(date(1989, 9, 11)) == (date.today() - date(1989, 9, 11)).total_seconds() / 60
    assert convertinp("February 6th, 1998") == None