import requests
import mysql.connector

# MySQL database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'battlemetrics_bans'
}

# Battlemetrics API URL
API_URL = 'https://api.battlemetrics.com/servers/{server_id}/bans'

# Server ID (replace with your server's ID)
SERVER_ID = 'your_server_id'

def fetch_bans_from_battlemetrics():
    url = API_URL.format(server_id=SERVER_ID)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Failed to fetch bans: {response.content}")
        return []

def save_bans_to_mysql(bans):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    for ban in bans:
        steam_id = ban.get('attributes', {}).get('identifier', '')
        reason = ban.get('attributes', {}).get('reason', '')
        server_name = ban.get('relationships', {}).get('server', {}).get('data', {}).get('attributes', {}).get('name', '')

        # Insert ban into MySQL database
        query = "INSERT INTO bans (steam_id, reason, server_name) VALUES (%s, %s, %s)"
        cursor.execute(query, (steam_id, reason, server_name))

    conn.commit()
    cursor.close()
    conn.close()

def main():
    bans = fetch_bans_from_battlemetrics()
    save_bans_to_mysql(bans)
    print(f"Successfully saved {len(bans)} bans to MySQL database.")

if __name__ == '__main__':
    main()
