class Media(object):
    # title = ""
    # poster_image_url = ""
    # trailer_url = ""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.movie_title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer_youtube

    # def toString(self):
    #     print("title : ", self.title, ", poster_image_url: ", self.poster_image_url, ", trailer_url:", self.trailer_url)

    # def __del__(self):
    #     class_name = self.__class__.__name__
    #     print(class_name, "销毁")


'''
t = Media( "jzl", "d://media/img/", "d://media/movie/1 - Welcome to Stage 3.mp4")
t.toString()

t.title = "test-jzl"
hasattr(t, 'title')
del t.title
setattr(t, 'title', "jzl-test")
print(getattr(t, 'title'))
delattr(t, 'title')
'''
avatar = Media("", "dsadad", "", "")
print(avatar.storyline)
