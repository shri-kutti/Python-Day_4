from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Optional
# from enum import Enum
# adding imports for stream lit
import mysql.connector

app = FastAPI()

mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="user",
     database="crud_new"
)

# if mydb.is_connected():
#      print("successfull")
# else :
#      print("check the details on connect and verify mysql.")
mycursor = mydb.cursor()  # to create a cursor obj from a mysql_db_connector obj(my_db) in python helps in exe qris & retriving results frm db
print("succes fu; db connection")

# noice done my db connection


#first using path parameters alone to make this work
class Players(BaseModel):
     id : int
     name : str
     age : int     

class UpdatePlayers(BaseModel):
     name : Optional[str] = None
     age : Optional[int] = None

# class Restrict_Name(str,Enum):
#      arun = "arun"
#      tilak = "tilak"

entry = {}

@app.get("/getbyID/{id}")
def  getby_ID(id : int = Path(description="The Player's ID : ",lt=11,le=10)):
#     if id in entry:
#          return entry[id]
#     else:
#           return "Error : ID not available"
     #ymsql to get data based on id
     sql = "select * from sp_players where id = %s"
     val = (id,)
     mycursor.execute(sql,val)
     result = mycursor.fetchone()
     mydb.commit()
     print("given data successfully")
     return result


@app.get("/getbyName/{name}")
def getbyName(name : str = Path(description="The Player's Name : ")):
     # for in_name in entry.values():
     #      if name in in_name.values(): #if name == in_name.get("name"): this ya this will work 
     #           return in_name #entry[name] wont work bcause it contains o type {int : {} } 

     # sql to get data from db based on name
     sql = "select * from sp_players where name = %s"
     val = (name,)
     mycursor.execute(sql,val)
     result = mycursor.fetchone()
     mydb.commit()
     print("given data successfully")
     return result

@app.post("/addPlayer/")
def addPlayer(player : Players):
     entry[player.id] =  player.model_dump()
     print("successfully added ... ")

     #mysql functions and bla bla to add the given data from endpt to db >~<
     sql = "insert into sp_players(name,age) values(%s,%s)"
     val = (entry[player.id]["name"],entry[player.id]["age"]) # dammmnn am dumb i could directly sent the data to db but ya am gonna go this wayeee
     mycursor.execute(sql,val) #prev mycursor.execute("SELECT bla bla bla ") now sq,val u know advanced u dont know hhehe
     mydb.commit()
     print("successfully added to db~!")

     response = {
          "message":"This was the item that was added.",
          "item": entry[player.id]
     }
     return response #entry[player.id] returning this only gives the resposne body  but with this response dict we can add a message i thinnk there is no other way to add a message to the post method or a print method.

@app.put("/updatePlayer/{id}")
def updatePlayerDetails(id : int,player : UpdatePlayers):
     sql = "select * from sp_players where id = %s"
     val = (id,)
     mycursor.execute(sql,val)
     check = mycursor.fetchone()
     mydb.commit()
     if check:
          print("is in there")
          sql = "update sp_players set name = %s where id = %s"
          # print(player) returns name='asmeen' age = None
          val = (player.name,id) #player.name --> asmeen
          mycursor.execute(sql,val)
          check = mycursor.fetchone() # dumb bruh ur update does no retrun so what are u gonna check phssh
          mydb.commit()
          if check:
               return check
          return check
     else: 
          print("id not there")
          check = None
          return "is not in there"
     
     
     # if id not in entry:
     #      return "Error : ID not found (inside Update EndPoint)"           # entry[id] = player.model_dump()
                                                                             # return "inside"
     # if player.name != None:
     #      entry[id]['name'] = player.name
     # if player.age != None:
     #      entry[id]['age'] = player.age

     # entry[id] = player                                   # this replaces the entire data with whats given and wats it set to default so be careful
     # here i have assigned the basemodel instance to a dictionary and then compared tthe keys of the new dict and the existing dict to update this reduces the no. of lines but i wanna try this without converting the bm to dict papom.
     # ran = player.model_dump() #exclude_unset=True
     # for i in ran:
     #      if ran[i] is not None:                                          # entry[id].keys():
     #           entry[id][i] = ran[i]
     #           print("Successfully updated.!")

     # ok so i tried the update method but it also does the same thing like it only assigns the new value and sets others to null hehe my solu's stands tall just kidding lets see another method.
     # ok am wrong when i use exclude_unset = true with the dict that i converted it removes the null or not updated values nice so ya but not intresting like mine 
     # entry[id].update(ran)
     # print("successfully upated.~")
     # return entry[id]

@app.delete("/delete/{id}")
def deletePlayer(id : int):
     # if id not in entry:
     #      return "Error : ID not present"
     #mysql functions and bla bla to delete the given data from endpt to db *-*
     sql = "delete from sp_players where id = %s"
     val = (id,) #entry[id]['id']
     mycursor.execute(sql,val)
     mydb.commit()
     print("succes fuly deleted")

     # del entry[id]
     return "Successfully deleted"

@app.post("/getPlayers")
def displayPlayers():
     #mysql functions and bla bla to retrive data from db <->
     mycursor.execute("select * from sp_players")
     result = mycursor.fetchall()
     # return entry
     return result