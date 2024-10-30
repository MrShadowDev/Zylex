# bypass.py
import time
import requests
import pyperclip
import json
import sys  

url_to_bypass = input("\033[93mURL to bypass: ")

url = f"https://api.bypass.vip/bypass?url={url_to_bypass}"

payload = {}
headers = {} 

try:
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    if data.get("status") == "success":
        result_link = data.get("result")
        
        print(f"\033[92mResult -> {result_link}")
        pyperclip.copy(result_link)
        print("\033[96mLink copied to your clipboard!")
        
        time.sleep(3)
    else:
        print("\033[91mError:", data.get("message", "Unknown error"))
        time.sleep(3)  

except Exception as e:
    print(f"\033[91mAn error occurred: {e}")
    time.sleep(3)

finally:
    sys.exit()
