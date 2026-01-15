-- CREATE TABLE producer(
-- producer_id SERIAL,
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (50) NOT NULL,
-- movie_id integer not null,
-- PRIMARY KEY (producer_id),
-- FOREIGN KEY (movie_id) REFERENCES movie (movie_id)
-- );

-- INSERT into producer (first_name, last_name, movie_id) 
-- values ('Mister', 'Crabs', (SELECT movie_id from movie where movie_title = 'Good Will Hunting') );

SELECT producer.first_name, producer.last_name, movie.movie_title
FROM producer
INNER JOIN movie
ON producer.movie_id = movie.movie_id;