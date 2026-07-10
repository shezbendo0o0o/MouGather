import os
import urllib.parse

def _digits(value):
    return "".join(ch for ch in str(value) if ch.isdigit())

def add(number, report):
    number = str(number).strip()
    digits = _digits(number)

    if not digits:
        return

    plus_number = number if number.startswith("+") else "+" + digits
    q_plus = urllib.parse.quote_plus(plus_number)
    q_digits = urllib.parse.quote_plus(digits)

    links = [
        ("Truecaller official reverse lookup", "https://www.truecaller.com/reverse-phone-number-lookup"),
        ("Truecaller official site", "https://www.truecaller.com/"),
        ("Getcontact official site", "https://getcontact.com/en/"),
        ("Sync.me reverse lookup", "https://sync.me/search/?number={}".format(q_digits)),
        ("WhoCallsMe reverse lookup", "https://whocallsme.com/"),
        ("tellows reverse lookup", "https://www.tellows.com/num/{}".format(q_digits)),
        ("NumLookup reverse lookup", "https://www.numlookup.com/"),
        ("Google exact number", "https://www.google.com/search?q=%22{}%22".format(q_plus)),
        ("Google digits only", "https://www.google.com/search?q=%22{}%22".format(q_digits)),
        ("Yandex exact number", "https://yandex.com/search/?text=%22{}%22".format(q_plus)),
    ]

    print("\n[+]EXTENDED MANUAL PHONE LOOKUP LINKS")
    print("[I] Some services may require login/app verification.\n")

    os.makedirs(os.path.dirname(report), exist_ok=True)

    with open(report, "a", encoding="utf-8", errors="ignore") as f:
        f.write("\n\nEXTENDED MANUAL PHONE LOOKUP LINKS:\n")
        f.write("Some services may require login/app verification.\n")

        for name, url in links:
            print("[v]{}: {}".format(name, url))
            f.write("{}: {}\n".format(name, url))

    print("\n[I] Extended links added to report: {}".format(report))
