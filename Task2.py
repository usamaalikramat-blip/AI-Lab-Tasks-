class Room:
    def __init__(self):
        self.mode = None
    def control(self, temp, occupied):
        target = "off" if not occupied else "cooling" if temp >= 30 else heating if temp <18 else "normal"
        command = target != self.mode
        self.mode = target
        return target, command
r = Room()
for temp, occupied in [(30,True),(30,True),(18,True),(25,True),(25,False)]:
    target, command = r.control(temp, occupied)
    print(temp, occupied, target, "Send Command" if command else "no command")

