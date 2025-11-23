# ------------------------------------------------------------
# Name       : Navya Kumar
# Course     : Programming for Problem Solving using Python
# Roll No.   : 2501410054
# ------------------------------------------------------------

class LibrarySystem:
    def __init__(self, datafile="library.txt"):
        self.datafile = datafile

        # Ensure file exists
        try:
            file = open(self.datafile, "r")
            file.close()
        except:
            file = open(self.datafile, "w")
            file.close()

    def insert_book(self, b_title, b_author, b_isbn):
        file = open(self.datafile, "a")
        file.write(b_title + "," + b_author + "," + b_isbn + ",available\n")
        file.close()
        print("Book successfully added.")

    def give_book(self, book_isbn):
        file = open(self.datafile, "r")
        records = file.readlines()
        file.close()

        updated = []
        exists = False

        for entry in records:
            parts = entry.strip().split(",")

            if parts[2] == book_isbn:
                exists = True
                if parts[3] == "available":
                    parts[3] = "issued"
                    print("Book issued to user.")
                else:
                    print("This book is already issued.")
            updated.append(",".join(parts) + "\n")

        if not exists:
            print("Book with this ISBN not found.")
            return

        file = open(self.datafile, "w")
        file.writelines(updated)
        file.close()

    def receive_book(self, book_isbn):
        file = open(self.datafile, "r")
        records = file.readlines()
        file.close()

        updated = []
        exists = False

        for entry in records:
            parts = entry.strip().split(",")

            if parts[2] == book_isbn:
                exists = True
                if parts[3] == "issued":
                    parts[3] = "available"
                    print("Book returned to library.")
                else:
                    print("Book was already available.")
            updated.append(",".join(parts) + "\n")

        if not exists:
            print("Book with this ISBN not found.")
            return

        file = open(self.datafile, "w")
        file.writelines(updated)
        file.close()

    def find_by_title(self, title_key):
        file = open(self.datafile, "r")
        entries = file.readlines()
        file.close()

        found_any = False

        for entry in entries:
            parts = entry.strip().split(",")
            if title_key.lower() in parts[0].lower():
                print("Title:", parts[0], "| Author:", parts[1], "| ISBN:", parts[2], "| Status:", parts[3])
                found_any = True

        if not found_any:
            print("No book matched your search.")

    def show_all(self):
        file = open(self.datafile, "r")
        entries = file.readlines()
        file.close()

        if not entries:
            print("Library is currently empty.")
            return

        for entry in entries:
            parts = entry.strip().split(",")
            print("Title:", parts[0], "| Author:", parts[1], "| ISBN:", parts[2], "| Status:", parts[3])


def main():
    system = LibrarySystem()

    while True:
        print("\n==== Library Menu ====")
        print("1. Add New Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Display All Books")
        print("5. Search Book by Title")
        print("6. Exit System")

        option = input("Choose an option: ")

        if option == "1":
            t = input("Enter Book Title: ")
            a = input("Enter Author Name: ")
            i = input("Enter ISBN Number: ")
            system.insert_book(t, a, i)

        elif option == "2":
            i = input("Enter ISBN to Issue: ")
            system.give_book(i)

        elif option == "3":
            i = input("Enter ISBN to Return: ")
            system.receive_book(i)

        elif option == "4":
            system.show_all()

        elif option == "5":
            key = input("Enter Title to Search: ")
            system.find_by_title(key)

        elif option == "6":
            print("Closing Library System...")
            break

        else:
            print("Invalid input! Try again.")

main()
