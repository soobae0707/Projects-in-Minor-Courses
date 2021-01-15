####google code archive: g / tutorial: t/ modified from me: m/ created= c

##total_count

#1. total number of triples: g
tot_triples= """SELECT (COUNT(*) AS ?no) { ?s ?p ?o }"""

#2. total number of distinct classes: g/m
tot_classes= """SELECT (COUNT(distinct ?o) AS ?no)
WHERE { ?s rdf:type ?o }"""

#3. total number of distinct predicates: g/m
tot_p= """SELECT (COUNT(distinct ?p) AS ?no)
WHERE { ?s ?p ?o .}"""

#4. total number of distinct subject nodes: g
tot_s= """SELECT (COUNT(DISTINCT ?s ) AS ?no) { ?s ?p ?o }"""

#5. total number of distinct object nodes: g
tot_o= """SELECT (COUNT(DISTINCT ?o ) AS ?no) { ?s ?p ?o filter(!isLiteral(?o)) }"""

#6. total number of occurrences of properties: t Q. difference between property and predicate?

tot_property= """
SELECT ?class ?property (COUNT(?property) AS ?prop_count)
WHERE { ?individual a ?class ; ?property ?something .}
GROUP BY ?class ?property ?prop_count 
ORDER BY ?class DESC(?prop_count)"""

## table

#1. table: class vs. total number of instances of the class: g

class_vs_num= """SELECT ?class (COUNT(?s) AS ?count ) { ?s a ?class } GROUP BY ?class ORDER BY ?count"""

#2. table: property vs. total number of triples using the property: g

prop_vs_num_tri= """SELECT ?p (COUNT(?s) AS ?count ) { ?s ?p ?o } GROUP BY ?p ORDER BY ?count"""

#3. table: property vs. total number of distinct subjects in triples using the property: g

prop_vs_num_sub= """SELECT ?p (COUNT(DISTINCT ?s ) AS ?count ) { ?s ?p ?o } GROUP BY ?p ORDER BY ?count"""

#4. table: property vs. total number of distinct objects in triples using the property: g

prop_vs_num_obj= """SELECT ?p (COUNT(DISTINCT ?o ) AS ?count ) { ?s ?p ?o } GROUP BY ?p ORDER BY ?count"""


## full: can also put limits on results (which the user can put as argument)

#1. exhaustive list of classes used in the dataset: g/t

full_classes= """SELECT DISTINCT ?type { ?s a ?type }"""

#2. exhaustive list of properties used in the dataset: g

full_properties= """SELECT DISTINCT ?p { ?s ?p ?o }"""


###### created queries

#1. Number of named graph being the subject of another line

num_ng_as_sub= """SELECT ?g ?some_prop
WHERE { 
    GRAPH ?g { ?s ?p ?o . }
    ?g ?some_prop ?obj .
}"""

#2. Percentages (not the counts) of distinct type of s/p/o : possible to get proportions?

perc_sub= """SELECT ((COUNT(?ind_class) AS ?class_indiv)/(COUNT(?ind) AS ?total_indiv)*100)"""

#3. Count/proportions of URI/Literal of s/p/o i.e. frequency of datatype
#4. AVG, MIN, MAX of the results: e.g. count for each s/p/o categories
#5. Broad overview: a big table with num of s/p/o

all_queries= [tot_triples, tot_classes, class_vs_num]
query_total= [tot_triples, tot_classes, tot_p, tot_s, tot_o]
query_table= [class_vs_num, prop_vs_num_tri, prop_vs_num_sub, prop_vs_num_obj]
query_full= [full_classes, full_properties]
