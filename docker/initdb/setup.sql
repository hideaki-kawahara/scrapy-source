create table tags
(
    id SERIAL,
    keyword TEXT NOT NULL,
    count INTEGER NOT NULL,
    create_at timestamp with time zone default CURRENT_TIMESTAMP,
    update_at timestamp with time zone default CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
