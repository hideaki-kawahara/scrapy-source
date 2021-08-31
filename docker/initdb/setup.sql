create table recipes
(
    id SERIAL,
    site_url TEXT NOT NULL,
    title TEXT NOT NULL,
    detail TEXT NOT NULL,
    cooking_time TEXT NOT NULL,
    budget TEXT NOT NULL,
    ingredient TEXT NOT NULL,
    how_to_make TEXT NOT NULL,
    tip TEXT NOT NULL,
    created_at timestamp with time zone default CURRENT_TIMESTAMP,
    updated_at timestamp with time zone default CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
