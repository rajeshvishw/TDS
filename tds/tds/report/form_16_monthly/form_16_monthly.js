// Copyright (c) 2026, Rajesh Vishwakarma and contributors
// For license information, please see license.txt

// Copyright (c) 2026, Rajesh Vishwakarma and contributors
// For license information, please see license.txt

frappe.query_reports["Form 16 Monthly"] = {
    "filters": [
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
            "reqd": 1
        },
        {
            "fieldname": "month",
            "label": __("Month"),
            "fieldtype": "Select",
            "options": [
                "",
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ],
            "default": ""
        }
    ]
};