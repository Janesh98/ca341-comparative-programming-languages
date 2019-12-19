from object_oriented.Queue import Queue
queue = Queue()

alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def __len__(l):
    length = 0
    for i in l:
        length += 1
    return length

def lower(s):
    for char in range(len(s)):
        for letter in range(len(alphabet_upper)):
            if s[char] == alphabet_upper[letter]:
                s = s[:char] + alphabet_lower[letter] + s[char+1:]
    return s

def strip(s):
    # go backwards through string, more efficient
    if s:
        i = len(s) - 1
        while s[i] == ' ':
            s = s[:i]
            i-=1
    return s

def main():
    while True:
        todo_type = ""
        while True:
            print("Enter Task or Event   |   quit, remove and view commands are also available")
            todo_type = lower(strip(input()))
            if todo_type in ["task", "event", "quit", "remove", "view"]:
                break
        if todo_type == "quit":
            break
        elif todo_type == "remove":
            if not queue.empty():
                reminder = queue.get()
                print(reminder + "\nReminder above has been removed\n")
            else:
                print("\nNo reminders available to remove\n")
        elif todo_type == "view":
            if queue.empty():
                print("\nNo reminders available to view\n")
            else:
                while not queue.empty():
                    print(queue.get())
        else:
            print("\nEnter " + todo_type + " title")
            title = input()
            print("\nEnter " + todo_type + " date")
            date = input()
            print("\nEnter " + todo_type + " start time")
            time = input()
            if todo_type == "task":
                print("\nEnter task duration")
                duration = input()
                print("\nEnter people assigned to the task separated by a comma \",\"")
                people = input()
                output = "\nTitle : " + title + "\nDate : " + date + "\nTime : " + time + "\nDuration : " + duration + "\nPeople : " + people + "\n"
                queue.put(output)
            else:
                print("\nEnter event location")
                location = input()
                output = "\nTitle : " + title + "\nDate : " + date + "\nTime : " + time + "\nLocation : " + location + "\n"
                queue.put(output)


if __name__ == '__main__':
    main()