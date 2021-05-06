import re


def time_to_seconds(time):
    return sum([int(value) * (60 ** i) for i, value in enumerate(reversed(time.split(":")))])


REG_PHRASE = r".* - - \[01/Jul/1995:(\d{2}:\d{2}:\d{2}) -.*] .*/missions/.*"
START_TIME = time_to_seconds("00:59:00")
END_TIME = time_to_seconds("13:27:00")


def main():
    everything_found = []
    with open("access_log_Jul95", 'r') as a:
        for line in a.readlines():
            out = re.match(REG_PHRASE, line)
            if out:
                if START_TIME <= time_to_seconds(out.groups()[0]) <= END_TIME:
                    everything_found.append(line)

    print(everything_found)


if __name__ == '__main__':
    main()
