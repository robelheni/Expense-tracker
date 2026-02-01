

# Expense Tracker

I builtt a web application to track personal expenses  and built it with fatsapi and PostgreSQL.

## Features

- Add expenses with description and amount
- View all expenses
- Calculate total spending
- Data persists in PostgreSQL database

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL

### Installation

1. Clone this repository:
```bash
   git clone https://github.com/YOUR_USERNAME/expense-tracker.git
   cd expense-tracker
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Create a PostgreSQL database:
```bash
   psql -U postgres
   CREATE DATABASE expense_tracker;
   \q
```

4. Create a `.env` file in the root directory:
```
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/expense_tracker
```

5. Create the database tables:
```bash
   python create_tables.py
```

6. Run the application:
```bash
   uvicorn main:app --reload
```

7. Open your browser and go to: `http://127.0.0.1:8000/docs`

## API Endpoints

- `GET /` - Hello World
- `POST /expenses` - Add a new expense
- `GET /expenses` - Get all expenses
- `GET /expenses/total` - Get total of all expenses

## Author

Robel Gashu - Computer Science Student

## License

This project is open source 