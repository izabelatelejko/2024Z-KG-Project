# 2024Z-KG-Project
Project for the 2024Z Knowledge Graphs course

30.11.2024

What we prepared:
* Project idea: Travel assistant - gather data related to traveling (flights, hotels etc.), we want to define some query templates that could be populated with parameters (read from some file) and as a result we would obtain travel proposals (meeting the criterias like budget, desired destinations, personalized overview of attractions)
* non KG data sources: Flights Schedules (there is an API that requires a manual approval - we do not know if this will work), TUI website - list of hotels WIP
* KG data sources: DBpedia (for mapping IATA codes)
* we managed to create KG from json data - flight schedules and run test quaries on it with pysparql anything

Questions:
* If we can't access the Flights Schedules API, can we generate the data?
* It would be nice to have the average ticket prices for data - can we generate it as well?
* Do non-KG data sources have to be of different formats?
* How much python may we use?
* 
