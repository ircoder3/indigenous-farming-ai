import csv, requests, time

QUERIES = [
    "crop rotation Karnataka rainfed",
    "ragi groundnut rotation Karnataka",
    "tank irrigation Karnataka traditional",
    "kere tank cascade Karnataka",
    "traditional water harvesting Karnataka",
    "indigenous pest management Karnataka",
    "traditional pest control neem Karnataka",
    "traditional intercropping Karnataka",
    "arecanut intercropping Karnataka",
    "indigenous technical knowledge Karnataka farmers",
]
EMAIL = "your_email@example.com"  # OpenAlex asks for this (faster, polite pool)

def abstract_text(inv):
    if not inv:
        return ""
    words = {}
    for w, positions in inv.items():
        for p in positions:
            words[p] = w
    return " ".join(words[i] for i in sorted(words))

seen, rows = set(), []
for q in QUERIES:
    r = requests.get("https://api.openalex.org/works", params={
        "search": q,
        "filter": "from_publication_date:2010-01-01",
        "per-page": 50,
        "mailto": EMAIL,
    }, timeout=30)
    for w in r.json().get("results", []):
        if w["id"] in seen:
            continue
        seen.add(w["id"])
        rows.append({
            "query": q,
            "title": w.get("title"),
            "year": w.get("publication_year"),
            "journal": ((w.get("primary_location") or {}).get("source") or {}).get("display_name"),
            "doi": w.get("doi"),
            "is_open_access": (w.get("open_access") or {}).get("is_oa"),
            "pdf_or_page": (w.get("open_access") or {}).get("oa_url"),
            "abstract": abstract_text(w.get("abstract_inverted_index")),
        })
    time.sleep(1)

with open("candidates.csv", "w", newline="", encoding="utf-8") as f:
    wr = csv.DictWriter(f, fieldnames=rows[0].keys())
    wr.writeheader()
    wr.writerows(rows)
print("Saved", len(rows), "candidates")