class Event():

    def __init__(self, title, date, start_time, location):
        # super().__init__(title, date, start_time)
        self.title = title
        self.date = date
        self.start_time = start_time
        self.location = location

    def __str__(self):
        return "\nTitle : {}\nDate : {}\nTime : {}\nLocation : {}\n".format(
            self.title, self.date, self.start_time, self.location)