import scrapy
class Graphics_Cards_scraper(scrapy.Spider):
    name = "cardsscraper"
    start_urls = ["https://www.techradar.com/news/computing-components/graphics-cards/best-graphics-cards-1291458"]

    def parse(self, response):
        all_cards = response.xpath("//div[@class='product prog-buying-guide']")
        with open('Cards_details.txt', 'w') as file:
            for card in all_cards:
                name_of_card = card.xpath(".//h3[@class='product__title']").xpath(".//a/text()").get()
                file.write(name_of_card + '\n')
                product_summary = card.xpath(".//div[@class='product-summary spec']")
                file.write(product_summary.xpath(".//h4/text()").get() + ":" + '\n')
                product_summary_container = product_summary.xpath(".//div[@class='product-summary__container']/div[@class='spec__entry']")
                for detail in product_summary_container:
                    name =  detail.xpath(".//span[@class='spec__name']/text()").get()
                    value = detail.xpath(".//span[@class='spec_value']/text()").get()
                    file.write("{} {}".format(name, value) + '\n')
                pros = card.xpath(".//div[@class='product-summary pros']")
                for data in pros:
                    file.write(data.xpath(".//h4/text()").get() + ":" + '\n')
                    productSummaryContainer = data.xpath(".//div[@class='product-summary__container']")
                    for item in productSummaryContainer.xpath(".//span[@class='_hawk pros__value']").xpath(".//div[@class='pros__entry']/text()").getall():
                        file.write("->"+ item + '\n')
                cons = card.xpath(".//div[@class='product-summary cons']")
                for data in cons:
                    file.write(data.xpath(".//h4/text()").get() + ":" + '\n')
                    productSummaryContainer = data.xpath(".//div[@class='product-summary__container']")
                    for item in productSummaryContainer.xpath(".//span[@class='_hawk cons__value']").xpath(".//div[@class='cons__entry']/text()").getall():
                        file.write("->"+ item + '\n')
                file.write('*'*50 + '\n')
