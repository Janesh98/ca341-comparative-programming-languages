class Task():

    def __init__(self, title, date, start_time, duration, people):
        # super().__init__(title, date, start_time)
        self.title = title
        self.date = date
        self.start_time = start_time
        self.duration = duration
        self.people = people

    def __str__(self):
        return "\nTitle : {}\nDate : {}\nTime : {}\nDuration : {}\nPeople : {}\n".format(
            self.title, self.date, self.start_time, self.duration, self.people)