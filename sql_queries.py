# DROP TABLES

songplay_table_drop = "DROP TABLE if exists songplays"
user_table_drop = "DROP table if exists users"
song_table_drop = "DROP TABLE if exists songs"
artist_table_drop = "DROP TABLE if exists artists"
time_table_drop = "DROP TABLE if exists time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays (songplay_id SERIAL PRIMARY KEY,
start_time bigint NOT NULL,
userId int NOT NULL,
level text NOT NULL,
song_id text,
artist_id text,
sessionId int,
location text,
userAgent text)
""")

user_table_create = ("""create table if not exists users (userId text,
first_name text,
last_name text,
gender CHAR(1), 
level text)
""")

song_table_create = ("""create table if not exists songs (song_id text,
title text,
artist_id text,
year int,
duration float)
""")

artist_table_create = ("""create table if not exists artists (artist_id text,
name text, 
location text, 
latitude float,
longitude float)
""")

time_table_create = ("""create table if not exists time (start_time timestamp,
hour int,
day int,
week int,
month int,
year int, 
weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays (start_time, userId, level, song_id, artist_id, sessionId, location, userAgent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""insert into users (userId, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""insert into songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""insert into artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""insert into time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""select a.song_id, a.artist_id
from songs a
inner join artists b
on a.artist_id = b.artist_id
where a.title = %s
and b.name = %s
and a.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]