phishing_keywords = [
    "verify", "account", "urgent", "password",
    "click", "login", "bank", "suspended"
]

def detect_phishing(email_text):
    score = 0
    reasons = []

    text = email_text.lower()

    for word in phishing_keywords:
        if word in text:
            score += 1
            reasons.append(f"Contains suspicious word: {word}")

    if "http://" in text or "https://" in text:
        score += 1
        reasons.append("Contains a link")

    if score >= 3:
        verdict = "Phishing"
    else:
        verdict = "Likely Safe"

    return verdict, score, reasons


#email = input("Paste email text:\n")
email="""Hello team,
The meeting is scheduled tomorrow at 10am.
Best regards."""
result = detect_phishing(email)
print("\nVerdict:", result[0])
print("Risk score:", result[1])
print("Reasons:")
for r in result[2]:
    print("-", r)
