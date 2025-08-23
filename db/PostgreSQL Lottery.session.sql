CREATE TABLE res_lottery (
    id SERIAL PRIMARY KEY,
    provinece VARCHAR(100) NOT NULL,
    lottery_number VARCHAR(20) NOT NULL,
    date DATE NOT NULL
);
