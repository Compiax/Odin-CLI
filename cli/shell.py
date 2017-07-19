from cmd import Cmd

class OdinShell(Cmd):
    def do_var(self, args):
        """Creates a variable."""
        print ("'var' called with arguments {}".format(repr(args)))

    def do_set(self, args):
        """Sets a variable."""
        print ("'set' called with arguments {}".format(repr(args)))

    def do_do(self, args):
        """Performs an operation."""
        print ("'do' called with arguments {}".format(repr(args)))

    def do_execute(self, args):
        """Executes the session."""
        print ("'execute' called with arguments {}".format(repr(args)))

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting the Odin CLI Shell..")
        raise SystemExit