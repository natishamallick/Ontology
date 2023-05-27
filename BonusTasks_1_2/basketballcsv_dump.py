import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, XSD



# Namespace and ontology
nm = Namespace("http://www.semanticweb.org/natishamallick/ontologies/2023/basketballNM#")

# Creating an RDF graph
g = Graph()

with open('team.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)  # Skip the header row

    # Reading the CSV data and adding it to the RDF graph
    for row in csv_reader:
        player_uri = URIRef(nm + row[0].replace(" ", "_"))
        g.add((player_uri, RDF.type, nm.BasketballPlayer))
        g.add((player_uri, nm.name, Literal(row[0], datatype=XSD.string)))
        g.add((player_uri, nm.birthDate, Literal(row[1], datatype=XSD.date)))
        g.add((player_uri, nm.age, Literal(int(row[2]), datatype=XSD.integer)))
        g.add((player_uri, nm.height, Literal(float(row[3]), datatype=XSD.decimal)))
        g.add((player_uri, nm.weight, Literal(float(row[4]), datatype=XSD.decimal)))
        g.add((player_uri, nm.hasPosition, URIRef(nm + row[5].replace(" ", "_"))))
        g.add((player_uri, nm.playsFor, URIRef(nm + row[6].replace(" ", "_"))))

        team_uri = URIRef(nm + row[6].replace(" ", "_"))
        g.add((team_uri, RDF.type, nm.Team))
        g.add((team_uri, nm.playsInLeague, URIRef(nm + row[7])))

        league_uri = URIRef(nm + row[7])
        g.add((league_uri, RDF.type, nm.League))
        g.add((league_uri, nm.leagueEstablished, Literal(int(row[8]), datatype=XSD.integer)))
        g.add((team_uri, nm.numberOfChampionships, Literal(int(row[9]), datatype=XSD.integer)))

# Serialize the graph to TTL
ttl_data = g.serialize(format="turtle")

# Save the TTL data to a file
with open("csv_dump.ttl", "w") as ttl_file:
    ttl_file.write(ttl_data)