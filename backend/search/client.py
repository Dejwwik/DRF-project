from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client


def perform_search(query, index_name="Product", **kwargs):
    client = get_client()
    # params = {"contentFilter": query}
    params = {"query": query}
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags):
            params["tagFilters"] = tags

    index_filters = [f"{k}:{v}" for k, v in kwargs.items()]
    if index_filters:
        params["facetFilters"] = index_filters
    results = client.search_single_index(index_name, params)
    return results
