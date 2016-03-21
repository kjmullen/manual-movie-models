## Description

You will make working models connected to a backend database using classes and @staticmethods

## Normal Mode

* Create classes (Should be singularly named Movie not Movies) to represent the following table rows:
	* movies
	* ratings
	* tags

* Each class should have all of the fields in the table they represent.

### Movie
* Create a staticmethod that will take an id and return one movie object with that id
* Create a staticmethod that takes a string and returns a list of movie objects that have that string in the title
* Create a staticmethod that takes a year and returns a list of movie objects that are made in that year
* Create a method called save that looks to see if the movie exists in the database.  If it does run an update statement otherwise insert the object data into a new row.

### Ratings
* Create a staticmethod that takes a movie id and a minimum rating count and returns the average rating for the movie
filtering based on on the minimum rating count

### Tags
* Make sure the timestamp field converts the timestamp to something readable instead of a unix timestamp
* Create a staticmethod that takes a movie id and returns a list of tags 

## Hard Mode

### Genre 
* Create a genre class for the genre table

### Movie 
* Create a staticmethod that will return the top 10 movies by rating
* Create a method that returns all related ratings for a given movie object
* Create a method that returns all tags for for a movie object
* Create a staticmethod that will return all genres for a movie 
* Create a method that takes a genre, creates it if needed then links it to a movie through a many to many relationship.
