from collections import deque

from signalflow import Pipe, Plumber


class EmitRange(Pipe):
    def once(self):
        for i in range(1, 11):
            self.emit_number(i)

    def emit_number(self, i: int):
        pass


class EmitRangeGenerator(Pipe):
    numbers = deque(range(1, 11))

    def once(self):
        if len(self.numbers) > 0:
            self.emit_number(self.numbers.popleft())
            return True
        return False

    def emit_number(self, i: int):
        pass


class Square(Pipe):
    def receive_number(self, sender, i: int):
        if sender == self:
            return
        self.emit_number(i*i)
        return True

    def emit_number(self, i: int):
        pass


class SquareOnlyEven(Pipe):
    def receive_number(self, sender, i: int):
        if sender == self:
            return
        if i % 2 == 0:
            self.emit_number(i*i)
            return True

    def emit_number(self, i: int):
        pass


class NumberLogger(Pipe):
    all_numbers = tuple()

    def receive_number(self, sender, i: int):
        self.all_numbers += (i, )


def test_sequence_break():
    flow = Plumber()
    flow.add_pipe(EmitRange())
    flow.add_pipe(Square())
    logger = NumberLogger()
    flow.add_pipe(logger)

    flow.go()
    assert (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) == logger.all_numbers

    flow = Plumber()
    flow.add_pipe(EmitRange())
    flow.add_pipe(SquareOnlyEven())
    logger = NumberLogger()
    flow.add_pipe(logger)

    flow.go()
    assert (1, 3, 5, 7, 9, 4, 16, 36, 64, 100) == logger.all_numbers


def test_generator_processing_order():
    """ this checks that queues are processed properly,
    EmitRangeGenerator differs from the EmitRange in that the former one
    emits one number at a time, thus emissions by receivers are processed
    before the next generator emission.
    """
    flow = Plumber()
    flow.add_pipe(EmitRangeGenerator())
    flow.add_pipe(SquareOnlyEven())
    logger = NumberLogger()
    flow.add_pipe(logger)

    flow.go()
    assert (1, 4, 3, 16, 5, 36, 7, 64, 9, 100) == logger.all_numbers
