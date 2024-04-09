#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """ the console of my program"""

    prompt = "(hbnh)"

    def do_quit(self, line):
        """ exit command"""
        return True

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """exit command"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
