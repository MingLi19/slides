from collections import deque


class Browser:
    def __init__(self):
        self._back = deque()
        self._forward = deque()
        self._current = None

    def visit(self, url: str):
        self._back.append(self._current)
        self._current = url
        self._forward.clear()

    def back(self) -> str:
        if not self._back:
            return self._current
        self._forward.append(self._current)
        self._current = self._back.pop()
        return self._current

    def forward(self) -> str:
        if not self._forward:
            return self._current
        self._back.append(self._current)
        self._current = self._forward.pop()
        return self._current


browser = Browser()
browser.visit("google.com")
browser.visit("yahoo.com")
browser.visit("bing.com")
print(browser.back())
print(browser.back())
print(browser.back())
print(browser.forward())
print(browser.forward())
print(browser.forward())
