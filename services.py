def build_query(url):
    # Build query based on contents of query_params.
    sql = """SELECT o.id, o.metal_id, o.size_id, o.style_id, o.timestamp"""

    if "metal" in url["query_params"]["_expand"]:
        sql += ", m.id metalId, m.metal, m.price metalPrice"
    if "size" in url["query_params"]["_expand"]:
        sql += ", sz.id sizeId, sz.carets, sz.price sizePrice"
    if "style" in url["query_params"]["_expand"]:
        sql += ", st.id styleId, st.style, st.price stylePrice"

    sql += " FROM Orders o"

    if "metal" in url["query_params"]["_expand"]:
        sql += " JOIN Metals m ON m.id = o.metal_id"
    if "size" in url["query_params"]["_expand"]:
        sql += " JOIN Sizes sz ON sz.id = o.size_id"
    if "style" in url["query_params"]["_expand"]:
        sql += " JOIN Styles st ON st.id = o.style_id"

    if url["pk"] != 0:
        sql += " WHERE o.id = ?"
    else:
        sql += " ORDER BY o.id"

    return sql


def expand_order(query_params, query_results):
    # Assign the contents of the "order" object to a variable named "expanded order"
    expanded_order = {
        "id": query_results["id"],
        "metal_id": query_results["metal_id"],
        "size_id": query_results["size_id"],
        "style_id": query_results["style_id"],
        "timestamp": query_results["timestamp"]
    }

    # Create empty objects for metal, size, and style.
    metal = {}
    size = {}
    style = {}

    # If ["query_params"] contains "metal", add metal keys/values to "metal" object.
    if "metal" in query_params["_expand"]:
        metal["id"] = query_results["metalId"]
        metal["metal"] = query_results["metal"]
        metal["price"] = query_results["metalPrice"]
        expanded_order["metal"] = metal

    # If ["query_params"] contains "size", add metal keys/values to "size" object.
    if "size" in query_params["_expand"]:
        size["id"] = query_results["sizeId"]
        size["carets"] = query_results["carets"]
        size["price"] = query_results["sizePrice"]
        expanded_order["size"] = size

    # If ["query_params"] contains "style", add metal keys/values to "style" object.
    if "style" in query_params["_expand"]:
        style["id"] = query_results["styleId"]
        style["style"] = query_results["style"]
        style["price"] = query_results["stylePrice"]
        expanded_order["style"] = style

    return expanded_order
