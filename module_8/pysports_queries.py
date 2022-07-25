#pysports_queries.py
#not putting my actual password in here as it's used in other places
db = mysql.connector.connect
    host = "localhost"
    user = "root"
    passwd = "..."
    database = "pysports"
cursor = db.cursor()
    
query = "SELECT team_id, team_name, mascot FROM team"
cursor.execture(query)

teams = "cursor.fetchall"

print(team)

for team in teams:
    print("Team Name: {}".format(team[1]))

cursor.close

db.close()

