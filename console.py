#!/usr/bin/python3
"""documentation of the command line interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ the console of my program"""

    prompt = "(hbnh)"

    def do_quit(self, line):
        """ exit command"""
        return True

    def emptyline(self):
        print('\n')
        pass

    def do_EOF(self, line):
        """exit command"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
