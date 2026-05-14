def prepare_ewaybill_json(self, picking):
    """
    This function converts the Odoo Delivery Order (picking)
    into the JSON format required by the GST portal.
    """
    # 1. Get the company (sender) and partner (receiver)
    company = picking.company_id
    partner = picking.partner_id

    # 2. Build the basic structure
    data = {
        "supplyType": "O",  # 'O' for Outward
        "subSupplyType": "1",  # '1' for Supply
        "docType": "CHL",  # 'CHL' for Delivery Challan
        "docNo": picking.name,
        "docDate": picking.date_done.strftime("%d/%m/%Y") if picking.date_done else picking.scheduled_date.strftime(
            "%d/%m/%Y"),
        "fromGstin": company.vat or "",
        "fromTrdName": company.name,
        "toGstin": partner.vat or "URP",  # 'URP' means Unregistered Person
        "toTrdName": partner.name,
        "transDistance": str(picking.l10n_in_distance),
        "transMode": picking.l10n_in_mode,
        "vehicleNo": picking.l10n_in_vehicle_no,
        "itemList": []
    }

    # 3. Loop through the products in the delivery
    for move in picking.move_ids:
        item_data = {
            "productName": move.product_id.display_name,
            "hsnCode": move.product_id.l10n_in_hsn_code or "0000",
            "quantity": move.product_uom_qty,
            "qtyUnit": "NOS",  # Units
            "taxableAmount": move.product_id.standard_price * move.product_uom_qty,  # Simplified
        }
        data["itemList"].append(item_data)

    return data