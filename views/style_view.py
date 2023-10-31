import json
from nss_handler import status
from repository import db_get_single, db_get_all


class StylesView():

    def get(self, handler, url):
        if url["pk"] > 0:
            sql = """
            SELECT
                s.id,
                s.style,
                s.price
            FROM Styles s
            WHERE s.id = ?
            """
            query_results = db_get_single(sql, url["pk"])
            serialized_styles = json.dumps(dict(query_results))

        else:
            query_results = db_get_all(
                "SELECT id, style, price FROM Styles"
            )
            styles = [dict(row) for row in query_results]
            serialized_styles = json.dumps(styles)

        return handler.response(serialized_styles, status.HTTP_200_SUCCESS)

    def create(self, handler, style_data):
        return handler.response("This action cannot be completed because it is unsupported.", status.HTTP_405_UNSUPPORTED_METHOD)

    def delete(self, handler, pk):
        return handler.response("This action cannot be completed because it is unsupported.", status.HTTP_405_UNSUPPORTED_METHOD)

    def update(self, handler, style_data, pk):
        return handler.response("This action cannot be completed because it is unsupported.", status.HTTP_405_UNSUPPORTED_METHOD)
