// Copyright (c) 2026, Rajesh Vishwakarma and contributors
// For license information, please see license.txt

frappe.query_reports["Form 16 Quaterly"] = {
    filters: [
        {
            fieldname: "company",
            label: "Company",
            fieldtype: "Link",
            options: "Company",
            reqd: 1
        },
        {
            fieldname: "year",
            label: "Financial Year Start",
            fieldtype: "Int",
            default: 2025,
            reqd: 1
        },
        {
            fieldname: "quarter",
            label: "Quarter",
            fieldtype: "Select",
            options: [
                "",
                "Q1 (Apr-Jun)",
                "Q2 (Jul-Sep)",
                "Q3 (Oct-Dec)",
                "Q4 (Jan-Mar)"
            ]
        }
    ],
    show_filters: false
};