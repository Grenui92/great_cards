"""
This module contains command for create files types and files extensions in FileExtension and FileTypes tables from storageapp
"""
from django.core.management.base import BaseCommand


"""
This module is used to create tables in the database.
"""
from times.models import Times

SRC = (
    (
        "Past Simple",
        "Действие совершалось/совершилось",
        (
            "I talked to Jhon yesterday.",
            "I did not talk to John yesterday.",
            "Did you talk to John yesterday?",
        ),
    ),
    (
        "Past Continuous",
        "Действие совершилос (точное время)",
        (
            "I was talking to Jhon yrsterday when you called me.",
            "I was not talking to John yesterday when you called me.",
            "Were you talking to John yesterday when I called you?",
        ),
    ),
    (
        "Past Perfect",
        "Действие совершилось ранее другого действия",
        (
            "I had talked to Jhon by the time you came.",
            "I had not talked to John by the time you cam",
            "Had you talked to John by the time I came?",
        ),
    ),
    (
        "Past Perfect Continuous",
        "Начатое действие продолжалось до (веремени/действия)",
        (
            "I had been talking to Jhon for two hours by the time you came / by 5 o'clock.",
            "I had not been talking to John for two hours by the time you came / by 5 o'clock.",
            "Had you been talking to John for two hours by the time I came / by 5 o'clock?",
        ),
    ),
    (
        "Present Simple",
        "Действие совершается постоянно",
        (
            "I talk to Jhon yesterday.",
            "I did not talk to John yesterday.",
            "Did you talk to John yesterday?",
        ),
    ),
    (
        "Present Continuous",
        "Дкйствие совершается сейчас",
        (
            "I am talking to Jhon now.",
            "I am not talking to Jhon now.",
            "Are you talking to John now?",
        ),
    ),
    (
        "Present Perfect",
        "Действие совершилось",
        (
            "I have talked to Jhon.",
            "I have not talked to John.",
            "Have you talked to John?",
        ),
    ),
    (
        "Present Perfect Continuous",
        "Начатое действие продолжается",
        (
            "I have been talking to Jhon for two hours / since 5 o'clock.",
            "I have not been talking to John for two hours / since 5 o'clock.",
            "Have you been talking to John for two hours / since 5 o'clock?",
        ),
    ),
    (
        "Future Simple",
        "Действие совершится",
        (
            "I will talk to Jhon tomorrow.",
            "I will not talk to John tomorrow.",
            "Will you talk to John tomorrow?",
        ),
    ),
    (
        "Future Continuous",
        "Действие будет совершаться (точное время / действие)",
        (
            "I will be talking to Jhon tomorrow at 5 / when you call me.",
            "I will not be talking to John tomorrow at 5 / when you call me.",
            "Will you be talking to John tomorrow at 5 / when I call you?",
        ),
    ),
    (
        "Future Perfect",
        "Дкйствие совершится ранее другого действия",
        (
            "I will have talked to Jhon by time you come.",
            "I will not have talked to John by the time you come.",
            "Will you have talked to John by the time I come?",
        ),
    ),
    (
        "Future Perfect Continuous",
        "Начатое действие будет продолжаться до (времен/действия)",
        (
            "I will have been talkin to Jhon for two hours by the time you come / by 5 o'clock.",
            "I will not have been talking to John for two hours by the time you come / by 5 o'clock.",
            "Will you have been talking to John for two hours by the time I come / by 5 o'clock?",
        ),
    ),
)


verbs = {
    "Past Simple": (
        (("I", "He", "She", "It"), ("<2nd form of the verb>", "<did not> + <1st form of the verb>")),
        (("We", "You", "They"), ("<2nd form of the verb>", "<did not> + <1st form of the verb>"))
    ),
    "Past Continuous": (
        (("I", "He", "She", "It"), ("<was> <verb+'ing>", "<was not> + <verb'ing>")),
        (("We", "You", "They"), ("<were> <verb+'ing>", "<were not> + <verb'ing>"))
    ),
    "Past Perfect": (
        (("I", "He", "She", "It"), ("<had> + <3rd form of the verb>", "<had not> + <3rd form of the verb>")),
        (("We", "You", "They"), ("<had> + <3rd form of the verb>", "<had not> + <3rd form of the verb>"))
    ),
    "Past Perfect Continuous": (
        (("I", "He", "She", "It"), ("<had been> + <verb'ing>", "<had not been> + <verb'ing>")),
        (("We", "You", "They"), ("<had been> + <verb'ing>", "<had not been> + <verb'ing>"))
    ),
    "Present Simple": (

    ),
    "Present Continuous": (

    ),
    "Present Perfect": (

    ),
    "Present Perfect Continuous": (

    ),
    "Future Simple": (

    ),
    "Future Continuous": (

    ),
    "Future Perfect": (

    ),
    "Future Perfect Continuous": (

    )
}


def create_tables():
    """
    The create_tables function creates the tables in the database.
    It is called by manage.py when you run python manage.py create_storageapp_tables

    :return: Nothing
    """
    for row in SRC:
        Times.objects.create(name=row[0], rule=row[1], examples=row[2])


class Command(BaseCommand):
    """
    This class contains command for create files types and files extensions in FileExtension and FileTypes tables from storageapp
    """

    help = ""

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
