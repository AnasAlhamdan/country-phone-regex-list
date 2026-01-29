# 🌍 Country Phone Regex List

A comprehensive JSON dataset containing phone number validation patterns, postal code regex, dial codes, and flag emojis for 160+ countries and territories.

## ✨ Features

- 📱 Phone number regex patterns for validation
- 📮 Postal code regex patterns
- 🏳️ Flag emojis for each country
- 📞 International dial codes
- 🔤 ISO 3166-1 alpha-2 country codes

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/AnasAlhamdan/country-phone-regex-list.git

# Or download the JSON directly
curl -O https://raw.githubusercontent.com/AnasAlhamdan/country-phone-regex-list/main/phone_list.json
```

## 📋 Data Structure

Each country entry contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `country_code` | `string` | ISO 3166-1 alpha-2 code |
| `country_name` | `string` | Full country name |
| `flag` | `string` | Flag emoji |
| `dial_code` | `string \| null` | International dialing code |
| `phone_regex` | `string \| null` | Regex pattern for phone validation |
| `postal_code_regex` | `string \| null` | Regex pattern for postal code validation |

### Example Entry

```json
{
  "country_code": "SA",
  "country_name": "Saudi Arabia",
  "flag": "🇸🇦",
  "dial_code": "+966",
  "phone_regex": "^(!?(\\+?966)|0)?5\\d{8}$",
  "postal_code_regex": "^\\d{5}(-{1}\\d{4})?$"
}
```

## 🚀 Usage Examples

### JavaScript / TypeScript

```ts
import countries from "./phone_list.json";

// Find a country by code
const usa = countries.find((c) => c.country_code === "US");

// Validate a phone number
function validatePhone(countryCode: string, phone: string): boolean {
  const country = countries.find((c) => c.country_code === countryCode);
  if (!country?.phone_regex) return false;
  return new RegExp(country.phone_regex).test(phone);
}

// Example
validatePhone("SA", "+966512345678"); // true
```

### Python

```python
import json
import re

with open("phone_list.json", "r", encoding="utf-8") as f:
    countries = json.load(f)

def validate_phone(country_code: str, phone: str) -> bool:
    country = next((c for c in countries if c["country_code"] == country_code), None)
    if not country or not country.get("phone_regex"):
        return False
    return bool(re.match(country["phone_regex"], phone))

# Example
validate_phone("SA", "+966512345678")  # True
```

### Building a Country Selector

```html
<select id="country-select">
  <option value="">Select a country</option>
</select>

<script>
  fetch("phone_list.json")
    .then((res) => res.json())
    .then((countries) => {
      const select = document.getElementById("country-select");
      countries.forEach((c) => {
        const option = document.createElement("option");
        option.value = c.country_code;
        option.textContent = `${c.flag} ${c.country_name} (${c.dial_code || "N/A"})`;
        select.appendChild(option);
      });
    });
</script>
```

## 🛠️ Use Cases

- **Form Validation** — Validate phone numbers and postal codes in user registration forms
- **Country Selectors** — Build dropdowns with flags and dial codes
- **Phone Input Components** — Auto-format phone numbers based on country
- **Address Verification** — Validate postal/ZIP codes by country
- **Internationalization (i18n)** — Display localized country information
- **Telecom Applications** — Route calls based on dial codes

## 📁 Files

| File | Description |
|------|-------------|
| `phone_list.json` | The main JSON dataset |
| `phone.py` | Python script used to parse and convert the data |
| `index.html` | Interactive preview UI for browsing the data |

## 🔄 Generating the Data

The JSON data was converted from markdown using `phone.py`:

```bash
python phone.py
```

This script:
1. Parses the source markdown file
2. Extracts country flags and converts them to ISO codes
3. Extracts phone and postal code regex patterns
4. Infers dial codes from phone regex patterns
5. Outputs structured JSON

## 📄 License

MIT License — feel free to use this data in your projects.

---

## 🙏 Data Source

The regex patterns in this repository were sourced from [ariankoochak/regex-patterns-of-all-countries](https://github.com/ariankoochak/regex-patterns-of-all-countries) and converted to structured JSON format.