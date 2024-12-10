# 2024Z-KG-Project
Project for the 2024Z Knowledge Graphs course

## Data Sources:

| **Source** | **Type**                 | **Content Description**                                                                                     | 
|------------|--------------------------|-------------------------------------------------------------------------------------------------------------|
| **Modlin Airport** ([Flight Schedules](https://www.modlinairport.pl/pasazer/rozklad-lotow)) | Non-KG HTML            | Flight schedules for the next 24 hours for Warsaw Modlin airport. Includes flight IDs, destinations, and departure times. | 
| **Tui Website** ([Hotels](https://tui.pl/all-inclusive))  | Non-KG HTML/JSON       | Contains travel-related information such as hotel information and prices.      | 
| **DBpedia** ([DBpedia](https://www.dbpedia.org)) | KG                     | Structured knowledge base containing information on cities, landmarks, and attractions linked to flight destinations.   | 

## Queries for Single Data Sources

All queries are in the sub-folder named `queries`.


#### Modlin Airport

Query `modln.rq` downloads the data from the Modlin airport website for all departures within the next 24 hours. The data contains information about the flight number, destination city, departure time, and current state.

Sample Output:

| **flightId** | **destText** | **depTimeText** | **stateText** |
|--------------|--------------|-----------------|---------------|
| FR 4060      | MALAGA       | 11:15           | WYLĄDOWAŁ     |
| FR 9259      | MALTA        | 11:55           | OCZEKIWANY    |



#### TUI hotels
Query `tui_hotels.rq` requests data from the tui api returning information about all? avaliable hotels. The query must be somehow updated with parameters to give up to date results.
Sample Output: 
| Location             | Name                                   | Price | Duration          | Rating           |
|----------------------|----------------------------------------|------|----------------|------------------|
| Eberstein           | Biolandhaus Arche                     | 1741 | `"6"^^xsd:int`  | `"0.0"^^xsd:double`  |
| Split               | Tifani Luxury Rooms                   | 1739 | `"6"^^xsd:int`  | `"4.0"^^xsd:double`  |
| Bar                 | Stara Carsija Resort And Spa          | 1739 | `"6"^^xsd:int`  | `"4.5"^^xsd:double`  |
| Dubrownik           | Valamar Lacroma Dubrovnik             | 1739 | `"6"^^xsd:int`  | `"4.0"^^xsd:double`  |
| Dubrownik           | Hotel Lapad                           | 1738 | `"6"^^xsd:int`  | `"4.0"^^xsd:double`  |
| Biograd na Moru     | Hotel Ilirija                         | 1736 | `"7"^^xsd:int`  | `"4.0"^^xsd:double`  |
| Riva                | Hotel Europa - Skypool & Panorama     | 1735 | `"6"^^xsd:int`  | `"4.0"^^xsd:double`  |



#### Attractions

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

#### Flights and hotels

Query `flights_hotels.rq` lists all available combinations of flights and hotels. The hotel rooms are for 2 people and displayed price is per one person.

Sample Output:

| Destination City | Flight Departure Time | Hotel Name                 | Hotel Price | Stay Duration | Hotel Standard |
|------------------|-----------------------|---------------------------|-------------|---------------|----------------|
| Barcelona        | 14:25                | BCN Urban Bonavista Hostel | 1748        | 6             | 2.0            |
| Barcelona        | 14:25                | Ingles                     | 1771        | 6             | 1.0            |
| Rzym             | 09:10                | Anfiteatro Flavio          | 1779        | 6             | 3.0            |
| Rzym             | 09:10                | Hotel Zone                 | 1779        | 6             | 4.0            |


#### Flights and hotels - with filters

Query `flights_hotels_with_filtering.rq` lists the combinations of flights and hotels that meet the requested criterias as price per day, stay duration and minimum hotel standard, ordered by price per day.

Sample Output:

| Destination City | Flight Departure Time | Hotel Name                                   | Hotel Price | Hotel Price Per Day | Stay Duration | Hotel Standard |
|------------------|-----------------------|---------------------------------------------|-------------|----------------------|---------------|----------------|
| Barcelona        | 14:25                | Catalonia Catedral                          | 2139        | 356                  | 6             | 4.0            |
| Rzym             | 09:10                | Diana Roof Garden                           | 2144        | 357                  | 6             | 4.0            |
| Barcelona        | 14:25                | Catalonia Passeig de Gracia                 | 2163        | 360                  | 6             | 4.0            |
| Rzym             | 09:10                | Comfort Hotel Bolivar                       | 2160        | 360                  | 6             | 4.0            |
| Barcelona        | 14:25                | Catalonia Square                            | 2187        | 364                  | 6             | 4.0            |
| Londyn           | 06:05                | Grand Plaza Serviced Apartments             | 2211        | 368                  | 6             | 4.0            |
| Barcelona        | 14:25                | Sensation Sagrada Familia                   | 2258        | 376                  | 6             | 4.0            |
| Londyn           | 06:05                | Thistle London Hyde Park Kensington Gardens | 2283        | 380                  | 6             | 4.0            |

## Feedback
1. Feature request - execute scripts with the browser before querying html -- to overcome cloudflare captchas etc
2. Bug report -- cli tool does not offer html functionality
3. Documentation:
    1. It's hard to figure out that you need the server to query html endpoints and the cli tool does not have html functionality altogether for some reason
    2. Nowhere in the docs is there an example of actually using http headers in the query, and their naming convention is normal (Content-Type) not something.something 
4. Sparql feature request -- path expressions like + ? * work only with explicit properties, so its impossible to use them with data from sparql-anything in a sane manner as ns:_# is common when parsing json, html or anything with a list
5. We are not sure if this is really a bug, and whether it is connected to sparql anything, but in one query we found out that changing variable name (e.g. `attractionName` -> `attractionNameEn`) would result in empty output table - no error, just no results, when with the other variable name we obtain valid results. Potential explanation is that language tags as variable name suffixes are somehow forbidden, but we couldn't find any information on that.
   
## 30.11.2024

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

## 09.12.2024

What we prepared:
1. Final choice of our datasources: TUI api for hotels, Modlin Airport website for flights and DBPedia for attractions
2. Queries for extracting data from each of them: using sparql-anything-server for obtaining the data from the internet
3. Queries that combine the data from each source
4. Queries that filter the combined data
5. Examples of the combined data
6. Presentation of the querying of data
7. Repository for our project
8. A list of suggestions for sparql-anything and sparql

What we presented:
1. The repository https://github.com/izabelatelejko/2024Z-KG-Project
2. The issues we had with dbpedia query
3. Sample outputs from all the queries

Questions:
1. How to optimize quering dbpedia?
2. How to submit a feature request to sparql?
3. How to put a limit statement in a service?

What answers we received:
1. To handle dbpedia issues - use python script to query for single cities and combine results
2. It's complicated -- to be continued
3. The service statement by default has only the WHERE part but select and the rest may be added by wrapping the service in a subquery
    
Project Plan - Final milestone:
1. Prepare python scripts for easier querying of the data (dbpedia)
2. Try to improve the mapping of airports to cities
3. Create query templates (jinja) to popluate with parameters specified by users
4. Prepare issues for sparql-anything github
5. Jupyter notebook with usage examples
6. Documentation of our solution

        
