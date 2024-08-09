from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Optional
from enum import Enum

app = FastAPI()

#first using path parameters alone to make this work
class Players(BaseModel):
     id : int
     name : str
     age : int     

class UpdatePlayers(BaseModel):
     name : Optional[str] = None
     age : Optional[int] = None

class Restrict_Name(str,Enum):
     arun = "arun"
     tilak = "tilak"

entry = {}

@app.get("/getbyID/{id}")
def  getby_ID(id : int = Path(description="The Player's ID : ",lt=11,le=10)):
    if id in entry:
         return entry[id]
    else:
          return "Error : ID not available"

@app.get("/getbyName/{name}")
def getbyName(name : str = Path(description="The Player's Name : ")):
     for in_name in entry.values():
          if name in in_name.values(): #if name == in_name.get("name"): this ya this will work 
               return in_name #entry[name] wont work bcause it contains o type {int : {} } 

@app.post("/addPlayer/")
def addPlayer(player : Players):
     entry[player.id] =  player.model_dump()
     print("successfully added ... ")
     response = {
          "message":"This was the item that was added.",
          "item": entry[player.id]
     }
     return response #entry[player.id] returning this only gives the resposne body  but with this response dict we can add a message i thinnk there is no other way to add a message to the post method or a print method.

@app.put("/updatePlayer/{id}")
def updatePlayerDetails(id : int,player : UpdatePlayers):
     if id not in entry:
          return "Error : ID not found (inside Update EndPoint)"           # entry[id] = player.model_dump()
                                                                           # return "inside"
     # if player.name != None:
     #      entry[id]['name'] = player.name
     # if player.age != None:
     #      entry[id]['age'] = player.age

     # entry[id] = player                                   # this replaces the entire data with whats given and wats it set to default so be careful
     # here i have assigned the basemodel instance to a dictionary and then compared tthe keys of the new dict and the existing dict to update this reduces the no. of lines but i wanna try this without converting the bm to dict papom.
     ran = player.model_dump() #exclude_unset=True
     for i in ran:
          if ran[i] is not None:                                          # entry[id].keys():
               entry[id][i] = ran[i]
               print("Successfully updated.!")

     # ok so i tried the update method but it also does the same thing like it only assigns the new value and sets others to null hehe my solu's stands tall just kidding lets see another method.
     # ok am wrong when i use exclude_unset = true with the dict that i converted it removes the null or not updated values nice so ya but not intresting like mine 
     # entry[id].update(ran)
     # print("successfully upated.~")
     return entry[id]

@app.delete("/delete/{id}")
def deletePlayer(id : int):
     if id not in entry:
          return "Error : ID not present"
     
     del entry[id]
     return "Successfully deleted"

@app.post("/getPlayers")
def displayPlayers():
     return entry