import requests

def get_public_ip():
    try:
        # Request public IP address from a public API
        response = requests.get("https://api.ipify.org")
        
        if response.status_code == 200:
            public_ip = response.text
            print("Your public IP address is:", public_ip)
        else:
            print("Failed to retrieve public IP address:", response.status_code)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    get_public_ip()