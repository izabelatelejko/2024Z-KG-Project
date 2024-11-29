# 2024Z-KG-Project
Project for the 2024Z Knowledge Graphs course

30.11.2024

What we prepared:
* Project idea: Travel assistant - gather data related to traveling (flights, hotels etc.), we want to define some query templates that could be populated with parameters (read from some file) and as a result we would obtain travel proposals (meeting the criterias like budget, desired destinations, personalized overview of attractions).
* non KG data sources: Flights Schedules (there is an API that requires a manual approval - we do not know if this will work), TUI website - list of hotels WIP.
* KG data sources: DBpedia (for mapping IATA codes).
* we managed to create KG from json data - flight schedules and run test quaries on it with pysparql anything.
* sample queries searching for attractions.

What we presented:
* Data sources and queries.
* How to use pysparql anything tool (for python) to create KG from JSON files, and query it.
* Quering html files in jena fuseki .

Questions:
* If we can't access the Flights Schedules API, can we generate the data?
* It would be nice to have the average ticket prices for data - can we generate it as well?
* Do non-KG data sources have to be of different formats?
* How much python may we use?

What answers we received: 
* We should make bug reports, issues and comments, submit a PR, issue to a repository for the missing documentation about querying html using the sparql server.
* We may simulate data with the correct schema - one we would receive from the api (but it would be better to use real data).
* It would be better to have at least 2 different data formats for non-KG data sources.
* The idea of having an automated way of gathering answers - travel proposals by using query templates is good.
* We do not have to create KG from non-KG data.
* Final deliverable: github repository with code (queries) and documentation for the project, README with project description, jupyter notebook with code samples and tutorial.
  
Project Plan:
Milestone 1:
1. Prepare feedback about sparql anything and its documentation
2. Clearly defined data sources
3. More queries and/or refining (including the ones combining different data sources)
4. Data exploration
5. Document our data and solution

Jan 15:
1. Finish documentation
2. Query templates for quering our merged graph to get travel proposals
3. Jupyter notebook showcasing the capabilities of our solution
