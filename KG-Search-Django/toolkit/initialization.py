# Name: initialization
# Author: Reacubeth
# Mail: noverfitting@gmail.com
# *_*coding:utf-8 *_*

import sys
from Model.neo4j_models import Neo4jTool

sys.path.append("..")

neo_con = Neo4jTool()  # 预加载neo4j
neo_con.connect2neo4j()
print('Neo4j has connected...')
