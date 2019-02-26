from .command import Command as BaseCommand

BASE_COMMAND = "housekeeper"


#Inherit from BaseCommand
class HousekeeperCommand(BaseCommand):

    def __init__(self, case_id):

        super(HousekeeperCommand, self).__init__(BASE_COMMAND)

        self.add_subcommand('get')
        self.add_option('V', long=False)
        self.add_argument(case_id)
