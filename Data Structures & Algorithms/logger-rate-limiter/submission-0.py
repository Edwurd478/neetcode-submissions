from collections import deque
class Logger:

    def __init__(self):
        self.active_messages = deque() #(timestamp, message)
        self.existing_messages = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.active_messages and self.active_messages[0][0] <= timestamp - 10:
            time, mes = self.active_messages.popleft()
            self.existing_messages.remove(mes)
        
        if message in self.existing_messages:
            return False
        
        self.active_messages.append((timestamp, message))
        self.existing_messages.add(message)
        return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
