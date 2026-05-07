import json

def validate_invoice(data_str):
    try:
        data = json.loads(data_str)

        errors = []
        if not data.get("invoice_number"):
            errors.append("Missing invoice number")

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "data": data
        }

    except:
        return {"valid": False, "errors": ["Invalid JSON"], "data": {}}