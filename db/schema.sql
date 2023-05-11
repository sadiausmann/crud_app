CREATE DATABASE recipe_app;

\c recipe_app

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password_digest TEXT
);

CREATE TABLE recipes(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  title TEXT,
  image_url image,
  recipe TEXT
);

CREATE TABLE comments(
  id SERIAL PRIMARY KEY,
  recipe_id INTEGER,
  user_id INTEGER
  comment TEXT,
);

CREATE TABLE likes(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  food_id INTEGER
);

