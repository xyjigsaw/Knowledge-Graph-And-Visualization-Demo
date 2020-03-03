# Knowledge-Graph-Visualization-Demo
There are 2D-Search and 3D-Graph-View for knowledge graph visualization.

## Neo4j
- Database Name：COVID-19
- Username：neo4j
- Password：123456

## Import2Neo4j

1. Put all CSV files into the Import folder shown below
![](https://gitee.com/omegaxyz/img/raw/master/upload/Neo4j-Import202003031535.png)


2. CYPHER4csvImport: Input the eight statements on by one in this file on the Neo4j console

After importing, you will see:
Node Label: (EVENT, LOCATION, PATIENT, TOPIC)
Relationship Types: (EVENT_LOCATION, EVENT_TOPIC, PATIENT_EVENT, PATIENT_LOCATION)


## Neo4j-3D 
(JavaScript Based, which can run directly)
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