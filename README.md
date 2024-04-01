Sure, here's a README to guide you through setting up and running the program to fetch ban information from a Battlemetrics server and store it in a MySQL database.

---

# Battlemetrics Bans to MySQL

This program fetches ban information from a Battlemetrics server using their API and stores it in a MySQL database.

## Prerequisites

- Python 3.x
- pip package manager
- MySQL server

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/battlemetrics-bans-to-mysql.git
cd battlemetrics-bans-to-mysql
```

### 2. Install Required Packages

Install the required Python packages using `pip`:

```bash
pip install requests mysql-connector-python
```

## Configuration

### 1. MySQL Database Setup

- Create a new MySQL database for storing the ban information:

```sql
CREATE DATABASE battlemetrics_bans;
USE battlemetrics_bans;
CREATE TABLE bans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    steam_id VARCHAR(255) NOT NULL,
    reason TEXT,
    server_name VARCHAR(255),
    ban_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. Update Database Configuration

Open `battlemetrics_bans_to_mysql.py` in a text editor and update the `DB_CONFIG` dictionary with your MySQL database connection details:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'battlemetrics_bans'
}
```

### 3. Set Battlemetrics Server ID

Replace `'your_server_id'` with your Battlemetrics server ID in the `battlemetrics_bans_to_mysql.py` file:

```python
SERVER_ID = 'your_server_id'
```

## Usage

Run the Python script to fetch bans from Battlemetrics and store them in the MySQL database:

```bash
python battlemetrics_bans_to_mysql.py
```

The program will print a message indicating the number of bans successfully saved to the MySQL database.

## Troubleshooting

- If you encounter any issues, ensure that:
  - MySQL server is running.
  - Database connection details in `DB_CONFIG` are correct.
  - Battlemetrics server ID is correct.

## Contributing

If you have suggestions or improvements, please create a pull request or open an issue.

---

That's it! Follow these steps to set up and run the program to fetch and store ban information from a Battlemetrics server to a MySQL database.
