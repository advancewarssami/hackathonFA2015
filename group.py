class group(object):


    def __init__(self, name):
        self.alltimes = []
        for day in range(0, 7):
            for hour in range(0, 24):
                self.alltimes.append(time(day, hour, 0))
                self.alltimes.append(time(day, hour, 30))
        self.name = name
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        user.set_group(self)

    def get_user(self):
        return self.users

    def get_available_times(self):
        badtimes = []
        for user in self.users:
            for timerange in user.times:
                for time in timerange.times:
                    badtimes.append(time)
        return time.get_good_times(self.alltimes, badtimes)

    def __repr__(self):
        string = ""
        string += self.name
        string += ": "
        string += str(self.users)
        return string


class user(object):

    def __init__(self, name):
        self.name = name
        self.group = None
        self.times = []

    def add_bad_time(self, starttime, endtime):
        self.times.append(timeRange(self.group.alltimes, starttime, endtime))

    def get_bad_times(self):
        return self.times

    def set_group(self, group):
        self.group = group

    def __repr__(self):
        string = ""
        string += self.name
        string += "'s bad times are: "
        for time in self.times:
            string += str(time)
        return string


class time(object):
    def __init__(self, day, hour, minute):  #day sunday = 0, monday = 1, tuesday = 2, ...  saturday = 6
        self.day = day
        self.hour = hour
        self.minute = minute

    @staticmethod
    def get_good_times(alltimes, badtimes):
        goodtimes = []
        for time in alltimes:
            if time in badtimes:
                pass
            else:
                goodtimes.append(time)
        return goodtimes

    @staticmethod
    def get_intermediate_times(alltimes, starttime, endtime):
        add = False
        intermediatetimes = []
        for time in alltimes:
            if add:
                if time == endtime:
                    add = False
                else:
                    intermediatetimes.append(time)
            elif time == starttime:
                add = True
        return intermediatetimes

    def __repr__(self):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        string = ""
        string += days[self.day]
        string += " at "
        string += str(self.hour)
        string += ":"
        if self.minute == 30:
            string += "30"
        else:
            string += "00"
        return string

    def __eq__(self, other):
        if self.day == other.day:
            if self.hour == other.hour:
                if self.minute == other.minute:
                    return True
        return False

class timeRange(object):

    def __init__(self, alltimes, starttime, endtime):
        self.times = []
        self.times.append(starttime)
        for t in time.get_intermediate_times(alltimes, starttime, endtime):
            self.times.append(t)
        self.times.append(endtime)

    def __repr__(self):
        string = ""
        for time in self.times:
            string += str(time)
            string += " "
        return string