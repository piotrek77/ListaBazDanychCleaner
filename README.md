# ListaBazDanychCleaner

Skrypt do czyszczenia pliku konfiguracyjnego `Lista baz danych.xml` (plik konfigurujący bazy danych w systemie enova365) z wpisów nieistniejących baz danych.

## Co robi skrypt

1. Otwiera plik `Lista baz danych.xml` z bieżącego katalogu
2. Dla każdego wpisu `MsSqlDatabase` łączy się z serwerem SQL (Windows Authentication)
3. Sprawdza czy baza danych istnieje
4. Jeśli baza nie istnieje - usuwa wpis z pliku
5. Przed modyfikacją tworzy kopię zapasową z timestampem

## Wymagania

- Python 3
- pyodbc
- ODBC Driver 17 for SQL Server

```bash
pip install pyodbc
```

## Użycie

Umieść plik `Lista baz danych.xml` w tym samym katalogu co skrypt, następnie uruchom:

```bash
python czysc.py
```

Kopia zapasowa zostanie utworzona jako `Lista baz danych.kopia YYYY-MM-DD-HH-MM.xml`.
