import httpx

API_URL = "http://www.utic.go.kr/guide/tsdmsOpenData.do"

params = {
    "key": "otI8zeD2J6SuHmddUPKmVn6ZpqSKbVs9waJXBGILC9A"
}

response = httpx.get(
    API_URL,
    params=params
)

print(response.status_code)
print(response.text)