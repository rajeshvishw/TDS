# Copyright (c) 2026, Rajesh Vishwakarma and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

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
            "fieldname": "date_of_tax_deducted",
            "label": "Date of Tax Deduction",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "fieldname": "tds_amount",
            "label": "TDS Amount",
            "fieldtype": "Currency",
            "width": 120
        }
    ]

def get_data(filters):
    company = filters.get("company")
    year = filters.get("year")
    month_name = filters.get("month")
    
    if not company or not year:
        frappe.msgprint("Please select Company and Year")
        return []
    
    conditions = """
        tl.company = %s
        AND YEAR(tl.date_of_tax_deducted) = %s
    """
    
    values = [company, year]
    
    # Agar month select hai to us month ka data dikhao, nahi to sare months ka data dikhao
    if month_name:
        month_map = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }
        month_no = month_map.get(month_name)
        conditions += " AND MONTH(tl.date_of_tax_deducted) = %s"
        values.append(month_no)
    
    query = f"""
        SELECT
            tl.employee,
            tl.pan_no,
            tl.date_of_tax_deducted,
            SUM(tl.tds_amount) AS tds_amount
        FROM `tabTDS Liability` tl
        WHERE {conditions}
        GROUP BY tl.employee, tl.pan_no, tl.date_of_tax_deducted
        ORDER BY tl.date_of_tax_deducted, tl.employee
    """
    
    return frappe.db.sql(query, tuple(values), as_dict=1)