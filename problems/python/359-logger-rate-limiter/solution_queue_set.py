from sys import argv
from typing import List
import dis
from collections import deque

class Logger:
  def __init__(self):
    self.messages = set()
    self.queue = deque()

  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    while self.queue and timestamp - self.queue[-1][0] > 9:
      m = self.queue.pop()[1]
      self.messages.remove(m)

    if message in self.messages:
      return False

    self.queue.appendleft([timestamp, message])
    self.messages.add(message)

    return True

f = Logger()

inputs = [ 
  (1, "foo"), 
  (2, "bar"), 
  (3, "foo"), 
  (8, "bar"), 
  (10, "foo"),
  (11, "foo")
]

for input in inputs:
  print(f'Inputs: [{input}]')
  print(f'Result: [{f.shouldPrintMessage(*input)}]')