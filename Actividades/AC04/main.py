import library as lib


class Video:
    def __init__(self, trending_date, title, publish_date, tags, views, likes,
                 dislikes):
        self.title = title
        self.trending_date = trending_date
        self.publish_date = publish_date
        self.tags = tags
        self.views = views
        self.likes = likes
        self.dislikes = dislikes

    def __str__(self):
        return self.title


def file_reading():
    with open("data_errores.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()[1:]
        video_list = []

        for line in lines:
            data = line.strip().split(",")
            video_list.append(Video(*data))
    return video_list


if __name__ == '__main__':

    videos = file_reading()

    # A partir de este punto, el estudiante debe manejar los errores
    for video in videos:

        days = lib.tiempo_trending(video.publish_date, video.trending_date)
        print("El video {} estuvo trending {} dia(s) despues de publicado"
              .format(video.title, days))

        ratio = lib.like_dislike_ratio(video.likes, video.dislikes)
        print("El video {} tiene aproximadamente {} likes por dislike"
              .format(video.title, ratio))

        lib.info_video(video.title, video.views, video.likes,
                          video.dislikes, video.tags)

        print()
