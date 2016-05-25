# Full-Stack-Web-Developer-Nanodegree
This is project repository for [Full Stack Nano degree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) in [Udacity](https://www.udacity.com/)

### What's included
- [Project. Korean Movie Trailer Website]()
- Project. Portfolio Site (not yet)
- Project. Multi User Blog (not yet)
- Project. Tournament Results (not yet)
- Project. Item Catalog (not yet)
- Project. Neighborhood Map (not yet)
- Project. Design a Game (not yet)
- Project. Linux Server Configuration (not yet)

---
####Project. Korean Moive Trailer Website
: This is simple website that shows Korean movie trailer that I like. You can see a moive poster. If you click it, you can also watch a pop-up movie trailer(Youtube) with english subtitle.
```
MovieTrailerWebsite/
├── entertainment_center.py 
├── fresh_tomatoes.html
├── fresh_tomatoes.py
├── media.py
```
#####How to use
- 1. import module and make a movie instance


ex)
```python
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

```
- 2. make a moive list that you want to put in website
```python
movies = [the_wailing, inside_Men, ... ]
```
- 3. use 'open_movies_page' method and get a html file which contain moive information you add
```python
fresh_tomatoes.open_movies_page(movies)
```
after run above instruction, You can find a new html file, fresh_tomatoes.html
