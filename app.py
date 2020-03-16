from flask import Flask, render_template, request, redirect, url_for
from data import dummydata
from flask_mysqldb import MySQL
from data import info
import os


app = Flask(__name__) #__name__ is for best practice

app.config["MYSQL_HOST"] = info.MySQLhost
app.config["MYSQL_USER"] = info.MySQLuser
app.config["MYSQL_PASSWORD"] = info.MySQLpassword
app.config["MYSQL_DB"] = info.MySQLdb


mysql = MySQL(app)

######################################################################################################################################################################
############################################################################     HOME     ############################################################################
######################################################################################################################################################################

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Actors")
    mysql.connection.commit()
    actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT * FROM Films")
    mysql.connection.commit()
    filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    actorselection = []
    filmselection = []

    for row in actornames:
        actorselection.append(row) #adding each row from the database into a newly created list, info  
    
    for row in filmnames:
        filmselection.append(row) #adding each row from the database into a newly created list, info 

    return render_template("index.html", name="Home", actorselection=actorselection, filmselection=filmselection)


@app.route('/home/actors/search', methods=['GET', 'POST']) # Delete function
def actors_search():
    if request.method == "POST":
        details=request.form
        actors=details['actors']
        if actors != "- Choose an Actor -":
            cur = mysql.connection.cursor()
            cur.execute("select Film_Name from Films where Film_ID in (select FilmID from Film_Actor where ActorID=(SELECT Actor_ID from Actors WHERE Actor_Name=(%s)))", [actors])
            mysql.connection.commit()
            selectfilmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.execute("SELECT * FROM Actors")
            mysql.connection.commit()
            actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.execute("SELECT * FROM Films")
            mysql.connection.commit()
            filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.close()

            filmchoice = []

            for row in selectfilmnames:
                filmchoice.append(row) #adding each row from the database into a newly created list, info  

            filmselection = []

            for row in filmnames:
                filmselection.append(row) #adding each row from the database into a newly created list, info 

            actorselection = []

            for row in actornames:
                actorselection.append(row) #adding each row from the database into a newly created list, info  

            return render_template("index.html", name="Home", actor="Films starring "+actors+":", filmchoice=filmchoice, actorselection=actorselection, filmselection=filmselection)
    return redirect(url_for('home'))


@app.route('/home/films/search', methods=['GET', 'POST']) # Delete function
def films_search():
    if request.method == "POST":
        details=request.form
        films=details['films']
        if films != "- Choose a Film -":
            cur = mysql.connection.cursor()
            cur.execute("select Actor_Name from Actors where Actor_ID in (select ActorID from Film_Actor where FilmID=(SELECT Film_ID from Films WHERE Film_Name=(%s)))", [films])
            mysql.connection.commit()
            selectactornames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.execute("SELECT * FROM Films")
            mysql.connection.commit()
            filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.execute("SELECT * FROM Actors")
            mysql.connection.commit()
            actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.close()

            actorchoice = []

            for row in selectactornames:
                actorchoice.append(row) #adding each row from the database into a newly created list, info  
            
            actorselection = []

            for row in actornames:
                actorselection.append(row) #adding each row from the database into a newly created list, info

            filmselection = []

            for row in filmnames:
                filmselection.append(row) #adding each row from the database into a newly created list, info  

            return render_template("index.html", name="Home", film="Actors starring in "+films+":", actorchoice=actorchoice, actorselection=actorselection, filmselection=filmselection)
    return redirect(url_for('home'))


@app.route('/home/link', methods=['GET', 'POST']) # Delete function
def actor_film_associate():
    if request.method == "POST":
        details=request.form
        films=details['filmname']
        actors=details['actorname']
        if films != "- Choose a Film -" and actors != "- Choose an Actor -":
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name=(%s)), (SELECT Actor_ID from Actors WHERE Actor_Name=(%s)));", [films, actors])
            mysql.connection.commit()
            cur.execute("select Actor_Name from Actors where Actor_ID in (select ActorID from Film_Actor where FilmID=(SELECT Film_ID from Films WHERE Film_Name=(%s)))", [films])
            mysql.connection.commit()
            selectactornames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.execute("SELECT * FROM Films")
            mysql.connection.commit()
            filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.execute("SELECT * FROM Actors")
            mysql.connection.commit()
            actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.close()

            actorchoice = []

            for row in selectactornames:
                actorchoice.append(row) #adding each row from the database into a newly created list, info  
            
            actorselection = []

            for row in actornames:
                actorselection.append(row) #adding each row from the database into a newly created list, info

            filmselection = []

            for row in filmnames:
                filmselection.append(row) #adding each row from the database into a newly created list, info  

            return render_template("index.html", name="Home", film="Actors starring in "+films+":", actorchoice=actorchoice, actorselection=actorselection, filmselection=filmselection)
    return redirect(url_for('home'))

    

