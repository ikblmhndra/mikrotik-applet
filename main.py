import base64
import json
import sys
import subprocess

def main(base64_json_data):
    # Decode the base64 encoded JSON data
    decoded_data = base64.b64decode(base64_json_data).decode('utf-8')
    data = json.loads(decoded_data)

    app_name = data["app_name"]
    protocol = data["protocol"]
    user = data["user"]
    asset = data["asset"]
    account = data["account"]
    platform = data["platform"]

    # Prepare the Winbox command with address, username, and password
    winbox_command = [
        "C:\\Program Files\Winbox\winbox64.exe",
        f"{asset['address']}",
        f"user={account['username']}",
        f"password={account['secret']}"
    ]

    # Launch Winbox with the provided details
    subprocess.run(winbox_command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <base64_json_data>")
        sys.exit(1)
    
    base64_json_data = sys.argv[1]
    main(base64_json_data)
