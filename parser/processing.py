import datetime


def remove_label(text):
    return text.split(": ")[1].strip()


def text2number(text):
    return int(text.replace(",", ""))


def decode_datetime(time):
    time = time.lower()
    if "ago" in time:
        time_ago = time.split(" ")[0]
        time_type = time_ago[-1]
        time_delta = int(time_ago[:-1])
        if time_type == "h":
            return datetime.datetime.now() - datetime.timedelta(hours=time_delta)
        elif time_type == "m":
            return datetime.datetime.now() - datetime.timedelta(minutes=time_delta)
        elif time_type == "s":
            return datetime.datetime.now() - datetime.timedelta(seconds=time_delta)
    else:
        if "," in time:
            date = time.split(", ")[0]
            year = time.split(", ")[1]
        else:
            date = time.strip()
            year = datetime.datetime.now().year

        month_name, date = date.split(" ")

        months = {
            "jan": "01",
            "feb": "02",
            "mar": "03",
            "apr": "04",
            "may": "05",
            "jun": "06",
            "jul": "07",
            "aug": "08",
            "sep": "09",
            "oct": "10",
            "nov": "11",
            "dec": "12",
        }
        month = months[month_name.lower()]
        return datetime.datetime(int(year), int(month), int(date))


def prepare_datetime(time):
    time = decode_datetime(time)
    time = time.strftime("%Y-%m-%d")
    return time


def parse_stats(stats):
    stats_separated = stats.split(" - ")
    data = {
        "rated": "",
        "language": "",
        "genre": "",
        "chapters": "",
        "words": "",
        "reviews": "",
        "favs": "",
        "follows": "",
        "published": "",
        "updated": "",
        "characters": "",
    }
    for i, stat in enumerate(stats_separated):
        if stat.startswith("Rated"):
            data["rated"] = remove_label(stat)
        elif i == 1:
            data["language"] = stat
        elif i == 2 and not stat.startswith("Chapters"):
            data["genre"] = stat
        elif stat.startswith("Chapters"):
            data["chapters"] = text2number(remove_label(stat))
        elif stat.startswith("Words"):
            data["words"] = text2number(remove_label(stat))
        elif stat.startswith("Reviews"):
            data["reviews"] = text2number(remove_label(stat))
        elif stat.startswith("Favs"):
            data["favs"] = text2number(remove_label(stat))
        elif stat.startswith("Follows"):
            data["follows"] = text2number(remove_label(stat))
        elif stat.startswith("Updated"):
            data["updated"] = prepare_datetime(remove_label(stat))
        elif stat.startswith("Published"):
            data["published"] = prepare_datetime(remove_label(stat))
        elif i == len(stats_separated) - 1:
            data["characters"] = stat
    return data
