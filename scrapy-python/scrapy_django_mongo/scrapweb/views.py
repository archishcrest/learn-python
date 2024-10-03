from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

from twisted.internet import reactor, defer, asyncioreactor
from crochet import setup, wait_for

import sys
from .static_webname_dynamic import FilteredSitemapSpider
from .all_tag_scraps_dynamic import DynamicTagSpider
from .all_tag_scraps_sap_dynamic import DynamicTagSpiderSAP

from .models import *

# Install asyncio reactor before anything else runs
if 'twisted.internet.reactor' not in sys.modules:
    asyncioreactor.install()

setup() 

class ScrapView(APIView):

	@wait_for(timeout=60.0)  # Timeout for spider to finish (in seconds)
	def post(self, request):

		sitemap_urls = request.data['url']

		print(sitemap_urls)

		newSite = Site.objects.create(
			name=sitemap_urls
		)

		if sitemap_urls.endswith('.xml'):

			process = CrawlerProcess(get_project_settings())
			process.crawl(FilteredSitemapSpider, sitemap_urls=sitemap_urls,site_id=newSite)
			process.start()

		else:
			# process = CrawlerProcess(get_project_settings())
			# tags = request.data['tags']
			# process.crawl(DynamicTagSpider, sitemap_urls=sitemap_urls,site_id=newSite,tags=tags)
			# process.start()

			# process = CrawlerProcess(get_project_settings())
			# tags = request.data['tags']
			# process.crawl(DynamicTagSpiderSAP, sitemap_urls=sitemap_urls,site_id=newSite,tags=tags)
			# process.start()

			# tags = request.data['tags']
			# runner = CrawlerRunner(get_project_settings())
			# runner.crawl(DynamicTagSpider, sitemap_urls=sitemap_urls, site_id=newSite.id, tags=tags)

			tags = request.data['tags']
			runner = CrawlerRunner(get_project_settings())

			d = runner.crawl(DynamicTagSpider, site_id=newSite, sitemap_urls=sitemap_urls, tags=tags)

		return Response('Spider executed successfully', status=status.HTTP_200_OK)