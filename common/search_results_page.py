from common.api_client import ApiClient


class SearchResultsPage:
    def __init__(self, client):
        self.client = client

    def search_films(self, keyword, page):
        response = self.client.send_request(keyword=keyword, page=page)
        return response.json()

    def count_films(self, results):
        return len(results.get('films', []))

    def total_pages(self, results):
        return results.get('totalPages', 0)

    def current_page(self, results):
        return results.get('currentPage', 0)
