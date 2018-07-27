# TracResfulApi

This is a python Restful Api which analyses data for policies and procedures within an organization and creates a data summary for each department in a JSON format.

Sample endpoints and related data are shown

Endpoint: http://127.0.0.1:8000/sbuset/

{
    "corporate": {
        "approved": 2,
        "unapproved": 3,
        "expired_yes": 3,
        "expired_no": 2,
        "reg_yes": 5,
        "reg_no": 0,
        "freq_daily": 0,
        "freq_weekly": 0,
        "freq_monthly": 5,
        "freq_annually": 0
    },
    "retail": {
        "approved": 2,
        "unapproved": 3,
        "expired_yes": 3,
        "expired_no": 2,
        "reg_yes": 5,
        "reg_no": 0,
        "freq_daily": 0,
        "freq_weekly": 0,
        "freq_monthly": 0,
        "freq_annually": 5
    },
    "treasury": {
        "approved": 1,
        "unapproved": 4,
        "expired_yes": 4,
        "expired_no": 1,
        "reg_yes": 5,
        "reg_no": 0,
        "freq_daily": 5,
        "freq_weekly": 0,
        "freq_monthly": 0,
        "freq_annually": 0
    },
    "financial": {
        "approved": 2,
        "unapproved": 3,
        "expired_yes": 3,
        "expired_no": 2,
        "reg_yes": 4,
        "reg_no": 1,
        "freq_daily": 0,
        "freq_weekly": 0,
        "freq_monthly": 0,
        "freq_annually": 5
    },
    "operations": {
        "approved": 3,
        "unapproved": 2,
        "expired_yes": 2,
        "expired_no": 3,
        "reg_yes": 5,
        "reg_no": 0,
        "freq_daily": 0,
        "freq_weekly": 0,
        "freq_monthly": 5,
        "freq_annually": 0
    },
    "humanResources": {
        "approved": 3,
        "unapproved": 2,
        "expired_yes": 2,
        "expired_no": 3,
        "reg_yes": 5,
        "reg_no": 0,
        "freq_daily": 0,
        "freq_weekly": 0,
        "freq_monthly": 0,
        "freq_annually": 5
    },
    "investments": {
        "approved": 3,
        "unapproved": 2,
        "expired_yes": 2,
        "expired_no": 3,
        "reg_yes": 5,
        "reg_no": 0,
        "freq_daily": 5,
        "freq_weekly": 0,
        "freq_monthly": 0,
        "freq_annually": 0
    },
    "rmc": {
        "approved": 3,
        "unapproved": 2,
        "expired_yes": 2,
        "expired_no": 3,
        "reg_yes": 5,
        "reg_no": 0,
        "freq_daily": 0,
        "freq_weekly": 0,
        "freq_monthly": 0,
        "freq_annually": 5
    },
    "accounts": {
        "approved": 2,
        "unapproved": 3,
        "expired_yes": 3,
        "expired_no": 2,
        "reg_yes": 4,
        "reg_no": 1,
        "freq_daily": 5,
        "freq_weekly": 0,
        "freq_monthly": 0,
        "freq_annually": 0
    },
    "infotech": {
        "approved": 2,
        "unapproved": 3,
        "expired_yes": 3,
        "expired_no": 2,
        "reg_yes": 4,
        "reg_no": 1,
        "freq_daily": 0,
        "freq_weekly": 5,
        "freq_monthly": 0,
        "freq_annually": 0
    }
}

Endpoint: http://127.0.0.1:8000/tracentries/policy/retail/approved/

[
    {
        "serial": "1",
        "description": "Policy1",
        "sbu": "Retail",
        "scope": "Provision",
        "reviewFrequency": "Annually",
        "lastReviewDate": "19-Oct-16",
        "nextReviewDate": "20-Oct-18",
        "days": "340",
        "expired": "No",
        "regulatory": "Yes",
        "approved": "Approved",
        "responsibility": "Retail Head",
        "note": "Update required"
    },
    {
        "serial": "41",
        "description": "Policy41",
        "sbu": "Retail",
        "scope": "Provision4",
        "reviewFrequency": "Annually",
        "lastReviewDate": "10-Dec-15",
        "nextReviewDate": "29-May-18",
        "days": "196",
        "expired": "No",
        "regulatory": "Yes",
        "approved": "Approved",
        "responsibility": "Retail Head",
        "note": "nan"
    }
]
