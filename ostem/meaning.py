class Meaning:
    def __init__(self, value, note):
        self.value = value
        self.note = note

    def __str__(self):
        return self.value + (f' ({self.note})' if self.note else "")
