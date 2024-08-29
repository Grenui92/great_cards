"""This module contains command for create files types and files extensions
in FileExtension and FileTypes tables from storageapp
"""
from times.models import Times, Verbs
from django.core.management.base import BaseCommand

from tools.logger import logger

"""This module is used to create tables in the database."""

SRC = (
    (
        "Past Simple",
        "Действие совершалось/совершилось",
        (
            "I talked to John yesterday.",
            "I did not talk to John yesterday.",
            "Did you talk to John yesterday?",
        ),
    ),
    (
        "Past Continuous",
        "Действие совершилос (точное время)",
        (
            "I was talking to John yrsterday when you called me.",
            "I was not talking to John yesterday when you called me.",
            "Were you talking to John yesterday when I called you?",
        ),
    ),
    (
        "Past Perfect",
        "Действие совершилось ранее другого действия",
        (
            "I had talked to John by the time you came.",
            "I had not talked to John by the time you cam",
            "Had you talked to John by the time I came?",
        ),
    ),
    (
        "Past Perfect Continuous",
        "Начатое действие продолжалось до (веремени/действия)",
        (
            "I had been talking to John for two hours by the time you came / by 5 o'clock.",
            "I had not been talking to John for two hours by the time you came / by 5 o'clock.",
            "Had you been talking to John for two hours by the time I came / by 5 o'clock?",
        ),
    ),
    (
        "Present Simple",
        "Действие совершается постоянно",
        (
            "I talk to John every day.",
            "I do not talk to John every day.",
            "Do I talk to John every day?",
        ),
    ),
    (
        "Present Continuous",
        "Действие совершается сейчас",
        (
            "I am talking to John now.",
            "I am not talking to John now.",
            "Are you talking to John now?",
        ),
    ),
    (
        "Present Perfect",
        "Действие совершилось",
        (
            "I have talked to John.",
            "I have not talked to John.",
            "Have you talked to John?",
        ),
    ),
    (
        "Present Perfect Continuous",
        "Начатое действие продолжается",
        (
            "I have been talking to John for two hours / since 5 o'clock.",
            "I have not been talking to John for two hours / since 5 o'clock.",
            "Have you been talking to John for two hours / since 5 o'clock?",
        ),
    ),
    (
        "Future Simple",
        "Действие совершится",
        (
            "I will talk to John tomorrow.",
            "I will not talk to John tomorrow.",
            "Will you talk to John tomorrow?",
        ),
    ),
    (
        "Future Continuous",
        "Действие будет совершаться (точное время / действие)",
        (
            "I will be talking to John tomorrow at 5 / when you call me.",
            "I will not be talking to John tomorrow at 5 / when you call me.",
            "Will you be talking to John tomorrow at 5 / when I call you?",
        ),
    ),
    (
        "Future Perfect",
        "Действие совершится ранее другого действия",
        (
            "I will have talked to John by time you come.",
            "I will not have talked to John by the time you come.",
            "Will you have talked to John by the time I come?",
        ),
    ),
    (
        "Future Perfect Continuous",
        "Начатое действие будет продолжаться до (времен/действия)",
        (
            "I will have been talkin to John for two hours by the time you come / by 5 o'clock.",
            "I will not have been talking to John for two hours by the time you come / by 5 o'clock.",
            "Will you have been talking to John for two hours by the time I come / by 5 o'clock?",
        ),
    ),
)


