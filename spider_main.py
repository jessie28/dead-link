# coding:utf-8
import url_get,url_manager,url_downloader,html_outputer,html_parser

class SpiderMain():
    def __init__(self):
        self.links = url_get.UrlGet()
        self.urls = url_manager.UrlManager()
        self.downloader = url_downloader.UrlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.loop = True

    def craw(self):


        while self.loop :
            self.links.add_content_list()
            if self.links.haveContentArr():
                while self.links.haveContentArr():
                    print "ok"
                    # 有数据
                    content_data = self.links.get_new_list()
                    if content_data :
                        self.urls.add_url_list(content_data)

                        while self.urls.have_url_list():
                            content = self.urls.get_url()
                            if content :
                                self.outputer.collect_data(content)
                            else:
                                pass

                        if self.outputer.hasData:
                            self.outputer.output()
                    else :
                        pass
            else:
                print 'over'
                self.loop = False
                return


            # print content_data


        # if self.links.haveContentArr():
        #     print "ok"
        #     # 有数据
        # else:
        #     #没数据
        #     print 'empty'
        #     self.page += 1
        #     self.links.add_content_list(self.page)

        # 获取content表里的数据
        # while self.links.haveContentArr():
        #     self.urls.add_content_list(content_arr)
        #     new_url_arr = self.urls.get_new_url






if __name__ == "__main__":

    obj_spider = SpiderMain()
    obj_spider.craw()






