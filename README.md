# BASIC-WALLET 
#### VIDEO: https://youtu.be/TllEwMs6uyw
#### DESCRIPTION:

## Overview
**Basic Wallet** is a simple web banking application built with Flask. Users can create an account, log in, view their balance and account number, transfer money to other users, and review their transaction history.
The goal of this project is to practice a modular Flask architecture (Blueprints + services + models) while implementing a complete authentication and money-transfer flow with both client-side and server-side validation.
## Features
- User registration and login with hashed passwords
- Session-based authentication (Flask-Session, filesystem storage)
- Personal dashboard with account number and balance
- Money transfers between accounts
- Transaction history (sent and received)
- Client-side validation with JavaScript regular expressions
- Server-side validation before database operations
- SQLite database with uniqueness constraints for account and transaction numbers
## Tech Stack
- **Backend:** Flask, Flask-Session, SQLite3
- **Frontend:** HTML, Jinja, Bootstrap, JavaScript
- **Security:** password hashing, environment-based `SECRET_KEY`, `login_required` decorator
## Design / Architecture
This project uses a modular architecture based on Flask Blueprints. Instead of placing the entire application in a single `app.py` file, features are split into independent modules. This improves maintainability, readability, and scalability.
Each feature module follows the same internal structure:
| File          | Responsibility                                          |
|---------------|---------------------------------------------------------|
| `__init__.py` | Creates the Blueprint and URL prefix                    |
| `routes.py`   | HTTP endpoints; receives requests and returns responses |
| `services.py` | Business logic and server-side validation               |
| `models.py`   | Database queries                                        |

## Project Structure

The application is organized inside the `app/` package.

- `app/__init__.py` creates the Flask application, loads the configuration, initializes extensions, registers all Blueprints, and configures Jinja filters.
- `app/config.py` contains the Config class responsible for loading environment variables and configuring sessions and the SQLite database.
- `app/db.py` manages database connections and automatically closes them after every request.
- `app/extensions.py` initializes Flask extensions such as Flask-Session.
- `app/helpers.py` contains helper functions shared across the application.
- `app/static/` stores CSS and JavaScript files.
- `app/templates/` stores all HTML templates grouped by Blueprint.

## Blueprints

The application is divided into three independent Blueprints.

why blueprints?

They allow you to split a large application into smaller, reusable components by grouping routes, templates, and static files, instead of writing everything in a single `app.py` file.

workflow

1. Browser
     ↓
2. routes.py
     ↓
3. services.py
     ↓
4. models.py
     ↓
5. SQLite

### auth

Responsible for user registration, login, logout, password hashing, and session management.

### account

Displays the user's dashboard, account information, account number, and current balance.

### transactions

Handles money transfers, validates account numbers and balances, creates transaction records, and displays transaction history.

workflow

1. Validate destination account number.
2. Verify that the destination account exists.
3. Check that the sender has sufficient funds.
4. Create the transaction.
5. Update both account balances.
6. Commit the transaction.

## DATABASE

The database contains three tables:

users: stores user information, such as first name, last name, username, and password.

accounts: linked to the users table via a `user_id`; each user can have an account with a 12-digit number and an initial balance of 
$10,000.

transactions: stores transaction details—such as the date, amount, and the account numbers involved—using a relationship based on two keys: `sender_account_id` and `recipient_account_id`.

## Design Decisions

One of the main design decisions was separating the project into Blueprints instead of implementing everything inside a single Flask application file.

Additionally, every Blueprint follows the same internal architecture by separating routes, services, and models.

Routes are responsible only for handling HTTP requests and responses.

Services contain all business logic, including validation, random account generation, transaction validation, and processing.

Models perform all database operations.

This separation keeps each file focused on a single responsibility and makes the application easier to maintain as it grows.

Another important decision was implementing validation on both the client and the server, since client-side JavaScript validation can easily be bypassed.

JavaScript regular expressions provide immediate feedback to users before submitting forms, improving usability.

However, every validation is repeated on the server because client-side validation can be bypassed.

The decision was made to use unique fields for account numbers and transaction numbers; these are validated on the back end using try-except blocks to handle integrity errors.

## Challenges

The most challenging part of the project was designing a modular architecture. At first I considered implementing all routes in a single Flask application, but as new features were added, the code became increasingly difficult to maintain. Refactoring the project into Blueprints with separate routes, services, and models required more initial work but resulted in a much cleaner and more scalable design.

## Future Improvements

If I continue developing this project, I would like to add password recovery, email verification, REST API endpoints, account statements in PDF format, recurring transfers, unit testing, and migration from SQLite to PostgreSQL.

## Setup

1. Create a virtualenv: 
   `python -m venv .venv`
   activate virtualenv:
   `.venv\Scripts\Activate.ps1`
   install dependencies:
   `pip install -r requirements.txt`

2. Set a `SECRET_KEY` in `.env`, you can use: `python -c "import secrets; print(secrets.token_hex(32))"`

3. Run:
   `flask --app run.py run` 
   or 
   `python run.py`
4. Database:
   `python -m sqlite3 wallet.db` or `python -m sqlite3 wallet.db < schema.sql`
 
5. Schema: use a schema.sql for create all tables.
