import re
import json


def country_code_to_flag(code: str) -> str:
    """Convert ISO country code to flag emoji."""
    if not code or len(code) != 2:
        return ""
    return "".join(chr(ord(c) - ord("A") + 0x1F1E6) for c in code.upper())


def flag_to_country_code(flag: str) -> str:
    """Convert flag emoji to ISO country code."""
    code_points = [ord(c) for c in flag if ord(c) >= 0x1F1E6]
    if len(code_points) >= 2:
        return "".join(chr(cp - 0x1F1E6 + ord("A")) for cp in code_points[:2])
    return ""


def parse_markdown(md_content: str) -> list[dict]:
    countries = []

    country_pattern = re.compile(
        r"^#{1,2}\s*([\U0001F1E6-\U0001F1FF]{2})\s*(.+?)\s*$", re.MULTILINE
    )
    phone_pattern = re.compile(
        r"#{5}\s*Phone Number\s*\n-\s*\*\*Pattern:\*\*\s*`(.+?)`"
    )
    postal_pattern = re.compile(
        r"#{5}\s*Postal Code\s*\n-\s*\*\*Pattern:\*\*\s*`(.+?)`"
    )

    sections = re.split(
        r"(?=^#{1,2}\s*[\U0001F1E6-\U0001F1FF])", md_content, flags=re.MULTILINE
    )

    for section in sections:
        country_match = country_pattern.search(section)
        if not country_match:
            continue

        flag = country_match.group(1)
        name = country_match.group(2).strip()
        country_code = flag_to_country_code(flag)

        # Regenerate flag from code (ensures consistency)
        flag = country_code_to_flag(country_code)

        phone_match = phone_pattern.search(section)
        postal_match = postal_pattern.search(section)

        phone_regex = phone_match.group(1) if phone_match else None
        postal_regex = postal_match.group(1) if postal_match else None

        if postal_regex == "❌":
            postal_regex = None

        countries.append({
            "country_code": country_code,
            "country_name": name,
            "flag": flag,
            "dial_code": extract_dial_code(phone_regex),
            "phone_regex": phone_regex,
            "postal_code_regex": postal_regex,
        })

    return countries


def extract_dial_code(phone_regex: str) -> str | None:
    """Try to extract dial code from phone regex pattern."""
    if not phone_regex:
        return None
    
    # Common patterns: \+93, \+?355, (\+?213), +1
    match = re.search(r"\\?\+\??(\d{1,4})", phone_regex)
    if match:
        return f"+{match.group(1)}"
    return None


if __name__ == "__main__":
    with open("phone_list.md", "r", encoding="utf-8") as f:
        md_content = f.read()

    data = parse_markdown(md_content)

    with open("phone_list.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Parsed {len(data)} countries")
    
    # Preview
    for country in data[:3]:
        print(f"{country['flag']} {country['country_code']} {country['country_name']} ({country['dial_code']})")