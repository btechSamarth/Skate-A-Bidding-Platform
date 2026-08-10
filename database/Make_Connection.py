import sqlite3

class MAKE_CONNECTION:

    def __enter__(self):
        self.connection = sqlite3.connect("data.db")
        self.cursor = self.connection.cursor()
        self.connection.execute("PRAGMA foreign_keys = ON")
        return self.cursor

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            self.connection.commit()
        else:
            self.connection.rollback()
            print("Something Bad Happened! Please Try Again Later")
        self.connection.close()