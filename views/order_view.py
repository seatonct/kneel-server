import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_create
from services import build_query, expand_order


class OrdersView():

    def create(self, handler, order_data):
        sql = """
            INSERT INTO Orders (metal_id, size_id, style_id) VALUES (?, ?, ?)"""

        order_id = db_create(
            sql, (order_data["metal_id"], order_data["size_id"], order_data["style_id"]))

        order = {
            "id": order_id,
            "metal_id": order_data['metal_id'],
            "size_id": order_data['size_id'],
            "style_id": order_data['style_id']
        }

        response_body = json.dumps(order)
        return handler.response(response_body, status.HTTP_201_SUCCESS_CREATED)

    def get(self, handler, url):
        if url["pk"] != 0:
            if "_expand" in url["query_params"]:
                sql = build_query(url)
                query_results = db_get_single(sql, url["pk"])

                order = expand_order(url["query_params"], query_results)
            else:
                sql = "SELECT id, metal_id, size_id, style_id, timestamp FROM Orders WHERE id = ?"
                order = db_get_single(sql, url["pk"])
            serialized_order = json.dumps(dict(order))

            return handler.response(serialized_order, status.HTTP_200_SUCCESS)
        else:
            if "_expand" in url["query_params"]:
                sql = build_query(url)
                query_results = db_get_all(sql)
                orders = [expand_order(url["query_params"], query_results)
                          for row in query_results]
            else:
                sql = "SELECT id, metal_id, size_id, style_id, timestamp FROM Orders"
                query_results = db_get_all(sql)
                orders = [dict(row) for row in query_results]
            serialized_orders = json.dumps(orders)

            return handler.response(serialized_orders, status.HTTP_200_SUCCESS)

    def delete(self, handler, pk):
        number_of_rows_deleted = db_delete(
            "DELETE FROM Orders WHERE id = ?", pk)

        if number_of_rows_deleted > 0:
            return handler.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY)
        return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND)

    def update(self, handler, order_data, pk):
        return handler.response("Action not allowed", status.HTTP_405_UNSUPPORTED_METHOD)
