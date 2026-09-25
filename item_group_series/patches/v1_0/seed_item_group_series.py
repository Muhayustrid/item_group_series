import frappe

SERIES_MAP = {
	"ATK": "ATK.YY..####.",
	"Bahan Baku": "BB.YY..####.",
	"Barang Habis Pakai": "BHP.YY..####.",
	"Peralatan": "PER.YY..####.",
	"Perlengkapan": "PEL.YY..####.",
	"Produk Jadi": "PJ.YY..####.",
	"Seragam": "SG.YY..####.",
	"Ropi Fancy": "RP.YY..###.",
	"Gempi": "GM.YY..###.",
	"Pastry": "CR.YY..###.",
	"Black Coffee": "BC.YY..###.",
	"Cappucino": "CP.YY..###.",
	"Chocolate": "CK.YY..###.",
	"Jasmine Tea": "JT.YY..###.",
	"Tradisional": "TR.YY..###.",
	"Air Mineral": "AM.YY..###.",
	"Paper Packaging": "PG.YY..###.",
	"Elektronik": "ETC.YY.-.###.",
	"Non Elektronik": "NETC.YY.-.###.",
	"Paket": "PAKET.YY.-.###.",
	"Add-on": "ADD.YY.-.###.",
	"ITEM": "ITEM.YY.-.####.",
}


def execute():
	"""Seed existing Item Groups with their corresponding default naming series."""
	if not frappe.db.has_column("Item Group", "custom_naming_series"):
		return

	for item_group, series in SERIES_MAP.items():
		if frappe.db.exists("Item Group", item_group):
			current = frappe.db.get_value("Item Group", item_group, "custom_naming_series")
			if not current:
				frappe.db.set_value("Item Group", item_group, "custom_naming_series", series)
