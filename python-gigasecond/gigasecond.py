from datetime import datetime, timedelta


def add_gigasecond(year, month, day):
    birthdate = datetime(year=year, month=month, day=day)
    giga = birthdate + timedelta(seconds=10**9)
    return giga
#     print(giga)
#
#
# add_gigasecond(1977, 6, 13)
