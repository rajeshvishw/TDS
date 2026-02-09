import frappe

def execute(filters=None):
    filters = filters or {}
    return get_columns(), get_data(filters)

def get_columns():
    return [
        {
            "fieldname": "employee",
            "label": "Employee",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 150
        },
        {
            "fieldname": "pan_no",
            "label": "PAN No",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "fieldname": "tds_amount",
            "label": "Total TDS",
            "fieldtype": "Currency",
            "width": 150
        }
    ]

def get_data(filters):
    company = filters.get("company")
    year = filters.get("year")
    quarter = filters.get("quarter") or None
    if not company or not year:
        return []
    year = int(year)

    # Default = Full FY
    from_date = f"{year}-04-01"
    to_date   = f"{year + 1}-03-31"
    if quarter == "Q1 (Apr-Jun)":
        from_date, to_date = f"{year}-04-01", f"{year}-06-30"
    elif quarter == "Q2 (Jul-Sep)":
        from_date, to_date = f"{year}-07-01", f"{year}-09-30"
    elif quarter == "Q3 (Oct-Dec)":
        from_date, to_date = f"{year}-10-01", f"{year}-12-31"
    elif quarter == "Q4 (Jan-Mar)":
        from_date, to_date = f"{year + 1}-01-01", f"{year + 1}-03-31"

    records = frappe.get_all(
        "TDS Liability",
        filters={
            "company": company,
            "date_of_tax_deducted": ["between", [from_date, to_date]]
        },
        fields=["employee", "pan_no", "tds_amount"]
    )

    result = {}
    for row in records:
        key = (row.employee, row.pan_no)
        if key not in result:
            result[key] = {
                "employee": row.employee,
                "pan_no": row.pan_no,
                "tds_amount": 0.0,
            }
        result[key]["tds_amount"] += float(row.tds_amount or 0)
    return list(result.values())