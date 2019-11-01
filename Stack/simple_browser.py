# _*_ coding:utf-8 _*_
"""
    解答：我们使用两个栈，X 和 Y，我们把首次浏览的页面依次压入栈 X，当点击后退按钮时，再依次从栈 X 中出栈，
    并将出栈的数据依次放入栈 Y。当我们点击前进按钮时，我们依次从栈 Y 中取出数据，放入栈 X 中。
    当栈 X 中没有数据时，那就说明没有页面可以继续后退浏览了。当栈 Y 中没有数据，
    那就说明没有页面可以点击前进按钮浏览了。
"""

from Stack.linked_stack import LinkedStack


class Browser:
    def __init__(self):
        self.f_stack = LinkedStack()
        self.b_stack = LinkedStack()

    def can_forward(self):
        if self.b_stack.is_empty():
            return False
        return True

    def can_back(self):
        if self.f_stack.is_empty():
            return False
        return True

    def open(self, url):
        """第一次浏览页面"""
        print("Open new url: %s" %url, end="\n")
        self.f_stack.push(url)

    def back(self):
        if self.f_stack.is_empty():
            return
        url = self.f_stack.pop()
        self.b_stack.push(url)
        print("Back to: %s" %url, end="\n")

    def forward(self):
        if self.b_stack.is_empty():
            return
        url = self.b_stack.pop()
        self.f_stack.push(url)
        print("Forward to: %s" %url, end="\n")


if __name__ == "__main__":
    browser = Browser()
    browser.open('a')
    browser.open('b')
    browser.open('c')
    if browser.can_back():
        browser.back()

    if browser.can_forward():
        browser.forward()

    browser.back()
    browser.back()
    browser.back()