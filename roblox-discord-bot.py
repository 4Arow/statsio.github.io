import requests
import time

# Roblox Game ID and Webhook URL
GAME_ID = "140394439509533"  # Shark Cook Food
WEBHOOK_URL = "https://discord.com/api/webhooks/1373700814455177348/GZpVuhb92_TSwokmnJeLJoHVT913IxuE9hCZ_o1SYk5Tk8vVFobKuS2jdwNg-xOwj5vP"  # Replace with your webhook URL

def fetch_roblox_stats(game_id):
    """Fetches the current player count and lifetime visits of the game."""
    url = f"https://games.roblox.com/v1/games/{game_id}/stats"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        current_players = data.get("playerCount", "N/A")
        lifetime_visits = data.get("totalVisits", "N/A")
        return current_players, lifetime_visits
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None, None

def send_to_discord(player_count, visits):
    """Sends a formatted message to Discord via webhook."""
    message = {
        "content": f"**🦈 Shark Cook Food - Roblox Game Stats**\n\n👥 **Current Players:** {player_count}\n🌐 **Lifetime Visits:** {visits}"
    }
    response = requests.post(WEBHOOK_URL, json=message)
    
    if response.status_code == 204:
        print("Successfully sent update to Discord.")
    else:
        print(f"Failed to send message: {response.status_code}")

def main():
    """Main loop to fetch and send data every 30 minutes."""
    while True:
        player_count, visits = fetch_roblox_stats(GAME_ID)
        if player_count is not None and visits is not None:
            send_to_discord(player_count, visits)
        else:
            print("Skipping this update due to failed fetch.")
        
        print("Stats updated. Waiting for 30 minutes...")
        time.sleep(1800)  # 1800 seconds = 30 minutes

if __name__ == "__main__":
    main()
