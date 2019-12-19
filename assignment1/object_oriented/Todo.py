from Queue import Queue
from threading import Thread
from Event import Event
from Task import Task

class Todo:

    def __init__(self):
        self.queue = Queue()
        self.quit == False
        self.cmds_allowed = ["task", "event", "quit", "remove", "view"]

    def start(self):
        # initiates todo loop
        while self.quit != True:
            threads = []
            print("Enter Task or Event   |   quit, remove and view commands are also available")
            cmd = input().strip().lower()

            if cmd in self.cmds_allowed:
                # getattr() is dangerous due to possibility of calling functions
                # the user is not meant to be able to so only allow it to search
                # for functions in the allowed commands

                myfunc = getattr(self, cmd) # find the function in this class

                t = Thread(target=myfunc) # create a thread to execute the given
                threads.append(t)         # function and append to threads list

                self.handle_threading(threads)

            else:
                print("{} is not a valid command\n".format(cmd))

    def handle_threading(self, threads):
        # function to handle the starting and ending of threads
        for t in threads:
            # starts each thread
            t.start()

        for t in threads:
            # waits for the threads to finish, also ensures stdout
            # is not used at the same time causing text to be jumbled together.
            t.join()

    def get_details(self, todo_type):
        # all input is not formatted apart from removing trailing whitespace
        # to allow the user to define how info is presented as it is only them
        # that needs to understand it
        print("\nEnter " + todo_type + " title")
        title = input().strip()
        print("\nEnter " + todo_type + " date")
        date = input().strip()
        print("\nEnter " + todo_type + " start time")
        time = input().strip()

        return title, date, time

    def task(self):
        title, date, time = self.get_details("task")
        print("\nEnter task duration")
        duration = input().strip()
        print("\nEnter people assigned to the task separated by a comma \",\"")
        people = input().strip()

        task = Task(title, date, time, duration, people)
        self.add(task)

    def event(self):
        title, date, time = self.get_details("event")
        print("\nEnter event location")
        location = input().strip()

        event = Event(title, date, time, location)
        self.add(event)

    def view(self):
        q = self.queue
        if q.empty():
            print("\nNo reminders available to view\n")
        else:
            while not q.empty():
                print(q.get())

    def quit(self):
        self.quit = True

    def add(self, reminder):
        self.queue.put(reminder)

    def remove(self):
        if not self.queue.empty():
            reminder = self.queue.get()
            print("{}\nReminder above has been removed\n".format(reminder))
        else:
            print("\nNo reminders available to remove\n")

    def __str__(self):
        return self.queue.get()

def main():
    Todo().start()

if __name__ == '__main__':
    main()