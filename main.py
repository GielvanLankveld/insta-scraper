from instagram import Instagram
from settings.settings import Settings

settings = Settings()
instagram = Instagram(settings.get_api_token)
instagram.scrape_profile()