CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    email TEXT NOT NULL,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birthday TEXT NOT NULL, -- simulando una fecha
);

CREATE TABLE acounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    acount_number TEXT NOT NULL UNIQUE,
    balance REAL NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    sender_acount_id INTEGER NOT NULL, 
    recipient_acount_id INTEGER NOT NULL,
    transaction_number TEXT NOT NULL UNIQUE, -- unique significa que no se puede repetir en los registros de la bd
    amount REAL NOT NULL,
    concept TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(sender_acount_id) REFERENCES acounts(id),
    FOREIGN KEY(recipient_acount_id) REFERENCES acounts(id)
);