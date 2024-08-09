print("getting used to vs code via its terminal   ->   found that when we create a file via the terminal like add a few text and then create it it uses utf-16 format.")


from fastapi import FastAPI

def full_name(first:str,last:str): # attribute error since said as int but psasing str.?works but typehints this ensures or doc purpose only
    # last. ok got it so when we declare type hints it helps with the docs i int it suggests int function then tat var is used when str is specfied it gives str funcs
    # we can also set possible types like it can accpet both the str and int by using the union | operator (int | str)
    return first.title() +" "+ last.title().lstrip() + "       "+ " heyyy   "
 

first = 'finraaaal'
last = 'voilaen     '

print(full_name(first,last))

van = first.count('a')
print(van)
fullly = None
if fullly:
    print("Maga")
else:
    print("Sala")


#pass no-op statement
#none statement return and stuff.
# instead of using optional we can use some_type, None so like kinda valid la but only on 3.8+ so nnah  don't
# : type hints is diff than = assigning as like default
# lf(unix ending line feed \n) converted to crlf (windows based carriage return line feed \r\n)
