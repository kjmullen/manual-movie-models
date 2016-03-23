import psycopg2
from psycopg2.extras import DictCursor


class Movie:

    def __init__(self, movieid, title, genres):
        self.movieid = movieid
        self.title = title
        self.genres = genres

    @staticmethod
    def create_movie_from_dict(movie_dict):
        return Movie(movie_dict['movieid'], movie_dict['title'],
                     movie_dict['genres'])

# Create a staticmethod
# that will take an id and
# return one movie object with that id

    @staticmethod
    def get_by_id(cursor, movieid):
        cursor.execute("SELECT * FROM movies WHERE movieid = %s;", (movieid,))
        movie_dict = cursor.fetchone()
        return Movie.create_movie_from_dict(movie_dict)

# Create a staticmethod
# that takes a string
# and returns a list
# of movie objects that
# have that string in the title

    @staticmethod
    def get_by_string(cursor, string):
        title_search = "%{}%".format(string)
        movie_list = []
        cursor.execute("SELECT * FROM movies m WHERE lower(title) like %s;",
                       (title_search,))
        for movie in cursor.fetchall():
            movie_list.append(movie)
        return movie_list

# Create a staticmethod
# that takes a year and
# returns a list of movie objects
# that are made in that year

    @staticmethod
    def get_by_year(cursor, year_entered):
        year_search = "%({})%".format(year_entered)
        movie_by_year_list = []
        cursor.execute\
            ("SELECT m.title FROM movies m WHERE title like %s;",
                       (year_search,))
        for movie in cursor.fetchall():
            movie_by_year_list.append(movie)
        return movie_by_year_list

# Create a method called save
# that looks to see if the
# movie exists in the database.
# If it does run an update statement
# otherwise insert the object data into a new row.

    def save(self, cursor):
        if not self.movieid:
            cursor.execute("INSERT INTO movies (title, genres)"
                           "VALUES (%s, %s);", (self.title, self.genres))
        else:
            cursor.execute("UPDATE movies SET title = %s, genres = %s WHERE movieid = %s;",
                           (self.title, self.genres, self.movieid))

    @staticmethod
    def update_movie_rating(cursor, movie_id, rating):
        movie = Movie.get_by_id(cursor, movie_id)
        if movie:
            cursor.execute("UPDATE movies SET mpaa_rating =%s WHERE movieid = %s;",(rating,movie_id))
            print("Movie rating updated.")
        else:
            cursor.execute("INSERT INTO movies "
                           "(movieid, title, genres, mpaa_rating) "
                           "VALUES(%s, %s, %s, %s);",
                           (movie_id, movie.title, movie.genres, rating))
            print("{} added to database with it's {} rating".format(movie.title, rating))

    def __str__(self):
        return self.title


class Rating:

    def __init__(self, userid, movieid, rating, timestamp, id):
        self.userid = userid
        self.movieid = movieid
        self.rating = rating
        self.timestamp = timestamp
        self.id = id

    @staticmethod
    def create_rating_from_dict(rating_dict):
        return Rating(rating_dict['userid'], rating_dict['movieid'],
                      rating_dict['rating'], rating_dict['timestamp'],
                      rating_dict['id'])

# Create a staticmethod
# that takes a movie id
# and a minimum rating count
# and returns the average rating
# for the movie filtering based
# on on the minimum rating count

    @staticmethod
    def min_ratings_avg(cursor, minimum_ratings, movie_id):
        pass
        cursor.execute("SELECT m.movieid, m.title, avg(r.rating), count(r.rating) FROM movies m JOIN ratings r ON m.movieid = r.movieid GROUP BY m.movieid HAVING count(r.rating) > %s ORDER BY Average DESC LIMIT 1;", (minimum_ratings))


# SELECT m.movieid, m.title, avg(r.rating) as Average, count(r.rating) as Count
# FROM movies m
# JOIN ratings r ON m.movieid = r.movieid
# GROUP BY m.movieid
# HAVING count(r.rating) > 100
# ORDER BY Average DESC
# LIMIT 10;


class Tag:

    def __init__(self, userid, movieid, tag, timestamp, id):
        self.userid = userid
        self.movieid = movieid
        self.tag = tag
        self.timestamp = timestamp
        self.id = id

    @staticmethod
    def create_tag_from_dict(tag_dict):
        return Tag(tag_dict['userid'], tag_dict['movieid'], tag_dict['tag'],
                   tag_dict['timestamp'], tag_dict['id'])

# Make sure the timestamp field
# converts the timestamp to
# something readable instead of
# a unix timestamp

# Create a staticmethod that
# takes a movie id and returns
# a list of tags

if __name__ == '__main__':

    conn = psycopg2.connect(host="localhost", database="movies")

    cur = conn.cursor(cursor_factory=DictCursor)

    my_movie = Movie.get_by_id(cur, 12)

    example_search_string = "akira"

    my_movie_search = Movie.get_by_string(cur, example_search_string)

    print(my_movie_search)

    example_year_search = "1929"

    my_year_search = Movie.get_by_year(cur, example_year_search)

    print(my_year_search)

    akira = Movie.get_by_id(cur, 1274)

    akira.update_movie_rating(cur, 1274, 'R')

    conn.commit()



