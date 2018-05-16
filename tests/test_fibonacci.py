from signalflow import Pipe, Plumber


class EmitZeroThenOne(Pipe):
    def once(self):
        # once is called when the loop has nothing to do and is looking
        # for new signals.
        self.emit_number(0)
        self.emit_number(1)

    def emit_number(self, i: int):
        # emit_* are always stubs.
        pass


class FibonacciAcummulator(Pipe):
    last_number = -1

    def receive_number(self, sender, i: int):
        if i > 34:
            return
        if self.last_number >= 0:
            self.emit_number(i + self.last_number)
        self.last_number = i

    def emit_number(self, i: int):
        pass


class NumberPrinter(Pipe):
    all_numbers = tuple()

    def receive_number(self, sender, i: int):
        self.all_numbers += (i, )


def test_fibonacci_plumber():
    flow = Plumber()
    flow.add_pipe(EmitZeroThenOne())
    flow.add_pipe(FibonacciAcummulator())
    printer = NumberPrinter()
    flow.add_pipe(printer)

    assert "number" in flow.joints
    assert len(flow.joints["number"]) == 2

    flow.go()  # Prints Fibonacci Sequence
    assert (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55) == printer.all_numbers