class User:

    def __init__(self, happy, sad, tired, alert, timestamp):
        self.happy = happy
        self.sad = sad
        self.tired = tired
        self.alert = alert
        self.timestamp = timestamp

    @property
    def moodavg(self):
        return self.happy - self.sad

    @property
    def awakeavg(self):
        return self.alert - self.tired

    def __repr__(self):
        return "User({}, {}, {}, {}, '{}')".format(self.happy, self.sad, self.tired, self.alert, self.timestamp)