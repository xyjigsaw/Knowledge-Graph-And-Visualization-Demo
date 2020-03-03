# Name: neo4j_models
# Author: Reacubeth
# Mail: noverfitting@gmail.com
# *_*coding:utf-8 *_*


from py2neo import Graph
import cpca
import neo4j


class Neo4jTool:
    graph = None

    def __init__(self):
        print("Initialize Neo4j tools...")

    def connect2neo4j(self):
        self.graph = Graph("http://localhost:7474", username="neo4j", password="123456")

    def get_rel(self, val):
        loc = val
        df = cpca.transform([loc], open_warning=False)
        sheng = ''
        shi = ''
        qu = ''
        if str(df['省'][0]):
            sheng = str(df['省'][0])
        if str(df['市'][0]):
            shi = str(df['市'][0])
            if shi == sheng:
                shi = ''
        if str(df['区'][0]):
            qu = str(df['区'][0])
            if qu == shi:
                qu = ''
        loc = sheng + shi + qu
        if loc == '':
            loc = str(df['地址'][0])
        sql = "MATCH (n1)<-[rel]-(n2:EVENT) WHERE n1.locationName=~'.*" + str(loc) + ".*' RETURN rel, n2 LIMIT 10;"
        answer = self.graph.run(sql).data()
        sql2 = "MATCH (n1)<-[rel]-(n2:PATIENT) WHERE n1.locationName=~'.*" + str(loc) + ".*' RETURN rel, n2 LIMIT 20;"
        answer.extend(self.graph.run(sql2).data())
        print(sheng, shi, qu)
        return answer
