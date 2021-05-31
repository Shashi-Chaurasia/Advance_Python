# *args and **kwargs     uses


def Animal(*args):
    if(len(args) == 3):
        print(f"Name of animal is :" , *args[0]  , "  ,  bread : " , *args[1] , " , color 👎 " , args[2])
    else:
        print(f"Name of animal is :" , *args[0]  , "  ,  bread : " , *args[1])


def studentPerformance(**kwargs):
    for key, value in kwargs.items():
        print(key , value)



marks_list = {"Shashi" : 98 , "Vinita" : 99 , "Chandan" : 78 , "Sanjay" : 100  , "AShutosh" : 76}

studentPerformance(
    **marks_list
)

# newAnimal = ["tommy" , "gernam"]

# Animal(*newAnimal)