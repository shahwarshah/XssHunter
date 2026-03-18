## 🔥 XssHunter - Advanced XSS Exploitation Engine


Made by: Syed Shahwar Ahmed
Type: CLI + Web UI XSS Payload Generator

🧩 Overview

XssHunter is a professional XSS exploitation toolkit designed for bug bounty hunters and penetration testers. It helps you:
Analyze filtering and blocked characters on injection points
Generate context-aware payloads (HTML, Attribute, JS, Unknown)
Automatically mutate payloads with bypass techniques
Load custom payload lists
Work via CLI or an interactive Web UI

It’s designed to maximize payload efficiency while testing vulnerable endpoints and simulate real-world bypasses.

🛠 Features
CLI Version

Context detection: HTML / Attribute / JS / Unknown
Filter observation questions: <script>, alert(), quotes, events, spaces, etc.

Payload mutation engine with:

Encoding & URL escaping
Case variation
Function constructor, object access, backtick execution
Custom payload loader from local files
Interactive prompts for dynamic testing

Copy-ready final payloads
Web UI Version
Green matrix hacker-style animated background
Centered, readable UI with bright cyan text
Select injection context
Checkbox filters for blocked characters
Custom payload paste area
Searchable payload results
Copy individual payloads

Supports same mutation engine as CLI

Optional: export all payloads (coming soon)

⚡ Installation

Clone the repository:

git clone https://github.com/shahwarshah/XssHunter.git
cd XssHunter

Install dependencies:
pip install -r requirements.txt

Dependencies include:
Flask (for Web UI)

Python 3.10+

🚀 Usage
CLI Version
python xsshunter_cli.py

Follow the prompts to select context

Answer filter questions (<script> blocked?, alert() blocked?)

Load custom payloads if needed

Generated payloads will be displayed in console

Web UI Version
cd Web-UI
python app.py

Open browser at http://127.0.0.1:5000
Select context, filters, and optionally paste custom payloads
Click Generate Payloads to see results
Copy individual payloads with the Copy button
Search or filter payloads dynamically

🎯 Example Workflow

Identify a possible XSS injection point.

Use XssHunter CLI or Web UI.

Select context (HTML / Attribute / JS / Unknown).
Answer filter questions to guide payload generation.
Copy the working payloads to your testing environment.
Optionally, add your own payloads and generate new mutations.

🧰 Recommended Usage

Only test on targets you own or have permission to test.
Combine with browser developer tools and proxy tools for live testing.
Keep a record of which payloads bypass filters for reporting.

📂 File Structure
XssHunter/
│
├─ xsshunter_cli.py          # CLI version
├─ Web-UI/
│   ├─ app.py                # Flask Web UI
│   ├─ templates/
│   │   └─ index.html        # Main web page
│   └─ static/
│       └─ (optional CSS/JS)
└─ requirements.txt
⚡ License

XssHunter is released under the MIT License. Use responsibly.

👨‍💻 Author

Syed Shahwar Ahmed – professional bug bounty hunter & security researcher
GitHub
 | LinkedIn
