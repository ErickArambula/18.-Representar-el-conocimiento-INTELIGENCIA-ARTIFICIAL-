from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS

# Crear un grafo RDF
g = Graph()

# Definir un espacio de nombres
ex = Namespace("http://example.org/")

# Definir conceptos y relaciones
g.add((ex.Person, RDF.type, RDFS.Class))
g.add((ex.name, RDF.type, RDF.Property))
g.add((ex.age, RDF.type, RDF.Property))

# Crear instancias y asignar propiedades
john = URIRef("http://example.org/john")
g.add((john, RDF.type, ex.Person))
g.add((john, ex.name, Literal("John")))
g.add((john, ex.age, Literal(30)))

# Consulta de la ontología
for s, p, o in g:
    print(s, p, o)
