# Symulator Harmonogramowania Round Robin

Ten projekt implementuje symulator harmonogramowania Round Robin. Algorytm Round Robin jest algorytmem szeregowania procesów w systemach operacyjnych, który przydziela każdemu procesowi stałą jednostkę czasu (kwant czasu), a następnie przełącza procesor do następnego procesu w kolejce. Jeśli proces nie zakończy się w przydzielonym mu czasie, jest on umieszczany z powrotem na końcu kolejki.

## Opis kodu

Kod składa się z dwóch głównych klas: `Task` i `RoundRobinScheduler`.

### Klasa `Task`

Klasa `Task` reprezentuje pojedyncze zadanie. Posiada następujące atrybuty:

*   `name`: Nazwa zadania (ciąg znaków).
*   `duration`: Początkowy czas trwania zadania (liczba).
*   `remaining_time`: Pozostały czas do zakończenia zadania (liczba).

Metoda `__repr__` zwraca reprezentację tekstową obiektu `Task`.

### Klasa `RoundRobinScheduler`

Klasa `RoundRobinScheduler` implementuje algorytm harmonogramowania Round Robin. Posiada następujące atrybuty:

*   `time_quantum`: Kwota czasu, jaką każde zadanie może spędzić na procesorze (liczba).
*   `queue`: Kolejka zadań do wykonania (kolejka `deque` z modułu `collections`).

Posiada również następujące metody:

*   `add_task(task)`: Dodaje zadanie do kolejki.
*   `run()`: Uruchamia harmonogramowanie. Metoda ta iteruje po kolejce zadań, przydzielając każdemu zadaniu kwant czasu. Jeśli zadanie nie zakończy się w tym czasie, jest ono umieszczane z powrotem na końcu kolejki. Po zakończeniu wszystkich zadań, metoda wypisuje całkowity czas wykonania.

## Użycie

Aby użyć symulatora, należy:

1.  Utworzyć obiekty `Task`, podając nazwę i czas trwania każdego zadania.
2.  Utworzyć obiekt `RoundRobinScheduler`, podając kwotę czasu.
3.  Dodać zadania do harmonogramu za pomocą metody `add_task`.
4.  Uruchomić harmonogramowanie za pomocą metody `run`.

## Przykład użycia

```python
from collections import deque

class Task:
    # ... (kod klasy Task)

class RoundRobinScheduler:
    # ... (kod klasy RoundRobinScheduler)

# Przykładowe zadania
tasks = [
    Task("Task1", 10),
    Task("Task2", 5),
    Task("Task3", 8),
    Task("Task4", 3)
]

# Tworzymy harmonogram Round-Robin z kwotą czasu 4
scheduler = RoundRobinScheduler(time_quantum=4)

# Dodajemy zadania do harmonogramu
for task in tasks:
    scheduler.add_task(task)

# Uruchamiamy harmonogramowanie
scheduler.run()
