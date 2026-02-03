import re

rules = {
    "keywords": {
        "words": ["name", "personal", "admin", "password", "login", "bank", "suspended"],
        "weight": 20
    },
    "links": {
        "pattern": r"http[a]?://",
        "weight": 30
    },
    "request_info": {
        "words": ["ssn", "credit card", "cvv", "pin"],
        "weight": 40
    }
}

def phishing(email):
    score = 0
    reasons = []
    text = email.lower()

    for word in rules["keywords"]["words"]:
        if word in text:
            score += rules["keywords"]["weight"]
            reasons.append(f"Suspicious keyword: {word}")

    if re.search(rules["links"]["pattern"], text):
        score += rules["links"]["weight"]
        reasons.append("Contains link")

    for word in rules["request_info"]["words"]:
        if word in text:
            score += rules["request_info"]["weight"]
            reasons.append(f"Sensitive data request: {word}")

    if score >= 70:
        verdict = "High Risk - Phishing"
    elif score >= 40:
        verdict = "Medium Risk"
    else:
        verdict = "Low Risk"

    return verdict, score, reasons


#email = input("Paste email:\n")
email="""Your account is suspended.
Click here to verify your password."""
v, s, r =phishing(email)
print("\nVerdict:", v)
print("Risk:", s, "%")
print("Reasons:")
for i in r:
    print("-", i)
