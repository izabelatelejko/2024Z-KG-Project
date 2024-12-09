# 2024Z-KG-Project
Project for the 2024Z Knowledge Graphs course

## Data Sources:

| **Source** | **Type**                 | **Content Description**                                                                                     | 
|------------|--------------------------|-------------------------------------------------------------------------------------------------------------|
| **Modlin Airport** ([Flight Schedules](https://www.modlinairport.pl/pasazer/rozklad-lotow)) | Non-KG HTML            | Flight schedules for the next 24 hours for Warsaw Modlin airport. Includes flight IDs, destinations, and departure times. | 
| **Tui Website**                        | Non-KG HTML/JSON       | Contains travel-related information such as vacation packages, flight schedules, and destination data.      | 
| **DBpedia** ([DBpedia](https://www.dbpedia.org)) | KG                     | Structured knowledge base containing information on cities, landmarks, and attractions linked to flight destinations.   | 

## Queries for Single Data Sources

All queries are in the sub-folder named `queries`.


#### Modlin Airport

Query `flights.rq` downloads the data from the Modlin airport website for all departures within the next 24 hours. The data contains information about the flight number, destination city, departure time, and current state.

Sample Output:

| **flightId** | **destText** | **depTimeText** | **stateText** |
|--------------|--------------|-----------------|---------------|
| FR 4060      | MALAGA       | 11:15           | WYLĄDOWAŁ     |
| FR 9259      | MALTA        | 11:55           | OCZEKIWANY    |


#### Attracrions

Query `dbpedia_attractions.rq` contains the information about places and attractions in chosen city.

Sample output for Warsaw:

#### Sample Output:
| **cityName**  | **attractionName**                                      | **attractionNamePolish**             | **categoryLabel** | **desc**                                                                                                                                                                                                                                                                                                                                                   |
|---------------|---------------------------------------------------------|---------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Warszawa      | Saxon Garden                                            | Ogród Saski w Warszawie               | place             | "The Saxon Garden (Polish: Ogród Saski) is a 15.5–hectare public garden in the Śródmieście district of Warsaw, Poland, facing Piłsudski Square. It is the oldest public park in the city. Established in the late 17th century, it opened to the public in 1727 as one of the first parks in the world accessible to all."                                      |
| Warszawa      | Blank Palace                                            | Pałac Blanka                          | place             | "The Blank Palace (Polish: Pałac Blanka) is a historic building on Senatorska Street in Warsaw, Poland. Built in the 18th century, it has been a residence for various notable figures. After destruction during World War II, it was rebuilt and now houses the Ministry of Sport and Tourism."                                                             |
| Warszawa      | Deanery of St. John's Cathedral, Warsaw                 | Pałac Dziekana w Warszawie            | place             | "The Deanery of St. John's Cathedral, Warsaw (Polish: Pałac Dziekana w Warszawie) is a historic structure in the Old Town of Warsaw, Poland. Built in the 16th century, it is now home to the Museum of the Archdiocese of Warsaw."                                                                                                                     |

---

## Queries Combining Data

#### Flights and Attractions

Query `flights_attractions.rq` lists all the attractions for cities that are available destinations from Modlin airport.

Sample Output:

| **cityName**  | **attractionName**     | **attractionDescription**                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **attractionTags**                |
|---------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Barcelona     | CaixaBank              | "CaixaBank, S.A., formerly Criteria CaixaCorp, is a major Spanish financial institution headquartered in Valencia, Spain. It is Spain's third-largest lender and operates an extensive branch network serving millions of customers. The bank is also involved in telecommunications and energy investments."@en                                                                                                                      | agent, organisation, company, bank |
| Liverpool     | Calderstones House     | "Calderstones Mansion House, located in Calderstones Park, Liverpool, is a Grade II listed building built in 1828. It has served various purposes, including as a residence, council offices, and cultural venue. It is now a center for literature and shared reading, managed by The Reader, with a permanent exhibition on local history."@en                                                                                           | architectural structure, building |


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
