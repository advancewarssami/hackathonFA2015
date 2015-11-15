import pickle

class Group(object):

    def __init__(self, name):
        self.all_times = []
        for day in range(0, 7):
            for hour in range(0, 24):
                self.all_times.append(Time(day, hour, 0))
                self.all_times.append(Time(day, hour, 30))
        self.name = name
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        user.set_group(self)

    def get_user(self):
        return self.users

    def get_available_times(self):
        bad_times = []
        for user in self.users:
            for timerange in user.times:
                for time in timerange.times:
                    bad_times.append(time)
        return Time.get_good_times(self.all_times, bad_times)

    def save(self):
        save_dict = {'name': self.name, 'users': self.users}
        return str(pickle.dumps(save_dict))

    def load(self, dumps):
        load_dict = pickle.loads(b'%s' %dumps)
        self.name = load_dict['name']
        self.users = load_dict['users']
        return self

    def __repr__(self):
        string = ""
        string += self.name
        string += ": "
        string += str(self.users)
        return string


class User(object):

    def __init__(self, name):
        self.name = name
        self.group = None
        self.times = []

    def add_bad_time(self, start_time, end_time):
        self.times.append(TimeRange(self.group.alltimes, start_time, end_time))

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


class Time(object):
    def __init__(self, day, hour, minute):  # day sunday = 0, monday = 1, tuesday = 2, ...  saturday = 6
        self.day = day
        self.hour = hour
        self.minute = minute

    @staticmethod
    def get_good_times(all_times, bad_times):
        goodtimes = []
        for time in all_times:
            if time in bad_times:
                pass
            else:
                goodtimes.append(time)
        return goodtimes

    @staticmethod
    def get_intermediate_times(all_times, start_time, end_time):
        add = False
        intermediate_times = []
        for time in all_times:
            if add:
                if time == end_time:
                    add = False
                else:
                    intermediate_times.append(time)
            elif time == start_time:
                add = True
        return intermediate_times

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


class TimeRange(object):

    def __init__(self, alltimes, starttime, endtime):
        self.times = []
        self.times.append(starttime)
        for t in Time.get_intermediate_times(alltimes, starttime, endtime):
            self.times.append(t)
        self.times.append(endtime)

    def __repr__(self):
        string = ""
        for time in self.times:
            string += str(time)
            string += " "
        return string
