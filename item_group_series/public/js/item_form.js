frappe.ui.form.on('Item', {
    refresh: function(frm) {
        if (frm.is_new() && frm.doc.item_group) {
            const field_default = (frm.fields_dict.naming_series && frm.fields_dict.naming_series.df.default) || '';
            if (!frm.doc.naming_series || frm.doc.naming_series === field_default) {
                frm.trigger('item_group');
            }
        }
    },

    item_group: function(frm) {
        if (!frm.is_new() || !frm.doc.item_group) return;

        frappe.db.get_value('Item Group', frm.doc.item_group, 'custom_naming_series')
            .then(function(r) {
                const default_series = "ITEM.YY..####.";
                const series = (r && r.message && r.message.custom_naming_series) ? r.message.custom_naming_series : default_series;

                if (frm.fields_dict.naming_series) {
                    let options = (frm.fields_dict.naming_series.df.options || '').split('\n').filter(Boolean);
                    if (series && !options.includes(series)) {
                        options.push(series);
                        frm.set_df_property('naming_series', 'options', options.join('\n'));
                    }
                }

                frm.set_value('naming_series', series);
            });
    }
});
