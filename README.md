# Knowledge-Graph-Visualization-Demo
**Archive**
The code is guided by Deng and Dr.Fu in [Acemap](https://www.acemap.info/).

There are 2D-Search and 3D-Graph-View for knowledge graph visualization.

## Neo4j Configuration
- Database Name：COVID-19
- Username：neo4j
- Password：123456

## Folder Import2Neo4j

1. Put all CSV files into the Import folder shown below
![](https://gitee.com/omegaxyz/img/raw/master/upload/Neo4j-Import202003031535.png)


2. CYPHER4csvImport: Input the eight statements on by one in this file on the Neo4j console

After importing, you will see:
- Node Label: (EVENT, LOCATION, PATIENT, TOPIC)
- Relationship Types: (EVENT_LOCATION, EVENT_TOPIC, PATIENT_EVENT, PATIENT_LOCATION)


## Neo4j-3D 

It is based on JavaScript using [3d-force-graph](https://github.com/vasturiano/3d-force-graph), which can run directly.
![](https://github.com/xyjigsaw/Knowledge-Graph-Visualization-Demo/blob/master/KG-3D-1.png)
![](https://github.com/xyjigsaw/Knowledge-Graph-Visualization-Demo/blob/master/KG-3D-2.png)
- index.html
![](https://gitee.com/omegaxyz/img/raw/master/upload/ncp-3d-graph202003031559.png)
Configure the server address (no port number required), Neo4j username, and password in the first red box shown above
The second box is the CYPHER statement, which limits the return number to 20000. The return value is as follows, and the search box can be added to HTML later.
![](https://gitee.com/omegaxyz/img/raw/master/upload/CYPHER-RETURN-3D-GRAPH202003031551.png)


## KG-Search
requirements
- Django
- py2neo
- neo4j
- cpca

Run：
```
python manage.py runserver
```
Address：localhost:8000
![](https://github.com/xyjigsaw/Knowledge-Graph-Visualization-Demo/blob/master/KG-Search1.png)
![](https://github.com/xyjigsaw/Knowledge-Graph-Visualization-Demo/blob/master/KG-Search2.png)

