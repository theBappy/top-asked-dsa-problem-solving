class Solution:
    def __init__(self):
        self.parent = []
        self.rank = []

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def Union(self, x: int, y: int) -> None:
        p_x = self.find(x)
        p_y = self.find(y)

        if p_x != p_y:
            if self.rank[p_x] > self.rank[p_y]:
                self.parent[p_y] = p_x
            elif self.rank[p_x] < self.rank[p_y]:
                self.parent[p_x] = p_y
            else:
                self.parent[p_x] = p_y
                self.rank[p_y] += 1

    def equationsPossible(self, equations: List[str]) -> bool:
        self.parent = list(range(26))
        self.rank = [1] * 26

        for s in equations:
            if s[1] == "=":
                self.Union(ord(s[0]) - ord("a"), ord(s[3]) - ord("a"))

        for s in equations:
            if s[1] == "!":
                if self.find(ord(s[0]) - ord("a")) == self.find(ord(s[3]) - ord("a")):
                    return False
        return True
