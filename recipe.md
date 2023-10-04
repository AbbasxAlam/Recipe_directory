Single Table Design Recipe Template
Copy this recipe template to design and create a database table from a specification.

1. Extract nouns from the user stories or specification
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
Nouns:
coach, student_name, student_cohort,

2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	Properties
cohort	start_date, coach
student first_name, last_name
Name of the table (always plural): cohorts, students

Column names: start_date, coach, first_name, last_name

3. Decide the column types
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

id: SERIAL
start_date: int
coach: text
first_name: text
last_name: text

4. Write the SQL
-- EXAMPLE
-- file: student_directory_1.sql

-- Replace the table name, columm names and types.

CREATE TABLE cohort (
  id SERIAL PRIMARY KEY,
  start_date int,
  coach text
);

CREATE TABLE student (
  id SERIAL PRIMARY KEY,
  first_name text,
  second_name text
);
5. Create the table
psql -h 127.0.0.1 database_name < albums_table.sql













Single Table Design Recipe Template
Copy this recipe template to design and create a database table from a specification.

1. Extract nouns from the user stories or specification
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' titles.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' genres.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' release years.

Nouns:
title, genre, release_year, movie

2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	Properties
movie	title, genre, release_year

Name of the table (always plural): movie

Column names: title, genre, release_year

3. Decide the column types
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

id: SERIAL
title: text
genre: text
release_year: int


4. Write the SQL
-- EXAMPLE
-- file: student_directory_1.sql

-- Replace the table name, columm names and types.

CREATE TABLE movie (
  id SERIAL PRIMARY KEY,
  title text,
  genre text,
  release_year int
);


5. Create the table
psql -h 127.0.0.1 database_name < albums_table.sql











Single Table Design Recipe Template
Copy this recipe template to design and create a database table from a specification.

1. Extract nouns from the user stories or specification
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).

Nouns:
recipe, name, cooking_time, rating

2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	Properties
cookbook	recipe_name, cooking_time, rating

Name of the table (always plural): cookbook

Column names: recipe_name, cooking_time, rating

3. Decide the column types
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

id: SERIAL
recipe_name: text
cooking_time, int
rating: int

4. Write the SQL
-- EXAMPLE
-- file: recipe_director.sql

-- Replace the table name, columm names and types.

CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  cooking_time int,
  recipe_name text,
  rating, int
);


5. Create the table
psql -h 127.0.0.1 database_name < albums_table.sql