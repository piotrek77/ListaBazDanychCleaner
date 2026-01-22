import xml.etree.ElementTree as ET
from datetime import datetime
import shutil
import pyodbc
import os

XML_FILE = "Lista baz danych.xml"


def check_database_exists(server: str, database_name: str) -> bool:
    """Sprawdza czy baza danych istnieje na serwerze MSSQL używając Trusted Connection."""
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE=master;"
        f"Trusted_Connection=yes;"
    )
    try:
        with pyodbc.connect(connection_string, timeout=10) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT 1 FROM sys.databases WHERE name = ?", (database_name,)
            )
            return cursor.fetchone() is not None
    except pyodbc.Error as e:
        print(f"  Błąd połączenia z {server}: {e}")
        return True  # W razie błędu połączenia nie usuwamy wpisu


def main():
    if not os.path.exists(XML_FILE):
        print(f"Plik {XML_FILE} nie istnieje!")
        return

    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    databases_to_remove = []

    for db_element in root.findall("MsSqlDatabase"):
        name = db_element.find("Name").text or ""
        server = db_element.find("Server").text or ""
        database_name = db_element.find("DatabaseName").text or ""

        print(f"Sprawdzam: {name} ({database_name} na {server})...", end=" ")

        if check_database_exists(server, database_name):
            print("OK")
        else:
            print("NIE ISTNIEJE - do usunięcia")
            databases_to_remove.append(db_element)

    if databases_to_remove:
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
        backup_file = f"Lista baz danych.kopia {timestamp}.xml"
        shutil.copy2(XML_FILE, backup_file)
        print(f"\nUtworzono kopię zapasową: {backup_file}")

        for db_element in databases_to_remove:
            name = db_element.find("Name").text
            root.remove(db_element)
            print(f"Usunięto: {name}")

        tree.write(XML_FILE, encoding="utf-8", xml_declaration=True)
        print(f"\nZapisano zmodyfikowany plik. Usunięto {len(databases_to_remove)} wpisów.")
    else:
        print("\nWszystkie bazy danych istnieją. Plik nie został zmodyfikowany.")


if __name__ == "__main__":
    main()
