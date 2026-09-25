# Item Group Series

Custom Frappe app for ERPNext to dynamically set Item `naming_series` based on the selected `Item Group`.

## Features
- **Dynamic Naming Series per Item Group**: Easily configure naming series directly on each `Item Group` document.
- **No Hardcoded Client Scripts**: When adding a new Item Group, just set its Naming Series in ERPNext Desk without code changes.
- **Dual-Layer Guarantee**:
  - **Desk UI**: Instant auto-fill of `naming_series` when an Item Group is selected on the Item form.
  - **Server-Side Hook**: Guarantees naming series is populated even on CSV/Excel Data Import or API requests.
- **Fallback**: Defaults to `ITEM.YY..####.` if no series is configured on the Item Group.

## License
MIT
