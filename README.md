# SQL Injection Scanner (DVWA)

A Python-based SQL Injection Scanner designed to detect common SQL Injection vulnerabilities in web applications.  
This project is developed **strictly for educational and ethical testing purposes** using **DVWA (Damn Vulnerable Web Application)** on a local environment.

---

## 📌 Project Objective

To build a script that:
- Sends common SQL Injection payloads
- Detects vulnerability indicators in responses
- Logs vulnerable payloads
- Works only on **authorized targets** like DVWA / localhost

---

## ⚙️ Technologies Used

- Python 3.x  
- Requests library  
- DVWA (Damn Vulnerable Web Application)  
- XAMPP (Apache + MySQL)

---

## 🧪 Testing Environment

- Target: `DVWA (localhost)`
- Security Level: **LOW**
- Authorization: **Allowed / Lab environment only**

⚠️ **Do NOT use this tool on real websites without permission**

---

## 🚀 How It Works

1. User provides:
   - Base URL (without parameters)
   - Parameter name (e.g., `id`)
2. The script injects common SQL payloads
3. Server responses are analyzed
4. If SQL error or abnormal output is detected → marked as **VULNERABLE**
5. Results are displayed in the terminal

---

## ▶️ How to Run

### Step 1: Install required module

pip install requests

Step 2: Start DVWA
Start Apache & MySQL using XAMPP
Login to DVWA
Set Security Level to LOW

Step 3: Run the scanner

python sql_injection_scanner.py

Step 4: Input example

Enter base URL (without parameters): http://localhost/DVWA/vulnerabilities/sqli/

Enter parameter name (e.g., id): id

📤 Sample Output

[VULNERABLE] Payload worked → 1' OR '1'='1

[VULNERABLE] Payload worked → 1' OR 1=1--

[VULNERABLE] Payload worked → 1" OR "1"="1

[+] Scan completed.

📸 Proof of Vulnerability

Manual testing using payload:

Sql

1' OR '1'='1

Returned multiple database records, confirming SQL Injection.


🔐 Ethical Disclaimer

This project is created only for learning and authorized testing.

❌ Illegal usage on real-world targets is strictly prohibited.

✅ Tested only on DVWA (local lab).


💡 Future Improvements

Blind SQL Injection detection,POST parameter scanning,Automated parameter discovery,Rate limiting & concurrency control,Secure coding recommendations.
