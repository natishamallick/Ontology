# Ontology
Basketball_Ontology
The goal of this coursework is to put the ontology modelling semantic data development, Description Logic (DL) and SWRL skills into practice that you have learnt
in the Semantic Web lectures and labs in a larger project.

Your task is to define, populate and query an ontology (including A-Box and a T-box) on a topic of your choice. 
The ontology must be able to integrate and reuse already available semantic data. 

At least two concepts of the ontology T-Box must be taken from external semantic data repositories. 
This way, the ontology will have an A-Box that can be populated with already existing data. 
You will use Protégé to design the ontology, and Python-based semantic tooling to populate the ontology with real world data.

Specifically, you should achieve the following:
Basic Task (60% coursework marks): Define your ontology in OWL2. The T-Box must be created using Protégé and should be your own work (not an existing ontology, 
butmay import existing ontologies). Populate the knowledge base from an external semantic data repository using SPARQL 1.1. Verify that you can also query the local
ontology using SPARQL.

Bonus Task 1 (20% coursework marks): As above, but your ontology should fuse information from at least two distinct external data repositories. 
The query to your local ontology should answer questions that cannot be answered by either remote knowledge base alone.

Bonus Task 2 (20% coursework marks): You are required to use Description Logic rules to define as many concepts as possible with the help of SWRL rules in order to
compensate for the limitations of the Protégé inference engines with DL. 
The A-Box (individuals) must be created in a way to demonstrate the correctness and effectiveness of the logic rules defined.
