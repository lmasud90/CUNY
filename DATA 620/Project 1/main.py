from neo4j.v1 import GraphDatabase, basic_auth

def clean_line(line):
    invalids = ['"', '\n']
    for n in invalids:
        line = line.replace(n, '')
        
    return line

def extract_data(file_loc, props):
    # Read in file
    routes_file = open(file_loc, "r")
    routes_lines = routes_file.readlines()
    routes_file.close()
    

    #Takes the lines that were read in, does a split to create an array, then zips
    #with the props to create a 2d array, and then forms a dictionary from that 2d array,
    #and returns a list of those dictionaries.
    return list(map(lambda x: dict(zip(props, clean_line(x).split(","))), routes_lines))
    
airport_props = [
        "airport_id",
        "name",
        "city",
        "country",
        "iata",
        "icao",
        "lat",
        "lon",
        "altitude",
        "timezone",
        "dst",
        "tz_database_time_zone",
        "type",
        "source"
]

route_props = [
        "airline",
        "airline_id",
        "source_airport",
        "source_airport_id",
        "destination_airport",
        "destination_airport_id",
        "codeshare",
        "stops",
        "equipment"
        ]

routes = extract_data("routes_small.dat", route_props)
airports = extract_data("airports_small.dat", airport_props)

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "password"))
session = driver.session()

for airport in airports:
    session.run(
        """CREATE (a:Airport {
            airport_id: {airport_id},
            name: {name},
            city: {city},
            country: {country},
            iata: {iata},
            icao: {icao},
            lat: {lat},
            lon: {lon},
            altitude: {altitude},
            timezone: {timezone},
            dst: {dst},
            tz_database_time_zone: {tz_database_time_zone},
            type: {type},
            type: {source}})""", airport)

for route_info in routes:
    route = {"destination": route_info["destination_airport"], "source": route_info["source_airport"]}
    session.run("MATCH(n: Airport {iata: {destination}}) MATCH(v: Airport {iata: {source}}) CREATE (n)-[:flies_to]->(v)", route)

    session.run(
        """CREATE (a:Route {
            airline: {airline},
            airline_id: {airline_id},
            source_airport: {source_airport},
            source_airport_id: {source_airport_id},
            destination_airport: {destination_airport},
            destination_airport_id: {destination_airport_id},
            codeshare: {codeshare},
            stops: {stops},
            equipment: {equipment}})
        """, route_info)

    session.run("MATCH(n: Airport {iata: {source}}) MATCH(v: Route {source_airport: {source}}) CREATE (n)-[:flies_to]->(v)", route)
    session.run("MATCH(n: Airport {iata: {destination}}) MATCH(v: Route {destination_airport: {destination}}) CREATE (n)-[:flies_to]->(v)", route)
    
session.close()