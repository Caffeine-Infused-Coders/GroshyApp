from pathlib import Path
import json


class AbstractDB:
    def __init__(self, db_name: str, db_type: str):
        cwd = Path.cwd()
        db_root = Path.joinpath(cwd, ".dbs")
        self.name = db_name  # Define database name from argument
        self.type = db_type
        self.dir = Path.joinpath(db_root, self.type)
        self.path = Path.joinpath(self.dir, f"{self.name}.json")

        if not db_root.exists():
            Path.mkdir(db_root)
            Path.mkdir(self.dir)
        elif db_root.exists() and not self.dir.exists():
            Path.mkdir(self.dir)

        if self.build_db():  # Build new database
            print(f"{self.name} ready for use")
        else:
            print(f"{self.name} could not be built")
            self.db_remove()

    def build_db(self):

        msg = {self.name: {}}  # Message to print in new database file
        result = False  # Default return value for this method

        try:
            with open(self.path, "x") as db:  # Create database json file and dump message
                json.dump(msg, db, indent=4)
                
            print(f"{self.name} created successfully")
            result = True  # Signal creation of db
        except FileExistsError:
            print(f"A {self.type} named {self.name} already exists in location {self.dir}...")

            ans_flg = False
            attempts = 3
            while ans_flg is False and attempts > 0:
                resp = input("Would you like to choose a different name? (y/n)")

                match resp:
                    case "yes" | "y":
                        ans_flg = True
                        self.name = input("Enter new name: ")
                        result = self.build_db()
                    case "no" | "n":
                        ans_flg = True
                        print(f"{self.type} creation aborted")
                    case _:
                        print("Unexpected input, please try again.")
                        attempts -= 1
                        continue

        return result

    def db_write(self, msg):

        success = False
        try:
            with open(self.path, "w") as db:
                json.dump(msg, db, indent=4)
                db.write("\n")
            success = True
        except FileNotFoundError:
            print(f"No database file found. Double check this location: {self.path}.json")
            pass

        return success

    def db_add(self, msg):

        success = False
        try:
            with open(self.path, "a") as db:
                json.dump(msg, db, indent=4)
                db.write("\n")
            success = True
        except FileNotFoundError:
            print(f"No database file found. Double check this location: {self.path}.json")
            pass

        return success

    def db_read(self):
        contents = False
        try:
            with open(self.path, "r") as db:
                contents = json.load(db)
        except FileNotFoundError:
            print(f"No database file found. Double check this location: {self.path}.json")
            pass

        return contents

    def db_remove(self):
        success = False
        print(f"Removing {self.name} from {self.dir}")
        Path.unlink(self.path)
        if not self.path.exists():
            success = True
            print(f"{self.name} removed...")

        return success

