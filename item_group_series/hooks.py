app_name = "item_group_series"
app_title = "Item Group Series"
app_publisher = "Muhammad Yusuf Tri Daryanto"
app_description = "Automatically select Item naming series based on Item Group in ERPNext"
app_email = "114971841+Muhayustrid@users.noreply.github.com"
app_license = "mit"

# Includes in <head>
# ------------------

# include js in doctype views
doctype_js = {
	"Item": "public/js/item_form.js"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item": {
		"before_insert": "item_group_series.overrides.item.set_naming_series"
	}
}

# Fixtures
# --------
fixtures = [
	{
		"dt": "Custom Field",
		"filters": [
			["name", "in", ["Item Group-custom_naming_series"]]
		]
	}
]

# Migration
# ---------
after_migrate = "item_group_series.patches.v1_0.seed_item_group_series.execute"

