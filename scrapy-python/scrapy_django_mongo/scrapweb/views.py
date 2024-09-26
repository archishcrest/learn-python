from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

from .static_webname_dynamic import FilteredSitemapSpider
from .all_tag_scraps_dynamic import DynamicTagSpider

from .models import *

class ScrapView(APIView):

	def post(self, request):

		sitemap_urls = request.data['url']

		newSite = Site.objects.create(
			name=sitemap_urls
		)

		if sitemap_urls.endswith('.xml'):

			process = CrawlerProcess(get_project_settings())
			process.crawl(FilteredSitemapSpider, sitemap_urls=sitemap_urls,site_id=newSite)
			process.start()

		else:
			process = CrawlerProcess(get_project_settings())
			tags = request.data['tags']
			process.crawl(DynamicTagSpider, sitemap_urls=sitemap_urls,site_id=newSite,tags=tags)
			process.start()

			# tags = request.data['tags']
			# runner = CrawlerRunner(get_project_settings())
			# runner.crawl(DynamicTagSpider, sitemap_urls=sitemap_urls, site_id=newSite.id, tags=tags)


		return Response('Spider executed successfully', status=status.HTTP_200_OK)