VERBS = {
    "Past Simple": (
        (("I", "We", "You", "They"),
         ("<2nd form of the verb>",
          "<did not> + <1st form of the verb>",
          "<Did> + <subject> + <1st form of the verb>?")),
        (("He", "She", "It"), ("<2nd form of the verb>",
                               "<did not> + <1st form of the verb>",
                               "<Did> + <subject> + <1st form of the verb>?"))
    ),
    "Past Continuous": (
        (("I", "He", "She", "It"),
         ("<was> + <verb'ing>",
          "<was not> + <verb'ing>",
          "<Was> + <subject> + <verb'ing>?")),
        (("We", "You", "They"),
         ("<were> <verb+'ing>",
          "<were not> + <verb'ing>",
          "<Were> + <subject> + <verb'ing>?"))
    ),
    "Past Perfect": (
        (("I", "We", "You", "They"),
         ("<had> + <3rd form of the verb>",
          "<had not> + <3rd form of the verb>",
          "<Had> + <subject> + <3rd form of the verb>?")),
        (("He", "She", "It"),
         ("<had> + <3rd form of the verb>",
          "<had not> + <3rd form of the verb>",
          "<Had> + <subject> + <3rd form of the verb>?"))
    ),
    "Past Perfect Continuous": (
        (("I", "We", "You", "They"),
         ("<had been> + <verb'ing>",
          "<had not been> + <verb'ing>",
          "<Had> + <subject> + <been> <verb'ing>?")),
        (("He", "She", "It"),
         ("<had been> + <verb'ing>",
          "<had not been> + <verb'ing>",
          "<Had> + <subject> + <been> <verb'ing>?"))
    ),
    "Present Simple": (
        (("I", "We", "You", "They"),
         ("<1st form of the verb>",
          "<do not> + <1st form of the verb>",
          "<Do> + <subject> + <1st form of the verb>?")),
        (("He", "She", "It"),
         ("<1st form of the verb>+s/es",
          "<does not> + <1st form of the verb>",
          "<Does> + <subject> + <1st form of the verb>?"))
    ),
    "Present Continuous": (
        (("I"),
         ("<am> + <verb'ing>",
          "<am not> + <verb'ing>",
          "<Am> + <subject> + <verb'ing>?")),
        (("We", "You", "They"),
         ("<are> + <verb'ing>",
          "<are not> + <verb'ing>",
          "<Are> + <subject> + <verb'ing>?")),
        (("He", "She", "It"),
         ("<is> + <verb'ing>",
          "<is not> + <verb'ing>",
          "<Is> + <subject> + <verb'ing>?"))
    ),
    "Present Perfect": (
        (("I", "We", "You", "They"),
         ("<have> + <3rd form of the verb>",
          "<have not> + <3rd form of the verb>",
          "<Have> + <subject> + <3rd form of the verb>?")),
        (("He", "She", "It"),
         ("<has> + <3rd form of the verb>",
          "<has not> + <3rd form of the verb>",
          "<Has> + <subject> + <3rd form of the verb>?"))
    ),
    "Present Perfect Continuous": (
        (("I", "We", "You", "They"),
         ("<have been> + <verb'ing>",
          "<have not been> + <verb'ing>",
          "<Have> + <subject> + <been> + <verb'ing>?")),
        (("He", "She", "It"),
         ("<has been> + <verb'ing>",
          "<has not been> + <verb'ing>",
          "<Has> + <subject> + <been> + <verb'ing>?"))
    ),
    "Future Simple": (
        (("I", "We", "You", "They"),
         ("<will/shall> + <1st form of the verb>",
          "<will/shall not> + <1st form of the verb>",
          "<Will/Shall> + <subject> + <1st form of the verb>?")),
        (("He", "She", "It"),
         ("<will/shall> + <1st form of the verb>",
          "<will/shall not> + <1st form of the verb>",
          "<Will/Shall> + <subject> + <1st form of the verb>?"))
    ),
    "Future Continuous": (
        (("I", "We", "You", "They"),
         ("<will/shall> + <verb'ing>",
          "<will/shall not> + <verb'ing>",
          "<Will/Shall> + <subject> + <verb'ing>?")),
        (("He", "She", "It"),
         ("<will> <verb+'ing>",
          "<will/shall not> + <verb'ing>",
          "<Will/Shall> + <subject> + <verb'ing>?"))
    ),
    "Future Perfect": (
        (("I", "We", "You", "They"),
         ("<will/shall have> + <3rd form of the verb>",
          "<will/shall not have> + <3rd form of the verb>",
          "<Will/Shall> + <subject> + <have> + <3rd form of the verb>?")),
        (("He", "She", "It"),
         ("<will/shall have> + <3rd form of the verb>",
          "<will/shall not have> + <3rd form of the verb>",
          "<Will/Shall> + <subject> + <have> + <3rd form of the verb>?"))
    ),
    "Future Perfect Continuous": (
        (("I", "We", "You", "They"),
         ("<will/shall have been> + <verb'ing>",
          "<will/shall not have been> + <verb'ing>",
          "<Will/Shall> + <subject> + <have been> + <verb'ing>?")),
        (("He", "She", "It"),
         ("<will/shall have been> + <verb'ing>",
          "<will/shall not have been> + <verb'ing>",
          "<Will/Shall> + <subject> + <have been> + <verb'ing>?"))
    )
}


def create_tables():
    """The create_tables function creates the tables in the database.

    :return: None
    """
    for row in SRC:

        time = Times.objects.create(name=row[0],
                                    rule=row[1],
                                    examples=row[2])
        for ex in VERBS[row[0]]:
            try:
                verb = Verbs.objects.create(name=row[0],
                                            pron=ex[0],
                                            verbs=ex[1])

            except Exception as exc:
                logger.info(exc)
                verb = Verbs.objects.create(name=row[0],
                                            pron=[ex[0]],
                                            verbs=ex[1])

            finally:
                time.verbs.add(verb)


class Command(BaseCommand):
    """This class contains command for create files types and
    files extensions in FileExtension and FileTypes tables from storageapp.

    The class has the following attributes:
    
    - help (str): A message that is displayed when you this command
    """

    help = "use 'python manage.py create_times_tables' to create tables"

    def handle(self, *args, **options):
        """The handle function is the entry point for a Django management
        command.

        :return: A string that is printed in the console
        """
        create_tables()
