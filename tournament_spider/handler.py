import boto3
import json
import scrapy
from spiders.frisbee_spider import FrisbeeSpider
from datetime import datetime

from scrapy.crawler import CrawlerProcess


def main(event, context):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'result.json'
    })

    process.crawl(FrisbeeSpider)
    process.start() # the script will block here until the crawling is finished

    date = datetime.today().strftime('%Y-%m-%d')
    file_name = 'result' + date + '.json'
    save_file_to_s3('return-tournament-file', file_name)

    print('All done.')

def save_file_to_s3(bucket, file_name):
    data = open(file_name, 'r')
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, file_name)
    obj.put(Body=json.dumps(data))