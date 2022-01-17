import dis

class Logger:
  def __init__(self):
    self.messages = {}

  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    if timestamp - self.messages.get(message, -10) < 10:
      return False

    self.messages[message] = timestamp

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