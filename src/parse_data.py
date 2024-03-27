from database import (category, language, country, country_language,
                      subdivision, subdivision_country, channel,
                      channel_language, channel_category, blocklist,
                      stream)

if __name__ == "__main__":
    # loading data to mysql database
    category.load()
    language.load()
    country.load()
    country_language.load()
    subdivision.load()
    subdivision_country.load()
    channel.load()
    channel_language.load()
    channel_category.load()
    blocklist.load()
    stream.load()
