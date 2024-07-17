class Spam:
    def __getitem__(self, index: int) -> str:
        print("->", index)
        if index == 0:
            return "foo"
        elif index == 1:
            return "bar"
        else:
            raise IndexError()
