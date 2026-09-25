import frappe

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
	field_default = (field_meta and field_meta.default) or ""

	# If naming series is not set, or is the static field default, or doesn't match group series
	if not doc.naming_series or doc.naming_series == field_default:
		doc.naming_series = target_series
	elif group_series and doc.naming_series != group_series:
		# If group has explicit series and current series is default fallback, adopt group series
		if doc.naming_series == DEFAULT_SERIES:
			doc.naming_series = group_series
