# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

def execute():
	for d in frappe.db.sql("""select name from `tabAccount`
		where ifnull(master_type, '') not in ('Customer', 'Supplier', 'Employee', '')"""):
			ac = frappe.get_doc("Account", d[0])
			ac.master_type = None
			ac.save()
