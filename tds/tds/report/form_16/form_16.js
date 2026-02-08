// Copyright (c) 2026, Rajesh Vishwakarma and contributors
// For license information, please see license.txt

frappe.query_reports["Form 16"] = {
    "filters": [
        {
            "fieldname": "view_type",
            "label": __("View Type"),
            "fieldtype": "Select",
            "options": ["Monthly", "Quarterly"],
            "default": "Monthly",
            "reqd": 1,
            "on_change": function() {
                frappe.query_report.refresh();
            }
        },
        {
            "fieldname": "company",
            "label": __("Company"),
            "fieldtype": "Link",
            "options": "Company",
            "reqd": 1,
            "default": frappe.defaults.get_user_default("Company")
        },
        {
            "fieldname": "year",
            "label": __("Year"),
            "fieldtype": "Int",
            "default": new Date().getFullYear(),
            "depends_on": "eval:doc.view_type=='Monthly'",
            "mandatory_depends_on": "eval:doc.view_type=='Monthly'"
        },
        {
            "fieldname": "month",
            "label": __("Month"),
            "fieldtype": "Select",
            "options": [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ],
            "default": ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"][new Date().getMonth()],
            "depends_on": "eval:doc.view_type=='Monthly'",
            "mandatory_depends_on": "eval:doc.view_type=='Monthly'"
        },
        {
            "fieldname": "financial_year",
            "label": __("Financial Year"),
            "fieldtype": "Link",
            "options": "Fiscal Year",
            "depends_on": "eval:doc.view_type=='Quarterly'",
            "mandatory_depends_on": "eval:doc.view_type=='Quarterly'"
        },
        {
            "fieldname": "quarter",
            "label": __("Quarter"),
            "fieldtype": "Select",
            "options": [
                "Q1 (Apr-Jun)",
                "Q2 (Jul-Sep)",
                "Q3 (Oct-Dec)",
                "Q4 (Jan-Mar)"
            ],
            "depends_on": "eval:doc.view_type=='Quarterly'",
            "mandatory_depends_on": "eval:doc.view_type=='Quarterly'"
        }
    ]
};