"""
This module contains command for create files types and files extensions in FileExtension and FileTypes tables from storageapp
"""
from django.core.management.base import BaseCommand


"""
This module is used to create tables in the database.
"""
from times.models import Times

SRC = {"past simple": "text of rule"}
def create_tables():
    """
    The create_tables function creates the tables in the database.
    It is called by manage.py when you run python manage.py create_storageapp_tables

    :return: Nothing
    """
    for time, rule in SRC.items():
        Times.objects.create(name=time, rule=rule)



class Command(BaseCommand):
    """
    This class contains command for create files types and files extensions in FileExtension and FileTypes tables from storageapp
    """
    help = ''

    def handle(self, *args, **options):
        """
        The handle function is the entry point for a Django management command.
        It's called by the manage.py script when you run python manage.py &lt;command&gt;
        from your project directory.

        :param self: Represent the instance of the class
        :param args: Pass a variable number of arguments to a function
        :param options: Pass in the options that are passed to the command
        :return: A string that is printed in the console
        """
        create_tables()
