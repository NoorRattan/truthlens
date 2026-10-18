import asyncio
from unittest.mock import patch

from pipeline import web_searcher


def test_ddgs_results_keep_the_api_source_schema():
    with patch.object(web_searcher, "DDGS") as client:
        client.return_value.__enter__.return_value.text.return_value = [
            {"title": "Source", "href": "https://example.org/article", "body": "Evidence"}
        ]
        result = web_searcher.search_claim_ddg("A claim")
    assert result == {
        "claim": "A claim",
        "results": [{"title": "Source", "url": "https://example.org/article", "snippet": "Evidence"}],
    }


def test_ddgs_failure_returns_an_empty_result():
    with patch.object(web_searcher, "DDGS", side_effect=RuntimeError("provider unavailable")):
        assert web_searcher.search_claim_ddg("A claim") == {"claim": "A claim", "results": []}


def test_empty_claims_do_not_contact_a_search_provider():
    with patch.object(web_searcher, "DDGS") as client:
        assert asyncio.run(web_searcher.search_claims([])) == {"corroboration_results": []}
    client.assert_not_called()
