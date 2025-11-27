import urllib.request
import json
import urllib.parse

def test_wiki():
    term = "Occam's Razor"
    encoded_term = urllib.parse.quote(term)
    url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={encoded_term}&limit=1&namespace=0&format=json"
    headers = {'User-Agent': 'MentalModelBot/1.0 (test@example.com)'}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            print(f"Success! Response: {data}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_wiki()
