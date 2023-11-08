import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # If matching no minute format
    if matches := re.search(r"^(\d+) (AM|PM) to (\d+) (AM|PM)$", s, re.IGNORECASE):

        start_hour = matches.group(1)
        end_hour = matches.group(3)

        start_daytime = matches.group(2)
        end_daytime = matches.group(4)

        # Parsing start hour
        # If AM
        if start_daytime == 'AM':
            if start_hour == '12':
                start_hour = 0
            else:
                start_hour = int(start_hour)
        # If PM
        elif start_daytime == 'PM':
            if start_hour == '12':
                start_hour = int(start_hour)
            else:
                start_hour = int(start_hour) + 12

        # Parsing ending hour
        # If AM
        if end_daytime == 'AM':
            if end_hour == '12':
                end_hour = 0
            else:
                end_hour = int(end_hour)

        # If PM
        elif end_daytime == 'PM':
            if end_hour == '12':
                end_hour = int(end_hour)
            else:
                end_hour = int(end_hour) + 12

        return f"{start_hour:02d}:00 to {end_hour:02d}:00"


    # If matching minute format
    elif matches := re.search(r"^(\d+):?(\d+)? (AM|PM) to (\d+):?(\d+)? (AM|PM)$", s, re.IGNORECASE):

        start_hour = matches.group(1)
        end_hour = matches.group(4)
        start_minutes = int(matches.group(2) or '0') # If end minutes in input while start minutes empty
        end_minutes = int(matches.group(5) or '0') # If start minutes in input while end minutes empty

        # Check correct minutes
        range_list = list(range(60))

        if start_minutes not in range_list or end_minutes not in range_list:
            raise ValueError

        start_daytime = matches.group(3)
        end_daytime = matches.group(6)

        # Parsing start hour
        # If AM
        if start_daytime == 'AM':
            if start_hour == '12':
                start_hour = 0
            else:
                start_hour = int(start_hour)
        # If PM
        elif start_daytime == 'PM':
            if start_hour == '12':
                start_hour = int(start_hour)
            else:
                start_hour = int(start_hour) + 12

        # Parsing ending hour
        # If AM
        if end_daytime == 'AM':
            if end_hour == '12':
                end_hour = 0
            else:
                end_hour = int(end_hour)

        # If PM
        elif end_daytime == 'PM':
            if end_hour == '12':
                end_hour = int(end_hour)
            else:
                end_hour = int(end_hour) + 12

        return f"{start_hour:02d}:{start_minutes:02d} to {end_hour:02d}:{end_minutes:02d}"

    else:
        raise ValueError



if __name__ == "__main__":
    main()