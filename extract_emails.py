"""
Task 2: Extract all email addresses from a .txt file and save to another file.
Concepts: re (regex), file handling
"""
import re
import os
from collections import Counter
from datetime import datetime

def extract_emails(input_file, output_file):
    result = {"total": 0, "unique": 0, "domains": {}, "emails": []}
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
    email_pattern = r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
    all_emails = re.findall(email_pattern, content)
    result["total"] = len(all_emails)
    unique_emails = sorted(set(e.lower() for e in all_emails))
    result["unique"] = len(unique_emails)
    result["emails"] = unique_emails
    domains = [e.split("@")[1] for e in unique_emails]
    result["domains"] = dict(Counter(domains).most_common())
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("  EXTRACTED EMAIL ADDRESSES\n")
        f.write("=" * 50 + "\n")
        f.write(f"  Total found  : {result['total']}\n")
        f.write(f"  Unique emails: {result['unique']}\n")
        f.write(f"  Extracted on : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")
        f.write("UNIQUE EMAILS:\n")
        for email in unique_emails:
            f.write(f"  {email}\n")
        f.write(f"\nDOMAIN BREAKDOWN:\n")
        for domain, count in result["domains"].items():
            f.write(f"  {domain:30s} -> {count} email(s)\n")
    print(f"  Found {result['total']} emails ({result['unique']} unique)")
    print(f"  Saved to: {output_file}")
    return result

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    inp  = os.path.join(base, "sample_data", "emails.txt")
    out  = os.path.join(base, "output", "extracted_emails.txt")
    print("=" * 50)
    print("  EMAIL EXTRACTOR")
    print("=" * 50)
    result = extract_emails(inp, out)
    print("\n  Top domains found:")
    for domain, count in list(result["domains"].items())[:5]:
        print(f"    {domain}: {count}")
