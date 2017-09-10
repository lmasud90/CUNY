from igraph import *

g = Graph()

g.add_vertices(10)

# For Carol
g.add_edges([
    (0,1),
    (0,2),
    (0,3)
])

# For Andre
g.add_edges([
    (1,2),
    (1, 7),
    (1,3)
])

# For Beverly
g.add_edges([
    (7,3),
    (7,8),
    (7,9)
])

# For Fernando
g.add_edges([
    (2,3),
    (2,8),
    (2,4)
])

# For Garth
g.add_edges([
    (8,4),
    (8,3),
    (8,9)
])

# For Ed
g.add_edges([
    (9,3)
])

# For Ike
g.add_edges([
    (5, 4)
])

# For Jane
g.add_edges([
    (6,5)
])

# Labels
g.vs["label"] = ["Carol", "Andre", "Fernando", "Diane", "Heather", "Ike", "Jane", "Beverly", "Garth", "Ed"]
plot(g)