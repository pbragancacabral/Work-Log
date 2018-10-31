import csv
import datetime
import os

from task import Task

FILE = "log.csv"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_main_menu():
    clear_screen()
    print("Work Log")
    print()
    print("What would you like to do?")
    print("1. Add new entry")
    print("2. Search in existing entries")
    print("3. Quit program")
    return input("> ")


def show_entry_menu():
    clear_screen()
    date = input("Date of the task (DD/MM/YYYY): ")
    title = input("Title of the task: ")
    time = input("Time spent in (minutes): ")
    notes = input("Notes (optional): ")
    fmt = "%d/%m/%Y"
    date = datetime.datetime.strptime(date, fmt).date()
    return Task(date, title, time, notes)


def show_entries_menu():
    clear_screen()
    print("1. Find by date")
    print("2. Find by time spent")
    print("3. Find by exact search")
    print("4. Find by pattern")
    print("5. Return to the main menu")
    print()
    return input("Please select an option: ")


def run():
    choice = show_main_menu()
    if choice == "1":
        entry = show_entry_menu()
        with open(FILE, "a") as csvfile:
            fieldnames = ["date", "title", "minutes", "notes"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerow({
                "date": entry.date,
                "title": entry.title,
                "minutes": entry.minutes,
                "notes": entry.notes
            })
        input("Entry added - please press <RETURN> to return to the main menu.")
        show_main_menu()
    elif choice == "2":
        choice = show_entries_menu()
        if choice == "1":
            date_to_search = input("Enter the date to search with format dd/mm/yyyy: ")
            day, month, year = date_to_search.split("/")
            fmt_date_to_search = f"{year}-{month}-{day}"
            with open(FILE, newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                rows = list(reader)
                for row in rows[1:]:
                    if row["date"] == fmt_date_to_search:
                        print(row)

        if choice == "5":
            show_main_menu()
    elif choice == "3":
        print("Quitting...")
        exit()
    else:
        input("\nPlease select a number from the menu.\nPress <enter> to continue.")
        run()


if __name__ == "__main__":
    run()
