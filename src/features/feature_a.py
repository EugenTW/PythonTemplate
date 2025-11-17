import requests

def fetch_data(url: str):
    """簡單功能：從指定 URL 抓取資料"""
    response = requests.get(url)
    return response.text[:200]  # 只取前 200 字元
