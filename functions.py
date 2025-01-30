def get_todos(filepath='Todos.txt'):   # kreirame funkcija koja kje go cita fileot so Parametar.
    """ Read the saved Todo List and assign it to the variable todos.  """  #Doc String
    with open(filepath , 'r') as file:
        todos = file.readlines()    # mnogu poprofi e vaka
    return todos     # koj rezultat da go vrati taa funckija


def write_todos(todos_arg, filepath='Todos.txt' ):
    """ Saves the new Todo list. """  #Doc String
    with open(filepath, 'w') as file:  # zapishuvanje na nov file so skraten metod (WITH)
        file.writelines(todos_arg)
# se preporacuva minium dva reda pomegju funkcii

if __name__ == "__main__":
    print("Hello from functions")   # ova moze da e informativno da znaeme od koj modul go startame kodot.