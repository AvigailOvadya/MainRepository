import json
import argparse


# פונקציה להוספת ארגומנט JSON לקובץ
def append_json(file_name, json_argument):
    try:
        # פרס את ארגומנט ה-JSON
        data = json.loads(json_argument)

        # קריאת הנתונים הקיימים מהקובץ
        try:
            with open(file_name, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        # הוספת הנתונים החדשים
        existing_data.append(data)

        # כתיבת הנתונים המעודכנים בחזרה לקובץ
        with open(file_name, 'w') as file:
            json.dump(existing_data, file)

        print("JSON argument appended successfully.")
    except json.JSONDecodeError:
        print("Invalid JSON argument.")


# פונקציה להחזרת 10 הארגומנטים האחרונים מהקובץ
def get_last_10(file_name):
    try:
        # קריאת הנתונים הקיימים מהקובץ
        with open(file_name, 'r') as file:
            existing_data = json.load(file)

        # קבלת 10 הארגומנטים האחרונים
        last_10 = existing_data[-10:]

        # הדפסת 10 הארגומנטים האחרונים
        print(json.dumps(last_10, indent=2))
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error reading JSON from file.")


def main():
    parser = argparse.ArgumentParser(description="CLI tool for JSON file manipulation")
    subparsers = parser.add_subparsers(dest="command")

    # תת-פרסר לפקודת append
    append_parser = subparsers.add_parser("append", help="Append a JSON argument to the file")
    append_parser.add_argument("file_name", type=str, help="The name of the file")
    append_parser.add_argument("json_argument", type=str, help="The JSON argument to append")

    # תת-פרסר לפקודת get_last_10
    get_last_10_parser = subparsers.add_parser("get_last_10", help="Get the last 10 JSON arguments from the file")
    get_last_10_parser.add_argument("file_name", type=str, help="The name of the file")

    args = parser.parse_args()

    if args.command == "append":
        append_json(args.file_name, args.json_argument)
    elif args.command == "get_last_10":
        get_last_10(args.file_name)
    else:
        parser.print_help()

    # data = {"name": "Avigail", "age": 20, "id": "326547965"}
    # json_argument = json.dumps(data)
    # print(json_argument)


if __name__ == "__main__":
    main()
