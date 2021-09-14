class FileHandler:
    @classmethod
    def load_and_clean_commands(cls, file_path):
        with open(file_path, 'r') as file:
            commands = file.readlines()
        commands = [cls._clean_command(x) for x in commands] # Clean command
        commands = [x for x in commands if x != ''] # Remove empty commands
        return commands

    @staticmethod
    def _clean_command(command):
        comment_index = command.find('//')
        command_no_comments = command if comment_index == -1 else command[:comment_index]
        return command_no_comments\
            .replace('\n', '')\
            .replace('\s', '')\
            .replace('\t', '')\
            .replace(' ', '')