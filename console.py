#!/usr/bin/python3
import cmd
import re
from shlex import split

import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ General class for HBNBCommand """
    prompt = '(hbnb)'
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
            'place': place, 'Amenity': Amenity, 'Review': Review,
            'state': state}
    def do quit(self, arg):
        """ Exit method for quit typing """
        exit ()

        def do_EOF(self, arg):
            """
            Exit method for EOF """
            print('')
            exit ()
            
      def emptyline(self):
          """ Method to pass when emptyline entered """
          pass
      def do_create(self, arg):
          """ Create a new instance """
          if len(arg) == 0:
              print('** class name missing **')
              return
          new = None
          if arg:
              arg_list = arg.split()
              if len(arg_list) == 1:
                  if arg in self.classess.keys():
                      new = self.classes[arg]()
                      new.save()
                      print(new.id)
                  else:
                      print("**class doesn't exist **")
    def do_show(self, arg):
        """ Method to print instance """
        if len(arg) == 0:
            print('**class name missing **')
            return
        elif arg.split()[0] not in self.classes:
            print("**class doesn't exits **")
            return
        elif len(arg.split()) > 1:
