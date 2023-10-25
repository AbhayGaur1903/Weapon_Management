import frappe

def execute(filters=None):
    # Define the columns
    columns = ["Weapon", "No Of Weapon"]

    # Initialize an empty data list
    data = []

    # Extract filters from the filters object
    filters_dict = frappe._dict(filters)

    # Write your custom SQL query to retrieve data
    query = """
        SELECT 
            twcm.weapon_category as "Weapon",
            COUNT(twid.weapon_name) AS "No Of Weapon"
        FROM "tabWeapon In Details" twid
        INNER JOIN "tabUnit Master" tum ON twid.unit_location = tum.name
        INNER JOIN "tabWeapon Category Master" twcm ON twid.weapon_category = twcm.name
    """

    # Construct the WHERE clause based on filters
    where_clause = "WHERE 1=1"  # Always true condition to start

    if filters_dict.get("unit"):
        where_clause += f" AND tum.name = %(unit)s"
    
    if filters_dict.get("weapon"):
        where_clause += f" AND twcm.name = %(weapon)s"

    # Add the WHERE clause to the query
    query += where_clause

    query += " GROUP BY twcm.weapon_category;"

    # Execute the SQL query
    result = frappe.db.sql(query, filters_dict, as_dict=True)

    # Populate data based on the query results
    for row in result:
        data_row = [row.get("Weapon"), row.get("No Of Weapon")]
        data.append(data_row)

    return columns, data
