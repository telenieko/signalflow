from signalflow import Plumber, Pipe


class FirstGen(Pipe):
    def once(self):
        self.emit_number(1)
        self.emit_number(2)

    def receive_number(self, sender, i):
        if sender > self:
            self.emit_message(i)

    def emit_number(self, i):
        pass

    def emit_message(self, i):
        pass


class SecondGen(Pipe):
    def once(self):
        self.emit_number(3)
        self.emit_number(4)

    def receive_number(self, sender, i):
        if sender < self:
            self.emit_message(i)

    def emit_number(self, i):
        pass

    def emit_message(self, i):
        pass


class Logger(Pipe):
    def __init__(self):
        self.received = []

    def receive_message(self, sender, i):
        self.received.append(i)


def test_comparison():
    flow = Plumber()
    flow.add_pipe(FirstGen())
    flow.add_pipe(SecondGen())
    logger = Logger()
    flow.add_pipe(logger)
    flow.go()

    assert [1, 2, 3, 4] == logger.received
