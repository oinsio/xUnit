class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        self.log = None
        TestCase.__init__(self, name)

    def test_method(self):
        self.wasRun = 1
        self.log = self.log + "test_method "

    def set_up(self):
        self.wasRun = None
        self.log = "set_up "


class TestCaseTest(TestCase):
    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert "set_up test_method " == test.log


TestCaseTest("test_template_method").run()
