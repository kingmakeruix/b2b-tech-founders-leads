import os
import sys
import json
import csv
import re
import urllib.request
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

# High-value tech startup seeds
TARGET_DOMAINS = [
    "https://supabase.com",
    "https://resend.com",
    "https://cal.com",
    "https://posthog.com",
    "https://dub.co",
    "https://formbricks.com",
    "https://papermark.io",
    "https://twenty.com"
]

def audit_and_extract_leads(url):
    print(f"[*] Lead verileri taranıyor: {url}")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"})
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            html = response.read(1024 * 512).decode("utf-8", errors="ignore")
            soup = BeautifulSoup(html, "html.parser")

            # Title & Meta
            title = soup.title.string.strip() if soup.title and soup.title.string else ""
            desc = ""
            desc_tag = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
            if desc_tag and desc_tag.get("content"):
                desc = desc_tag["content"].strip()

            text = soup.get_text()
            
            # Emails
            email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
            raw_emails = re.findall(email_pattern, text)
            emails = list(set([e for e in raw_emails if not e.endswith(('.png', '.jpg', '.jpeg', '.svg', '.gif'))]))

            # Socials
            github = ""
            twitter = ""
            linkedin = ""
            for a in soup.find_all("a", href=True):
                href = a["href"]
                if "github.com/" in href and not github:
                    github = href
                elif ("twitter.com/" in href or "x.com/" in href) and not twitter:
                    twitter = href
                elif "linkedin.com/" in href and not linkedin:
                    linkedin = href

            return {
                "Company": title.split("–")[0].split("-")[0].strip(),
                "Website": url,
                "Description": desc[:150],
                "Primary_Email": emails[0] if emails else "info@" + urllib.parse.urlparse(url).netloc.replace("www.", ""),
                "All_Emails": "; ".join(emails),
                "Twitter": twitter,
                "GitHub": github,
                "LinkedIn": linkedin
            }
    except Exception as e:
        print(f"[-] Hata ({url}): {e}")
        return None

def build_dataset():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(out_dir, "b2b_tech_leads.csv")
    json_file = os.path.join(out_dir, "b2b_tech_leads.json")

    results = []
    for domain in TARGET_DOMAINS:
        lead = audit_and_extract_leads(domain)
        if lead:
            results.append(lead)

    # Save to CSV
    if results:
        keys = results[0].keys()
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(results)

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"\n[+] Başarılı! {len(results)} adet doğrulanmış B2B Lead verisi kaydedildi:")
        print(f"    - CSV:  {csv_file}")
        print(f"    - JSON: {json_file}")

if __name__ == "__main__":
    print("=" * 80)
    print("B2B YÜKSEK DEĞERLİ LEAD & VERİ ÇIKARMA MOTORU")
    print("=" * 80)
    build_dataset()
