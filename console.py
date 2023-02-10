#!/usr/bin/python3
"""

console for AirBnB clone

"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import json

classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}

class HBNBCommand(cmd.Cmd):
    """
    console main class
    """
    prompt = "(hbnb) "

    def do_EOF(self, args):
        "Quit the console - Usage: EOF\n"
        print("")
        return True

    def do_quit(self, args):
        "Quit command to exit the program\n"
        return (True)

    def emptyline(self):
        "Does not perform any action"
        pass

    def do_create(self, args):
        """Create a new instance - Usage: create <Classname>\n"""
        if args is None or len(args) == 0:
            print("** Class name missing **")
        else:
            if args in classes:
                new = eval(str(args) + "()")
                new.save()
                print(new.id)
            else:
                print("** Class doesn't exist **")

    def do_show(self, args):
        """Show the representation of an instance - Usage show <Classname>\n"""
        if args is None or len(args) == 0:
            print("** Class name is missing **")
        else:
            line = args.split()
            if line[0] in classes:
                if len(line) < 2:
                    print("""** instance id missing **""")
                else:
                    objects = models.storage.all()
                    key = str(line[0]) + "," + str(line[1])























