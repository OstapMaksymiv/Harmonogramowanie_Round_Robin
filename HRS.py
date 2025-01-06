from collections import deque

class Task:
    def __init__(self, name, duration):
        self.name = name  
        self.duration = duration  
        self.remaining_time = duration  

    def __repr__(self):
        return f"Task({self.name}, {self.remaining_time})"
class RoundRobinScheduler:
    def __init__(self, time_quantum):
        self.time_quantum = time_quantum  
        self.queue = deque()
    def add_task(self, task):
        self.queue.append(task)
    def run(self):
        time_elapsed = 0  
        while self.queue:
            task = self.queue.popleft()  
            if task.remaining_time > self.time_quantum:
                print(f"Task {task.name} is running for {self.time_quantum} time units.")
                task.remaining_time -= self.time_quantum
                time_elapsed += self.time_quantum
                self.queue.append(task)  
            else:
                print(f"Task {task.name} is finished after running for {task.remaining_time} time units.")
                time_elapsed += task.remaining_time
                task.remaining_time = 0 
        print(f"All tasks completed in {time_elapsed} time units.")

tasks = [
    Task("Task1", 10),
    Task("Task2", 5),
    Task("Task3", 8),
    Task("Task4", 3)
]

scheduler = RoundRobinScheduler(time_quantum=4)

for task in tasks:
    scheduler.add_task(task)

scheduler.run()
