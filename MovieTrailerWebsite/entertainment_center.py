import fresh_tomatoes
import media

the_wailing = media.Movie("The Wailing",
                          ("A stranger arrives in a little village and soon af"
                           "ter a mysterious sickness starts spreading. A poli"
                           "ce man is drawn into the incident and is forced to"
                           " solve the mystery in order to save his daughter"),
                          ("http://movie.phinf.naver.net/20160425_165/14615601"
                           "65179gYQ0g_JPEG/movie_image.jpg"),
                          "https://www.youtube.com/watch?v=43uAputjI4k")

inside_Men = media.Movie("Inside Men",
                         ("A former political henchman seeks out revenge for b"
                          "eing dropped by a ruthless politician while a deter"
                          "mined investigator tries to proof a connection betw"
                          "een them."),
                         ("http://movie.phinf.naver.net/20151217_11/1450315249"
                          "365tMoQD_JPEG/movie_image.jpg"),
                         "https://www.youtube.com/watch?v=UP38GHwWg8I")

the_terror_live = media.Movie("The Terror Live",
                              ("Young-Hwa Yoon, once a top national news ancho"
                               "r wants to get his title back through an exclu"
                               "sive live broadcast with a terrorist"),
                              ("https://attachment.namuwikiusercontent.com/the"
                               "terrorlive.jpg"),
                              "https://www.youtube.com/watch?v=aRFz4Toqz2o")

movies = [the_wailing, inside_Men, the_terror_live]
fresh_tomatoes.open_movies_page(movies)
