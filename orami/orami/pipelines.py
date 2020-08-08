# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class OramiPipeline:
    def process_item(self, item, spider):
        return item

class OramiProductPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('product_name'):
            adapter['product_name'] = adapter.get('product_name').strip()

        if adapter.get('product_brand'):
            adapter['product_brand'] = adapter.get('product_brand').strip()

        if adapter.get('product_url'):
            adapter['product_url'] = adapter.get('product_url').strip()

        adapter['rating'] = str(adapter.get('rating'))
        adapter['created'] = str(adapter.get('created'))

        if adapter.get('price_range'):
            adapter['price_range'] = adapter.get('price_range').strip()

        if adapter.get('normal_price'):
            adapter['normal_price'] = adapter.get('normal_price').strip()

        if adapter.get('disc_price'):
            adapter['disc_price'] = adapter.get('disc_price').strip()

        return item

