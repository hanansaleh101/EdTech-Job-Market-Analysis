import pandas as pd

# ----------------------------
# Read Excel
# ----------------------------

df = pd.read_excel(
    "output/GSV_150_with_careers.xlsx",
    dtype=str
)

df = df.fillna("")

# ----------------------------
# Detect ATS
# ----------------------------

for index, row in df.iterrows():

    url = row["Careers Page"].lower()

    ats = ""

    if "greenhouse" in url or "job-boards.greenhouse.io" in url:
        ats = "Greenhouse"

    elif "lever" in url:
        ats = "Lever"

    elif "ashby" in url:
        ats = "Ashby"

    elif "workable" in url or "apply.workable.com" in url:
        ats = "Workable"

    elif "teamtailor" in url:
        ats = "Teamtailor"

    elif "smartrecruiters" in url:
        ats = "SmartRecruiters"

    elif "freshteam" in url:
        ats = "Freshteam"

    elif "bamboohr" in url:
        ats = "BambooHR"

    elif "icims" in url:
        ats = "iCIMS"

    elif "myworkdayjobs" in url or "workday" in url:
        ats = "Workday"

    elif "jobvite" in url:
        ats = "Jobvite"

    elif "oraclecloud" in url:
        ats = "Oracle Recruiting"

    elif "careers." in url or "/careers" in url or "/jobs" in url:
        ats = "Company Website"

    else:
        ats = "Unknown"

    df.at[index, "ATS"] = ats

# ----------------------------
# Save
# ----------------------------

df.to_excel(
    "output/GSV_150_with_ats.xlsx",
    index=False
)

print("Finished!")