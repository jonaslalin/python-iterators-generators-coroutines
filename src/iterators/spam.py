class Spam:
    def __getitem__(self, index: int) -> str:
        print("->", index)
        if index == 0:
            return "spam"
        elif index == 1:
            return "can"
        else:
            raise IndexError()
