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

    def format_loc(self, val):
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
        return loc

    def get_rel(self, val):
        loc = self.format_loc(val)
        sql = "MATCH (n1)<-[rel]-(n2:EVENT) WHERE n1.locationName=~'.*" + str(loc) + ".*' RETURN n1, rel, n2 LIMIT 10;"
        answer = self.graph.run(sql).data()
        sql2 = "MATCH (n1)<-[rel]-(n2:PATIENT) WHERE n1.locationName=~'.*" + str(loc) + ".*' RETURN n1, rel, n2 LIMIT 20;"
        answer.extend(self.graph.run(sql2).data())
        return answer

    def match_location4patient(self, val):
        loc = self.format_loc(val)
        sql = "MATCH (n1)<-[rel]-(n2:PATIENT) WHERE n1.locationName=~'.*" + str(
            loc) + ".*' RETURN n1, rel, n2 LIMIT 40;"
        answer = self.graph.run(sql).data()
        return answer

    def match_location4event_patient(self, val):
        loc = self.format_loc(val)
        sql = "MATCH (n1)<-[rel]-(n2:EVENT) WHERE n1.locationName=~'.*" + str(loc) + ".*' RETURN n1, rel, n2 LIMIT 40;"
        answer = self.graph.run(sql).data()
        answer.extend(self.match_location4patient(loc))
        return answer

    def match_topic4event(self, val):
        sql = "MATCH (n1:EVENT)-[rel:EVENT_TOPIC]->(n2:TOPIC) WHERE n2.topicName =~'.*" + str(val) + \
              ".*' RETURN n1, rel, n2 LIMIT 40;"
        answer = self.graph.run(sql).data()
        return answer

    def match_patient_name(self, val):
        loc = self.format_loc(val)
        sql = "MATCH (n1)-[rel]->(n2:EVENT) WHERE n1.patientName=~'.*" + str(loc) + ".*' RETURN n1, rel, n2 LIMIT 40;"
        answer = self.graph.run(sql).data()
        # sql2 = "MATCH (n2:LOCATION)<-[rel]-(n1:PATIENT) WHERE n1.patientName=~'.*" + str(
        #    loc) + ".*' RETURN n1, rel, n2 LIMIT 20;"
        # answer.extend(self.graph.run(sql2).data())
        return answer

    def match_location_topic4event(self, loc, tpc):
        loc = self.format_loc(loc)
        sql = "MATCH (n1)<-[rel]-(n2:EVENT) WHERE n1.locationName=~'.*" + str(loc) + \
              ".*' WITH n1, rel, n2 MATCH (n3)<-[rel2]-(n2:EVENT) WHERE n3.topicName=~'.*" + \
              str(tpc) + ".*' RETURN n1, rel, n2 LIMIT 40;"
        answer = self.graph.run(sql).data()
        return answer

    def match_location_gender4patient(self, loc, sex):
        loc = self.format_loc(loc)
        sql = "MATCH (n1)<-[rel]-(n2:PATIENT) WHERE n1.locationName=~'.*" + str(loc) + \
              ".*' and n2.gender='" + str(sex) + "' RETURN n1, rel, n2 LIMIT 40;"
        answer = self.graph.run(sql).data()
        return answer

    def match_location_time4event(self, loc, time):
        loc = self.format_loc(loc)
        sql = "MATCH (n1)<-[rel]-(n2:EVENT) WHERE n1.locationName=~'.*" + str(loc) + \
              ".*' and n2.time = '" + str(time) + "' RETURN n1, rel, n2 LIMIT 40;"
        answer = self.graph.run(sql).data()
        return answer

    def match_location_time4event_patient(self, loc, time):
        loc = self.format_loc(loc)
        sql = "MATCH (n1)<-[rel]-(n2:EVENT) WHERE n1.locationName=~'.*" + str(loc) + \
              ".*' and n2.time = '" + str(time) + \
              "' WITH n1, rel, n2 MATCH (n3:PATIENT)-[rel2]->(n2) RETURN n1, rel, n2, rel2, n3 LIMIT 40;"
        answer = self.graph.run(sql).data()
        return answer

    def match_name_time4location_event(self, name, time):
        sql = "MATCH (n1:PATIENT)-[rel]->(n2:EVENT) WHERE n1.patientName='" + str(name) + \
              "' and n2.time='" + str(time) + \
              "' WITH n1, rel, n2 MATCH (n2)-[rel2]-(n3:LOCATION) RETURN n1, rel, n2, rel2, n3;"
        answer = self.graph.run(sql).data()
        return answer

    def match_location_time_topic4patient(self, loc, time, tpc):
        loc = self.format_loc(loc)
        sql = "MATCH (nx)<-[rel0]-(ny:EVENT) WHERE nx.topicName=~'.*" + str(tpc) + \
              ".*' and ny.time='" + str(time) + \
              "' WITH ny MATCH (n3)<-[rel2]-(ny) WHERE n3.locationName=~'.*" + str(loc) + \
              ".*' WITH ny, n3 MATCH (n2:PATIENT)-[rel3]->(ny) WITH n2 MATCH (n1:LOCATION)<-[rel]-(n2) RETURN n1, rel, n2 LIMIT 40;"
        answer = self.graph.run(sql).data()
        return answer
