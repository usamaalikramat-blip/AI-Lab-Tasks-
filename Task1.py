class scholarship:
    def __init__(self, score, documents, attendance, interview):
        self.score = score
        self.documents = documents
        self.attendance = attendance
        self.interview = interview
    def check(self):
        if self.score >= 70and self.documents and self.attendance >= 75 and self.interview:
            return "eligible"
        return "not eligible"
tests = [
    (80,True,80,True),
    (80,True,60,True),
    (80,True,80,False),
    (70,True,80,True)
]
ecpected = ["eligible","not eligible","not eligible","eligible"]
for i, data in enumerate (tests):
    s = scholarship(*data)
    actual = s.check()
print("\nTest case:",i + 1)
print("input:",data)
print("Expected:",ecpected[i])
print("actual:",actual)
print("reason:",actual)


