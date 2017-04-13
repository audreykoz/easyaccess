class Undocumented(object):
    def do_drop(self, line):
        self.default('drop ' + line)

    def do_DROP(self, line):
        self.default('DROP ' + line)

    def do_create(self, line):
        self.default('create ' + line)

    def do_CREATE(self, line):
        self.default('CREATE ' + line)

    def do_alter(self, line):
        self.default('alter ' + line)

    def do_ALTER(self, line):
        self.default('ALTER ' + line)
