#pysports_update_and_delete.py
b = mysql.connector.connect
    host = "localhost"
    user = "root"
    passwd = "..."
    database = "pysports"
cursor = db.cursor()

INSERT INTO player (first_name, last_name, team_name)
    VALUES('Luke','Team Gandalf',1)

SELECT player_id, first_name, last_name, team_name
FROM player
INNER JOIN team
    ON player.team_neam = team.team_name;

UPDATE player
SET team_id 2
    first_name = 'Luke
    last_name = 'Skywalker'
WHERE first_name = 'Luke';

query = "SELECT team_id, team_name,"
cursor.execture(query)

DELETE FROM player
WHERE first_name = 'Luke'; 

query = "SELECT team_id, team_name,"
cursor.execture(query)
