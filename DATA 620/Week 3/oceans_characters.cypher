//Ocean's 13

CREATE (clooney: Actor {character: "Frank Ocean", name: "George Clooney", nickname: "clooney"})-[:in]->(oceans13:Movie {name:"Ocean's 13", released: "2006"}),
       (pitt: Actor {character:"Rusty Ryan", name: "Brad Pitt", nickname: "pitt"})-[:in]->(oceans13), 
       (damon: Actor {character:"Linus Caldwell", name: "Matt Damon", nickname: "damon"})-[:in]->(oceans13),
       (garcia: Actor {character:"Terry Benedict", name: "Andy Garcia", nickname: "garcia"})-[:in]->(oceans13), 
       (cheadle: Actor {character:"Basher Tarr", name: "Don Cheadle", nickname: "cheadle"})-[:in]->(oceans13),
       (mac: Actor {character:"Frank Catton", name: "Bernie Mac", nickname: "mac"})-[:in]->(oceans13),
       (gould: Actor {character:"Reuben Tishkoff", name: "Elliott Gould", nickname: "gould"})-[:in]->(oceans13),
       (affleck: Actor {character:"Virgil Malloy", name: "Casey Affleck", nickname: "affleck"})-[:in]->(oceans13),
       (caan: Actor {character:"Turk Malloy", name: "Scott Caan", nickname: "caan"})-[:in]->(oceans13),
       (jemison: Actor {character:"Livingston Dell", name: "Eddie Jemison", nickname: "jemison"})-[:in]->(oceans13),
       (qin: Actor {character:"The Amazing Yen", name: "Shaobo Qin", nickname: "qin"})-[:in]->(oceans13),
       (reiner: Actor {character:"Saul Bloom", name: "Carl Reiner", nickname: "reiner"})-[:in]->(oceans13),
       (izzard: Actor {character:"Roman Nagel", name: "Eddie Izzard", nickname: "izzard"})-[:in]->(oceans13)

// Ocean's 12 
CREATE (oceans12: Movie {name:"Ocean's 12", released: "2004"})

MATCH (u:Actor {nickname:'clooney'}), (r:Movie {name:"Ocean's 12"})
CREATE (u)-[:in]->(r)

MATCH (pitt:Actor {nickname:'pitt'}), (damon:Actor {nickname:'damon'}), (r:Movie {name:"Ocean's 12"})
CREATE (pitt)-[:in]->(r), (damon)-[:in]->(r)

MATCH (gould:Actor {nickname:'gould'}), (affleck:Actor {nickname:'affleck'}), (r:Movie {name:"Ocean's 12"})
CREATE (gould)-[:in]->(r), (affleck)-[:in]->(r)

MATCH (caan:Actor {nickname:'caan'}), (jemison:Actor {nickname:'jemison'}), (r:Movie {name:"Ocean's 12"})
CREATE (caan)-[:in]->(r), (jemison)-[:in]->(r)

MATCH (cheadle:Actor {nickname:'cheadle'}), (qin:Actor {nickname:'qin'}), (r:Movie {name:"Ocean's 12"})
CREATE (cheadle)-[:in]->(r), (qin)-[:in]->(r)

MATCH (reiner:Actor {nickname:'reiner'}), (mac:Actor {nickname:'mac'}), (r:Movie {name:"Ocean's 12"})
CREATE (reiner)-[:in]->(r), (mac)-[:in]->(r)

CREATE (roberts: Actor {character:"Tess Ocean", name: "Julia Roberts", nickname: "roberts"})

MATCH (u:Actor {nickname:'roberts'}), (r:Movie {name:"Ocean's 12"})
CREATE (u)-[:in]->(r)

// Ocean's 11
CREATE (oceans11: Movie {name:"Ocean's 11", released: "2001"})

MATCH (clooney:Actor {nickname:'clooney'}), (pitt:Actor {nickname:'pitt'}), (damon:Actor {nickname:'damon'}), (cheadle:Actor {nickname:'cheadle'}), (mac:Actor {nickname:'mac'}),(caan:Actor {nickname:'caan'}), (affleck:Actor {nickname:'affleck'}), (reiner:Actor {nickname:'reiner'}), (gould:Actor {nickname:'gould'}),  (jemison:Actor {nickname:'jemison'}), (qin:Actor {nickname:'qin'}), (garcia:Actor {nickname:'garcia'}),  (roberts:Actor {nickname:'roberts'}), (r:Movie {name:"Ocean's 11"})
CREATE (clooney)-[:in]->(r), (pitt)-[:in]->(r), (damon)-[:in]->(r), (cheadle)-[:in]->(r), (mac)-[:in]->(r), (caan)-[:in]->(r), (affleck)-[:in]->(r), (reiner)-[:in]->(r), (gould)-[:in]->(r), (jemison)-[:in]->(r), (qin)-[:in]->(r), (garcia)-[:in]->(r), (roberts)-[:in]->(r)

// Ocean's 8
CREATE (oceans8: Movie {name:"Ocean's 8", released: "2018"})

MATCH (reiner:Actor {nickname:'reiner'}), (damon:Actor {nickname:'damon'}), (r:Movie {name:"Ocean's 8"})
CREATE (reiner)-[:in]->(r), (damon)-[:in]->(r)

MATCH (r:Movie {name:"Ocean's 8"})
CREATE (bullock: Actor {character: "Debbie Ocean", name: "Sandra Bullock", nickname: "bullock"})-[:in]->(r),
       (blanchett: Actor {character:"Lou", name: "Cate Blanchett", nickname: "blanchett"})-[:in]->(r), 
       (carter: Actor {character:"Rose", name: "Helena Bonham Carter", nickname: "carter"})-[:in]->(r), 
       (hathaway: Actor {character:"Daphne Kluger", name: "Anne Hathaway", nickname: "hathaway"})-[:in]->(r), 
       (rihanna: Actor {character:"Nine Ball", name: "Rihanna", nickname: "rihanna"})-[:in]->(r), 
       (kaling: Actor {character:"Amita", name: "Mindy Kaling", nickname: "kaling"})-[:in]->(r), 
       (paulson: Actor {character:"Tammy", name: "Sarah Paulson", nickname: "paulson"})-[:in]->(r), 
       (awkwafina: Actor {character:"Constance", name: "Awkwafina", nickname: "awkwafina"})-[:in]->(r)

// Degree of graph
START n = node(*) 
MATCH (n)--(c)
RETURN n, count(*) as connections
ORDER BY connections DESC
LIMIT 10

// Number of movies per actor
MATCH (actor:Actor)-[:in]->(movie:Movie) 
RETURN actor.name, COUNT(actor) AS actor
ORDER BY actor DESC