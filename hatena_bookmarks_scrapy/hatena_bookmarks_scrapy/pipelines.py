import os
import datetime
import csv
import dropbox
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter


class HatenaBookmarksScrapyPipeline:
    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):
        self.local_filename = 'hatena_bookmarks_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
        self.csv_file = open(self.local_filename, 'wb')
        self.exporter = CsvItemExporter(self.csv_file, quoting=csv.QUOTE_NONNUMERIC)
        self.exporter.start_exporting()
        self.dbx = dropbox.Dropbox('TOKENを設定してください')


    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csv_file.close()
        self.dbx.files_upload(open(self.local_filename, 'rb').read(), '/scrapy/hatena_bookmarks/{}'.format(self.local_filename),  mode=dropbox.files.WriteMode('overwrite'))
        os.remove(self.local_filename)


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
