# Python signal based flow based programming

This library provides utilities that allow to build simple signal / generator
based data flows which provide for clean code on complex data transformations.

This was primarily designed to be used in batch works though, in principle,
streaming data should work just fine.

And it was born because I needed something *really* simple that would allow me
to process data on a row-by-row basis and generate events/signals during that
processing.

## Usage example (see tests/)

```python
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
    def receive_number(self, sender, i: int):
        print(f"Received {i}")
        

flow = Plumber()
flow.add_pipe(EmitZeroThenOne())
flow.add_pipe(FibonacciAcummulator())
flow.add_pipe(NumberPrinter())

flow.go()  # Prints Fibonacci Sequence
```
