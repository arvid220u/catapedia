drop table if exists users;
create table users (
    id text primary key not null,
    username text not null,
    email text not null,
    passwordhash text not null,
);
drop table if exists lists;
create table lists (
    id text primary key not null,
    title text not null,
    description text,
);
drop table if exists items;
create table items (
    id text primary key not null,
    description text,
    wikipedialink text,
);
drop table if exists relatedlists;
create table relatedlists (
    list1id text not null,
    list2id text not null,
    primary key(list1id, list2id);
);
drop table if exists listitems;
create table listitems (
    id text primary key not null,
    listid text not null,
    itemid text,
    description text
);
