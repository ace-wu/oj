class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.comb_length = combinationLength
        self.comb_iter = iter(self.iter_next(0))
        self.next_comb = []

    def peek(self):
        if not self.next_comb:
            next_ = self.next()
            if next_ is not None:
                self.next_comb.append(next_)
            return next_
        return self.next_comb[-1]

    def next(self) -> str:
        if self.next_comb:
            return self.next_comb.pop()
        try:
            return next(self.comb_iter)
        except StopIteration:
            pass
        return None

    def iter_next(self, cursor, selected=None):
        if selected is None:
            selected = []
        elif len(selected) == self.comb_length:
            yield ''.join(selected)
            return
        selected.append(self.characters[cursor])
        yield from self.iter_next(cursor + 1, selected)
        selected.pop()
        if len(selected) + len(self.characters) - cursor > self.comb_length:
            yield from self.iter_next(cursor + 1, selected)


    def hasNext(self) -> bool:
        return self.peek() is not None


## TC: O(k) for a single query of next()/hasNext()/peek()
## SC: O(k)
