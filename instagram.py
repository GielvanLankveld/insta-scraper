class Instagram():
    def __init__(self, api_key):
        self.api_key = api_key
        self.GOOD_STRING = '\033[92m✔\033[0m'
        self.BAD_STRING = '\033[92m❌\033[0m'

    def scrape_profile(self):
        print(f'{self.GOOD_STRING} Started crawling Instagram..')
        