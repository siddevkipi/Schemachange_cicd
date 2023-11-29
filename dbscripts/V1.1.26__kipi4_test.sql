use database DEMO_DB;
create schema KIPI11;
create table kipi_test_users11 if not exists(
  name varchar (100),  -- variable string column
  preferences string, -- column used to store JSON type of data
  created_at timestamp
);
