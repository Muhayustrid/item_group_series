import frappe
from frappe.tests import IntegrationTestCase
from item_group_series.overrides.item import DEFAULT_SERIES, set_naming_series


class TestItemGroupSeries(IntegrationTestCase):
	def test_naming_series_assigned_from_item_group(self):
		item = frappe.new_doc("Item")
		item.item_code = "_Test Item Bahan Baku"
		item.item_name = "_Test Item Bahan Baku"
		item.item_group = "Bahan Baku"
		item.stock_uom = "Nos"
		set_naming_series(item)
		self.assertEqual(item.naming_series, "BB.YY..####.")

	def test_fallback_naming_series_for_unset_group(self):
		group_name = "_Test Group No Series"
		if not frappe.db.exists("Item Group", group_name):
			frappe.get_doc({
				"doctype": "Item Group",
				"item_group_name": group_name,
				"parent_item_group": "All Item Groups",
				"is_group": 0,
			}).insert(ignore_permissions=True)

		item = frappe.new_doc("Item")
		item.item_code = "_Test Item Fallback"
		item.item_name = "_Test Item Fallback"
		item.item_group = group_name
		item.stock_uom = "Nos"
		set_naming_series(item)
		self.assertEqual(item.naming_series, DEFAULT_SERIES)

	def test_e2e_insert_with_item_group_series(self):
		# Test actual document insertion and name generation
		item = frappe.get_doc({
			"doctype": "Item",
			"item_name": "_Test E2E Bahan Baku Item",
			"item_group": "Bahan Baku",
			"stock_uom": "Nos",
		}).insert(ignore_permissions=True)

		self.assertEqual(item.naming_series, "BB.YY..####.")
		self.assertTrue(item.name.startswith("BB26") or "BB" in item.name)

		# Test dynamic new item group
		dynamic_group = "_Test Group Dynamic Series"
		if not frappe.db.exists("Item Group", dynamic_group):
			frappe.get_doc({
				"doctype": "Item Group",
				"item_group_name": dynamic_group,
				"parent_item_group": "All Item Groups",
				"is_group": 0,
				"custom_naming_series": "DYN.YY..####.",
			}).insert(ignore_permissions=True)

		item_dyn = frappe.get_doc({
			"doctype": "Item",
			"item_name": "_Test E2E Dynamic Item",
			"item_group": dynamic_group,
			"stock_uom": "Nos",
		}).insert(ignore_permissions=True)

		self.assertEqual(item_dyn.naming_series, "DYN.YY..####.")
		self.assertTrue(item_dyn.name.startswith("DYN26") or "DYN" in item_dyn.name)
