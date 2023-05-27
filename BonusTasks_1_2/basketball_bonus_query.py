# -*- coding: utf-8 -*-
"""Basketball_bonus_Query.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-vQYlFq27boYPvKtKhsRUiulp2sEzgQ-
"""

pip install rdflib

pip install SPARQLWrapper

import rdflib
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

# Define the namespaces used in the ontology
NAMESPACE = {
    'rdf': RDF,
    'rdfs': RDFS,
    'fa': rdflib.Namespace('http://www.semanticweb.org/natishamallick/ontologies/2023/basketballNM#')
}

# Load the populated ontology graph
g = rdflib.Graph()
g.parse('NM_basketball_populated.owl')

# Define the name of the BasketballPlayer you want to retrieve the position for
BasketballPlayer_name = 'Borgie Hermida'


# Define the SPARQL query to retrieve the player's team
query = prepareQuery(
    '''
    SELECT ?player ?ShortPlayer
    WHERE {
        ?BasketballPlayer rdf:type fa:BasketballPlayer .
        ?BasketballPlayer fa:name ?name .
        ?player fa:height ?ShortPlayer .
        ?ShortPlayer rdf:type fa:ShortPlayer .
        FILTER (regex(?name, "%s", "i"))
    }
    ''',
    initNs=NAMESPACE
)

# Execute the SPARQL query and print the results
for result in g.query(query):
    player = result.player.split('#')[-1]
    ShortPlayer = result.ShortPlayer
    print(f'{BasketballPlayer_name} has height {ShortPlayer} and is a Short Player')
