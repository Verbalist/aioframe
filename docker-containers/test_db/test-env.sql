SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

CREATE table public.test(
  id serial PRIMARY KEY ,
  test_attr_int INTEGER,
  test_attr_char VARCHAR(255)
) ;

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM test;
GRANT ALL ON SCHEMA public TO test;
GRANT ALL ON SCHEMA public TO PUBLIC;
