import webbrowser

#the subclasses Movie and TvShow inherite two attributes from the parent class Video

class Video():
    def __init__(self, title, duration):
        self.tit = title
        self.dur = duration


class Movie(Video):
    def __init__(self, title, duration, storyline, poster_image, youtube_trailer):
        Video.__init__(self, title, duration)
        self.line = storyline
        self.img = poster_image
        self.trailer= youtube_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer)


class TvShow(Video):
    def __init__(self, title, duration, season, episode, tv_station):
        Video.__init__(self, title, duration)
        self.season = season
        self.epi=episode
        self.station=tv_station
    def get_local_listing(self):
        webbrowser.open(self.station)



ygm = Movie("You've Got Mail", "2hr","a love story of two New Yorkers in the 90s", "https://upload.wikimedia.org/wikipedia/en/e/ee/You've_Got_Mail.jpg","https://www.youtube.com/watch?v=znESQTt3L80")

print("The movie is "+ ygm.tit+".")
ygm.show_trailer()
