CREATE DATABASE battlemetrics_bans;

USE battlemetrics_bans;

CREATE TABLE bans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    steam_id VARCHAR(255) NOT NULL,
    reason TEXT,
    server_name VARCHAR(255),
    ban_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
