def fetch_seo_data(keyword):
    mock_data = {
        "wireless earbuds": {"search_volume": 54000, "keyword_difficulty": 36, "avg_cpc": 1.20},
        "ai writing tool": {"search_volume": 22000, "keyword_difficulty": 42, "avg_cpc": 2.50},
    }
    return mock_data.get(keyword.lower(), {
        "search_volume": 1000,
        "keyword_difficulty": 25,
        "avg_cpc": 0.50
    })
