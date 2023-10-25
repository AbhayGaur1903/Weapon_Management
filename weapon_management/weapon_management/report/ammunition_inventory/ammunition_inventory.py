# Copyright (c) 2023, Expedien and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    # Define the columns
    columns = ["Ammunition Name", "No.of Ammunition"]

    # Initialize an empty data list
    data = []

    # Extract filters from the filters object
    filters_dict = frappe._dict(filters)

    # # Use frappe.msgprint to check the filter values
    # frappe.msgprint(f"Filters received: {filters_dict}")

    # Write your custom SQL query to retrieve data
    query = """
		select 
		tacm.ammunition_category as "Ammunition Name",
		count(taid.ammunition_category) as "No.of Ammunition"
		from "tabAmmunition In Details" taid 
		inner join "tabUnit Master" tum  on taid.unit_location  = tum.name
		inner join "tabAmmunition Category Master" tacm on taid.ammunition_category = tacm.name
		
    """

    # Construct the WHERE clause based on filters
    where_clause = "WHERE 1=1"  # Always true condition to start

    if filters_dict.get("unit"):
        where_clause += f" AND tum.name = %(unit)s"
        
    if filters_dict.get("ammunition_name"):
        where_clause += f" AND tacm.name = %(ammunition_name)s"


    # Add the WHERE clause to the query
    query += where_clause

    query += "GROUP BY tacm.ammunition_category  ;"

    # Execute the SQL query
    result = frappe.db.sql(query, filters_dict, as_dict=True)

    # Populate data based on the query results
    for row in result:
        data_row = [row.get("Ammunition Name"), row.get("No.of Ammunition")]
        data.append(data_row)

    return columns, data
