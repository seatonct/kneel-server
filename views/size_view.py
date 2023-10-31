import json
from nss_handler import status
from repository import db_get_single, db_get_all


class SizesView():

    def get(self, handler, url):
        if url["pk"] > 0:
            sql = """
            SELECT
                s.id,
                s.carets,
                s.price
            FROM Sizes s
            WHERE s.id = ?
            """
            query_results = db_get_single(sql, url["pk"])
            serialized_sizes = json.dumps(dict(query_results))

        else:
            query_results = db_get_all(
                "SELECT id, carets, price FROM Sizes"
            )
            metals = [dict(row) for row in query_results]
            serialized_sizes = json.dumps(metals)

        return handler.response(serialized_sizes, status.HTTP_200_SUCCESS)

    def create(self, handler, size_data):
        return handler.response("This action cannot be completed because it is unsupported.", status.HTTP_405_UNSUPPORTED_METHOD)

    def delete(self, handler, pk):
        return handler.response("This action cannot be completed because it is unsupported.", status.HTTP_405_UNSUPPORTED_METHOD)

    def update(self, handler, size_data, pk):
        return handler.response("This action cannot be completed because it is unsupported.", status.HTTP_405_UNSUPPORTED_METHOD)
