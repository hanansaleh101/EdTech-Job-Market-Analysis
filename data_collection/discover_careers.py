import pandas as pd
from ddgs import DDGS

# ------------------------------------
# Read Excel
# ------------------------------------

df = pd.read_excel(
    "data/GSV_150_Company_Tracking_Template.xlsx",
    dtype=str
).fillna("")

# ------------------------------------
# Search Settings
# ------------------------------------

queries = [
    "{} careers",
    "{} jobs",
    "{} work with us",
    "{} hiring"
]

good_keywords = [
    "career",
    "careers",
    "jobs",
    "job",
    "greenhouse",
    "lever",
    "ashby",
    "workable",
    "teamtailor",
    "smartrecruiters",
    "job-boards",
    "freshteam",
    "applytojob",
    "bamboohr"
]

bad_domains = [
    "linkedin.com",
    "glassdoor.com",
    "indeed.com",
    "ziprecruiter.com",
    "facebook.com",
    "mycareersfuture.gov.sg",
    "builtin.com",
    "careers360.com",
    "traderjoes.com",
    "palantir.com",
    "luminik.io",
    "fitt.co",
    "cardrates.com",
    "emergecapital.vc",
    "metaintro.com"
]

# ------------------------------------
# Search Careers Pages
# ------------------------------------

with DDGS() as ddgs:

    for index, row in df.iterrows():

        company = row["Company"]

        # Skip if already found
        if row["Careers Page"] != "":
            continue

        print(f"\nSearching {company}")

        careers_url = ""

        for search in queries:

            query = search.format(company)

            print(f"   Trying: {query}")

            try:

                results = list(
                    ddgs.text(
                        query,
                        max_results=10
                    )
                )

            except Exception as e:
                print(e)
                continue

            for result in results:

                url = result["href"].lower()

                # Ignore bad websites
                if any(domain in url for domain in bad_domains):
                    continue

                # Accept good careers pages / ATS pages
                if any(keyword in url for keyword in good_keywords):
                    careers_url = result["href"]
                    print(f"      ✓ {careers_url}")
                    break

            if careers_url:
                break

        df.at[index, "Careers Page"] = careers_url

# ------------------------------------
# Save
# ------------------------------------

df.to_excel(
    "output/GSV_150_with_careers.xlsx",
    index=False
)

print("\nFinished!")