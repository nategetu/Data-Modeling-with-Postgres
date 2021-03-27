# Song Play Analysis Guide
This project retrieves songplay and user activity information from the Sparkify music streaming app for analysis.

## Purpose
Analysts at Sparkify can utilize this package to better understand which songs Sparkify users are listening to.

## Design
This project implements a Postgres database in a star schema (displayed below) centered on the 'songplays' table, which provides information on individual song plays in Sparkify.

![Table Schema Design](https://github.com/nategetu/Data-Modeling-with-Postgres/blob/main/tableSchemaDesign.jpg?raw=true)

Auxiliary tables for analysis include tables with information on app users, songs in Sparkify, the artists who create those songs, and timestamps for song plays.
The schema design allows for quick retrieval of song play records, as well as giving the end-user analyst the opportunity to join in auxiliary dimension tables for additional analysis on different variables (e.g. users, artists)

Source data exists as JSON files for song and play information which are extracted and transformed in python script 'etl.py' and loaded to Postgres tables created in 'create_tables.py'

## Instructions & Tips
1. Execute python script 'create_tables.py', which creates the Postgres tables in databse 'studentdb' for final output as specified in 'sql_queries.py'
2. Execute python script 'etl.py' to extract data from the song and log JSON files in the 'data' folder and populate the tables listed above
3. Perform analysis as needed using user-defined scripts

- 'etl.ipynb' and 'test.ipynb' are used for debugging the ETL process and are not necessary for package use by end-users
