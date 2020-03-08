# Knowledge-Graph-Visualization-Demo
**Archive**

The code is guided by Deng and Dr.Fu from [Acemap](https://www.acemap.info/).

There are 2D-Search and 3D-Graph-View for knowledge graph visualization.

KG data (COVID-2019 traces data from tencent) csv files are in folder Import2Neo4j.

---

## Neo4j Configuration

- Database Name：COVID-19
- Username：neo4j
- Password：123456

---

## Folder: Import2Neo4j

1. Put all CSV files into the Import folder shown below

![](https://gitee.com/omegaxyz/img/raw/master/upload/Neo4j-Import202003031535.png)


2. CYPHER4csvImport: Input the eight statements on by one in this file on the Neo4j console

3. After importing, you will see:

- Node Label: (EVENT, LOCATION, PATIENT, TOPIC)
- Relationship Types: (EVENT_LOCATION, EVENT_TOPIC, PATIENT_EVENT, PATIENT_LOCATION)

---


## Folder: Neo4j-3D 

It is based on js using [3d-force-graph](https://github.com/vasturiano/3d-force-graph), which can run directly.

### Preview

![](https://github.com/xyjigsaw/Knowledge-Graph-Visualization-Demo/blob/master/KG-3D-1.png)
![](https://github.com/xyjigsaw/Knowledge-Graph-Visualization-Demo/blob/master/KG-3D-2.png)

### index.html Setting
![](https://gitee.com/omegaxyz/img/raw/master/upload/ncp-3d-graph202003031559.png)

1. Configure the server address (no port number required), Neo4j username, and password in the first red box shown above.
2. The second box is the CYPHER statement, which limits the return number to 20000. The return value is as follows, and the search box can be added to HTML later.

![](https://gitee.com/omegaxyz/img/raw/master/upload/CYPHER-RETURN-3D-GRAPH202003031551.png)

---


## Folder: KG-Search

**Provide KG graph and triple lists**

### Requirements
- Django
- py2neo
- neo4j
- cpca
- Jieba

### Run
```
python manage.py runserver
```
Address：localhost: 8000

### Search
**Support 3 disorder keywords (space seperated) at most**

**Examples**

- 1 keyword
  - 江苏苏州
  - 确诊
  - 王某
- 2 keywords
  - 隔离 苏州
  - 苏州 男性
  - 苏州 2月2日
  - 2月2日 王某
- 3 keywords
  - 2月2日 苏州 确诊 


### Preview

![](https://gitee.com/omegaxyz/img/raw/master/upload/KG-Search3202003081542.png)