######################################################################################################################################################################
###########################################################################     ACTORS     ###########################################################################
######################################################################################################################################################################

@app.route('/actors', methods=['GET', 'POST']) # Read Function
def actors():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Actors")
    mysql.connection.commit()
    actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    actorselection = []

    for row in actornames:
        actorselection.append(row) #adding each row from the database into a newly created list, info  

    return render_template("actors.html", name="Actor Database", actorselection=actorselection)

@app.route('/actors/create', methods=['GET', 'POST']) # Create function
def actors_create():
    if request.method == "POST":
        details=request.form
        name=details['name']
        if name != "":
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Actors (Actor_Name) VALUES (%s)", [name])
            mysql.connection.commit()
            cur.close()

    return redirect(url_for('actors'))


@app.route('/actors/delete', methods=['GET', 'POST']) # Delete function
def actors_delete():
    if request.method == "POST":
        details=request.form
        actors=details['actors']
        if actors != "- Choose an Actor -":
            cur=mysql.connection.cursor()
            cur.execute("DELETE Actors, Film_Actor FROM Actors INNER JOIN Film_Actor ON Actors.Actor_ID = Film_Actor.ActorID WHERE Actors.Actor_Name=(%s)", [actors])
            cur.execute("DELETE FROM Actors WHERE Actor_Name = (%s)", [actors]) #works in GCP SQL
            mysql.connection.commit()
            cur.close()
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM Actors")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    
    return redirect(url_for('actors'))
    
 

@app.route('/actors/update', methods=['GET', 'POST']) # Update function
def actors_update():
    if request.method == "POST":
        details=request.form
        fromname=details['initialname']
        toname=details['finalname']
        if fromname != "- Choose an Actor -":
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Actors SET Actor_Name=(%s) WHERE Actor_Name=(%s)", [toname, fromname])
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('actors'))

    return redirect(url_for('actors'))

#######################################################################################################################################################################
############################################################################     FILMS     ############################################################################
#######################################################################################################################################################################


@app.route('/films', methods=['GET', 'POST']) # Read Function
def films():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Films")
    mysql.connection.commit()
    filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    filmselection = []

    for row in filmnames:
        filmselection.append(row) #adding each row from the database into a newly created list, info  

    return render_template("films.html", name="Film Database", filmselection=filmselection)

@app.route('/films/create', methods=['GET', 'POST']) # Create function
def films_create():
    if request.method == "POST":
        details=request.form
        name=details['name']
        if name != "Choose a Film":
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Films (Film_Name) VALUES (%s)", [name])
            mysql.connection.commit()
            cur.close()

    return redirect(url_for('films'))


@app.route('/films/delete', methods=['GET', 'POST']) # Delete function
def films_delete():
    if request.method == "POST":
        details=request.form
        films=details['films']
        if actors != "- Choose a Film -":
            cur=mysql.connection.cursor()
            cur.execute("DELETE Films, Film_Actor FROM Films INNER JOIN Film_Actor ON Films.Film_ID = Film_Actor.FilmID WHERE Films.Film_Name=(%s)", [films])
            cur.execute("DELETE FROM Films WHERE Film_Name = (%s)", [films]) #works in GCP SQL
            mysql.connection.commit()
            cur.close()
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM Films")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    
    return redirect(url_for('films'))
 

@app.route('/films/update', methods=['GET', 'POST']) # Update function
def films_update():
    if request.method == "POST":
        details=request.form
        fromname=details['initialname']
        toname=details['finalname']
        if fromname != "" and toname != "":
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Films SET Film_Name=(%s) WHERE Film_Name=(%s)", [toname, fromname])
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('films'))

    return redirect(url_for('films'))

#######################################################################################################################################################################
############################################################################     MISC.     ############################################################################
#######################################################################################################################################################################

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)