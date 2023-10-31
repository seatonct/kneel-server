import json
from nss_handler import status
from repository import db_get_single, db_get_all


class MetalsView():

    def get(self, handler, url):
        if url["pk"] > 0:
            sql = """
            SELECT
                m.id,
                m.metal,
                m.price
            FROM Metals m
            WHERE m.id = ?
            """
            query_results = db_get_single(sql, url["pk"])
            serialized_metals = json.dumps(dict(query_results))

        else:
            query_results = db_get_all(
                "SELECT id, metal, price FROM Metals"
            )
            metals = [dict(row) for row in query_results]
            serialized_metals = json.dumps(metals)

        return handler.response(serialized_metals, status.HTTP_200_SUCCESS)

    def create(self, handler, metal_data):
        return handler.response("This action cannot be completed because it is unsupported.", status.HTTP_405_UNSUPPORTED_METHOD)

    def delete(self, handler, pk):
        return handler.response("This action cannot be completed because it is unsupported.", status.HTTP_405_UNSUPPORTED_METHOD)

    def update(self, handler, metal_data, pk):
        return handler.response("This action cannot be completed because it is unsupported.", status.HTTP_405_UNSUPPORTED_METHOD)
