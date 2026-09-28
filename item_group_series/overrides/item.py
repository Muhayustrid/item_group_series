import frappe
from frappe.model.naming import get_default_naming_series

DEFAULT_SERIES = "ITEM.YY..####."


def set_naming_series(doc, method=None):
	"""Set doc.naming_series based on Item Group before insert.

	Ensures that items created via Data Import, API, or desk follow
	the naming series configured in Item Group.
	"""
	if not doc.item_group:
		return

	group_series = frappe.db.get_value("Item Group", doc.item_group, "custom_naming_series")
	target_series = group_series or DEFAULT_SERIES

	field_meta = frappe.get_meta("Item").get_field("naming_series")
	# The framework prefills naming_series with its own default (field default
	# property or first option) at insert; treat all of those as "not chosen".
	# An explicitly chosen series is respected.
	replaceable = {
		"",
		(field_meta and field_meta.default) or "",
		get_default_naming_series("Item") or "",
		DEFAULT_SERIES,
	}
	if (doc.naming_series or "") in replaceable:
		doc.naming_series = target_series
