# from SPARQLWrapper import SPARQLWrapper, JSON
# import rdflib

# # Initialize graph and namespaces
# graph = rdflib.Graph()
# NM = rdflib.Namespace("http://www.semanticweb.org/natishamallick/ontologies/2023/basketballNM#")
# graph.bind("basketballNM", NM)

# sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# prefixes = """
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX dbo: <http://dbpedia.org/ontology/>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX foaf: <http://xmlns.com/foaf/0.1/>
# PREFIX basketballNM: <http://www.semanticweb.org/natishamallick/ontologies/2023/basketballNM/>
# """

# query = prefixes + """
# SELECT ?player ?player_name ?birthDate ?height ?weight ?team ?team_name ?position ?position_name ?league ?league_name ?leagueEstablished ?numberOfChampionships WHERE {
#   ?player rdf:type dbo:BasketballPlayer .
#   ?player foaf:name ?player_name .
#   OPTIONAL { ?player dbo:birthDate ?birthDate . }
#   OPTIONAL { ?player dbo:height ?height . }
#   OPTIONAL { ?player dbo:weight ?weight . }
#   OPTIONAL { 
#     ?player dbo:team ?team .
#     ?team rdfs:label ?team_name .
#     FILTER(lang(?team_name) = "en")
#   }
#   OPTIONAL { 
#     ?player dbo:position ?position .
#     ?position rdfs:label ?position_name .
#     FILTER(lang(?position_name) = "en")
#   }
#   OPTIONAL { 
#     ?team dbo:league ?league .
#     ?league rdfs:label ?league_name .
#     ?league dbo:established ?leagueEstablished .
#     OPTIONAL { ?team dbo:numberOfChampionships ?numberOfChampionships . }
#     FILTER(lang(?league_name) = "en")
#   }
# } LIMIT 10
# """

# sparql.setQuery(query)
# sparql.setReturnFormat(JSON)
# results = sparql.query().convert()

# for result in results["results"]["bindings"]:
#     player = rdflib.URIRef(result['player']['value'])
#     graph.add((player, rdflib.RDF.type, NM.BasketballPlayer))

#     # Add player properties to the graph
#     if 'player_name' in result:
#         graph.add((player, NM.name, rdflib.Literal(result['player_name']['value'])))
#     if 'birthDate' in result:
#         graph.add((player, NM.birthDate, rdflib.Literal(result['birthDate']['value'])))
#     if 'height' in result:
#         graph.add((player, NM.height, rdflib.Literal(result['height']['value'], datatype=rdflib.XSD.decimal)))
#     if 'weight' in result:
#         graph.add((player, NM.weight, rdflib.Literal(result['weight']['value'], datatype=rdflib.XSD.decimal)))
#     if 'team' in result:
#         team = rdflib.URIRef(result['team']['value'])
#         graph.add((player, NM.played_for, team))
#     if 'position' in result:
#         position = rdflib
#     # Add team properties to the graph
#     if 'team' in result and 'team_name' in result:
#         graph.add((team, rdflib.RDF.type, NM.Team))
#         graph.add((team, NM.name, rdflib.Literal(result['team_name']['value'])))

#     # Add position properties to the graph
#     if 'position' in result and 'position_name' in result:
#         graph.add((position, rdflib.RDF.type, NM.Position))
#         graph.add((position, NM.name, rdflib.Literal(result['position_name']['value'])))

#     # Add league properties to the graph
#     if 'league' in result:
#         league = rdflib.URIRef(result['league']['value'])
#         graph.add((team, NM.part_of_league, league))

#         if 'league_name' in result:
#             graph.add((league, NM.name, rdflib.Literal(result['league_name']['value'])))
#         if 'leagueEstablished' in result:
#             graph.add((league, NM.established, rdflib.Literal(result['leagueEstablished']['value'])))
#         if 'numberOfChampionships' in result:
#             graph.add((team, NM.numberOfChampionships, rdflib.Literal(result['numberOfChampionships']['value'], datatype=rdflib.XSD.integer)))


# with open('basketball_data.ttl', 'wb') as ttl_file:
#     ttl_file.write(graph.serialize(format='turtle'))

# print("Data saved to basketball_data.ttl")

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
from rdflib import Graph, Literal, URIRef, Namespace
from rdflib.namespace import RDF, RDFS, OWL

# Create a graph and define the namespace
graph = rdflib.Graph()
NM = Namespace("http://www.semanticweb.org/natishamallick/ontologies/2023/basketballNM#")
graph.bind("NM", NM)

# Query DBpedia using SPARQL
sparql = SPARQLWrapper("https://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbp: <http://dbpedia.org/property/>
    PREFIX dbr: <http://dbpedia.org/resource/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT DISTINCT ?player ?name ?birthDate ?birthPlace ?team ?position ?height ?weight ?careerStart ?careerEnd WHERE {
        ?player rdf:type dbo:BasketballPlayer ;
                foaf:name ?name ;
                dbo:birthDate ?birthDate ;
                dbo:birthPlace ?birthPlace ;
                dbo:team ?team ;
                dbo:position ?position ;
                dbo:height ?height ;
                dbo:weight ?weight ;
                dbp:careerStart ?careerStart ;
                dbp:careerEnd ?careerEnd .
        FILTER (lang(?name) = 'en')
    }
    LIMIT 100
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    player = URIRef(result["player"]["value"])
    name = Literal(result["name"]["value"])
    birthDate = Literal(result["birthDate"]["value"], datatype=rdflib.XSD.date)
    birthPlace = URIRef(result["birthPlace"]["value"])
    team = URIRef(result["team"]["value"])
    position = URIRef(result["position"]["value"])
    height = Literal(result["height"]["value"], datatype=rdflib.XSD.decimal)
    weight = Literal(result["weight"]["value"], datatype=rdflib.XSD.decimal)
    careerStart = Literal(result["careerStart"]["value"], datatype=rdflib.XSD.date)
    careerEnd_value = result["careerEnd"]["value"]
    
    if careerEnd_value.lower() == 'present':
        careerEnd = Literal("Currently active")
    else:
        careerEnd = Literal(careerEnd_value, datatype=rdflib.XSD.date)

    graph.add((player, RDF.type, NM.BasketballPlayer))
    graph.add((player, NM.name, name))
    graph.add((player, NM.birthDate, birthDate))
    graph.add((player, NM.birthPlace, birthPlace))
    graph.add((player, NM.playsFor, team))
    graph.add((player, NM.hasPosition, position))
    graph.add((player, NM.height, height))
    graph.add((player, NM.weight, weight))
    graph.add((player, NM.careerStart, careerStart))
    graph.add((player, NM.careerEnd, careerEnd))

# Serialize the graph to a TTL file
graph.serialize(destination="basketball_dbpedia_dump.ttl", format="ttl")


