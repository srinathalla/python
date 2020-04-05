class FileSystem:

    def __init__(self):
        self.fs = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.fs:
            return False
        parent = path[:path.rindex("/")]
        if len(parent) > 0 and parent not in self.fs:
            return False

        self.fs[path] = value
        return True

    def get(self, path: str) -> int:

        return self.fs.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
obj = FileSystem()
print(obj.createPath("/a", 1))

print(obj.get("/a"))
