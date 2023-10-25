frappe.pages['weapon-distribution-report'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Weapon Distribution Report',
		single_column: true
	});
	
	let field = page.add_field({
		label: 'Weapon Category',
		fieldtype: 'Link',
		fieldname: 'weapon_category',
		options: 'Weapon Category Master',
		change() {
			console.log(field.get_value());
		}
	});

	let datarangeField = page.add_field({
		label: 'Date Range',
		fieldtype: 'Date Range',
		fieldname: 'date_range'
	});

	var tableContainer = $('<div></div>').appendTo(page.main);
	var table = createModernTable(tableContainer);

	// You can add code here to populate the table with data
};

function createModernTable(container) {
	let table = $('<table class="modern-table"></table>').appendTo(container);
	table.css('margin-top', '14px');
	let thead = $('<thead></thead>').appendTo(table);
	$('<tr><th style="text-align: center;">Weapon Name</th><th style="text-align: center;">Unit</th></tr>').appendTo(thead);

	$('<tbody></tbody>').appendTo(table);
	return table;
}



