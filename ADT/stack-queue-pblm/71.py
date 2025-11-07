class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        stack = deque()
        for token in tokens:
            if token == "" or token == ".":
                continue
            if token != "..":
                stack.append(token)
            elif stack:
                stack.pop()
        result = ""
        while stack:
            result = "/" + stack.pop() + result
        if len(result) == 0:
            result = "/"
        return result
