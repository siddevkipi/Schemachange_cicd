use database DEMO_DB;
create schema KIPI1;
create table kipi_test_users2 if not exists(
  name varchar (100),  -- variable string column
  preferences string, -- column used to store JSON type of data
  created_at timestamp
);
