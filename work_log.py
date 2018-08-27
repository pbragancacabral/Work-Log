import os


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
    task = input("Title of the task: ")
    time = input("Time spent in (minutes): ")
    notes = input("Notes (optional): ")
    return date, task, time, notes


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
    while True:
        choice = show_main_menu()
        if choice == "1":
            entry = show_entry_menu()
            # save entry
            clear_screen()
            input("Entry added - please press <RETURN> to return to the main menu.")
            show_main_menu()
        elif choice == "2":
            choice = show_entries_menu()
            if choice == "5":
                show_main_menu()
        elif choice == "3":
            print("Quitting...")
        exit()
    else:
        print("Error: please select a number from the menu.")
        print()


if __name__ == "__main__":
    run()
