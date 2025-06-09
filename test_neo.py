from neo4j import GraphDatabase

URI = "neo4j+s://ea5b80d2.databases.neo4j.io"  
USERNAME = "neo4j"
PASSWORD = "OMaKwSR0X5bEBrrUSV9jRGDfJCmWuUB0p8mq3NgDtnI"  

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

try:
    with driver.session() as session:
        result = session.run("RETURN 'AuraDB connected!' AS message")
        print(result.single()["message"])
except Exception as e:
    print("Connection failed:", e)
