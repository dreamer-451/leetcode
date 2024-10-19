def reformatDate(date):
    month = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }
    if len(date) != 13:
        date = "0" + date
    date_format = f"{date[9:]}-{month[date[5:8]]}-{date[:2]}"
    return date_format


if __name__ == '__main__':
    date = "20th Oct 2052"
    date_format = reformatDate(date)
    print(date_format)