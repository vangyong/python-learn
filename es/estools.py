#!/usr/bin/python
# -*- coding: UTF-8 -*-

from elasticsearch import Elasticsearch


class Search(object):

    def __init__(self, ip='127.0.0.1'):
        self.es = Elasticsearch([ip], port=9200)

    def create_index(self, index_name='new', index_type="ott_date"):
        """
        创建索引, 创建索引名字
        :param ex: Elasticsearch对象
        :return:
        """
        # 索引 相当于数据库中的 库名
        _index_mappings = {
            "mappings": {
                index_type: {  # 相当于数据库中的表名
                    "properties": {
                        "title": {
                            "type": "text",
                            "index": True,
                        },
                        "date": {
                            "type": "date",
                            "store": True,
                            "format": "yyyy/MM/dd HH:mm:ss||yyyy/MM/dd||epoch_millis"
                        },
                        "keyword": {
                            "type": "keyword",
                            "index": "not_analyzed"
                        },
                        "source": {
                            "type": "string",
                            "index": "not_analyzed"
                        },
                        "link": {
                            "type": "string",
                            "index": "not_analyzed"
                        }
                    }
                }
            }
        }
        if self.es.indices.exists(index=index_name) is not True:
            res = self.es.indices.create(index=index_name, body=_index_mappings)
            print(res)



class ElasticObj(object):

    def __init__(self, index_name, index_type, ip="127.0.0.1"):
        '''

        :param index_name: 索引名称
        :param index_type: 索引类型
        '''
        self.index_name = index_name
        self.index_type = index_type
        self.es = Elasticsearch([ip], http_auth=('elastic', 'password'), port=9200)



    def Delete_Index_Data(self, id):
        '''
        删除索引中的一条
        :param id:
        :return:
        '''
        res = self.es.delete(index=self.index_name, doc_type=self.index_type, id=id)
        print
        res

    def bulk_Index_Data(self):
        '''
        用bulk将批量数据存储到es
        :return:
        '''
        list = [
            {"date": "2017/09/13",
             "source": "慧聪网",
             "link": "http://info.broadcast.hc360.com/2017/09/130859749974.shtml",
             "keyword": "电视",
             "title": "付费 电视 行业面临的转型和挑战"
             },
            {"date": "2017/09/13",
             "source": "中国文明网",
             "link": "http://www.wenming.cn/xj_pd/yw/201709/t20170913_4421323.shtml",
             "keyword": "电视",
             "title": "电视 专题片《巡视利剑》广获好评：铁腕反腐凝聚党心民心"
             },
            {"date": "2017/09/13",
             "source": "人民电视",
             "link": "http://tv.people.com.cn/BIG5/n1/2017/0913/c67816-29533981.html",
             "keyword": "电视",
             "title": "中国第21批赴刚果（金）维和部隊启程--人民 电视 --人民网"
             },
            {"date": "2017/09/13",
             "source": "站长之家",
             "link": "http://www.chinaz.com/news/2017/0913/804263.shtml",
             "keyword": "电视",
             "title": "电视 盒子 哪个牌子好？ 吐血奉献三大选购秘笈"
             }
        ]
        ACTIONS = []
        i = 1
        for line in list:
            action = {
                "_index": self.index_name,
                "_type": self.index_type,
                "_id": i,  # _id 也可以默认生成，不赋值
                "_source": {
                    "date": line['date'],
                    "source": line['source'].decode('utf8'),
                    "link": line['link'],
                    "keyword": line['keyword'].decode('utf8'),
                    "title": line['title'].decode('utf8')}
            }
            i += 1
            print
            action
            ACTIONS.append(action)
            # 批量处理
        success, _ = bulk(self.es, ACTIONS, index=self.index_name, raise_on_error=True)
        print('Performed %d actions' % success)

    def Get_Data_By_Body(self):

        doc = {
            "query": {
                "match": {
                    "keyword": "电视"
                }
            }
        }
        _searched = self.es.search(index=self.index_name, doc_type=self.index_type, body=doc)

        for hit in _searched['hits']['hits']:
            # print hit['_source']
            print
            hit['_source']['date'], hit['_source']['source'], hit['_source']['link'], hit['_source'][
                'keyword'], \
            hit['_source']['title']


if __name__ == '__main__':
    Search().create_index()

    # obj = ElasticObj("new", "ott_date")
    # ids = 'AWrkQ3pQMaFgY0F_O9X7'
    # obj.Delete_Index_Data(ids)

    # obj = ElasticObj("tv_info_a", "tv_details_a")
    # obj.bulk_Index_Data()

    # obj = ElasticObj("tv_info_a", "tv_details_a")
    # obj.Get_Data_By_Body()
