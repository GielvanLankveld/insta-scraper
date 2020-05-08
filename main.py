from instagram import Instagram
from settings.settings import Settings

settings = Settings()
instagram = Instagram(settings.get_api_token())
result = instagram.scrape_profile('https://graph.instagram.com/me/media', [])
print(result)