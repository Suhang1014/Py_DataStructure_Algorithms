# _*_ coding:utf-8 _*_
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    def is_overlap(self, other):
        if self.x <= other.x + other.w and other.x <= self.x + self.w and \
                self.y <= other.y + other.h and other.y <= self.y + self.h:
            return True
        return False

    def overlap_rectangle(self, other):
        if self.is_overlap(other):
            return Rectangle(max(self.x, other.x), max(self.y, other.y), \
                             min(other.x+other.w, self.x+self.w) - max(other.x, self.x), \
                             min(other.y+other.h, self.y+self.h) - max(other.y, self.y))
        return None


if __name__ == '__main__':
    S = Rectangle(0.1, 0.1, 0.5, 0.5)
    R = Rectangle(0.2, 0.2, 0.6, 0.5)
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.add_patch(patches.Rectangle((S.x, S.y), S.w, S.h, facecolor='red'))
    ax.add_patch(patches.Rectangle((R.x, R.y), R.w, R.h, facecolor='blue'))
    if S.is_overlap(R) is True:
        overlap = S.overlap_rectangle(R)
        ax.add_patch(patches.Rectangle((overlap.x, overlap.y), overlap.w, overlap.h, facecolor='green'))
        plt.show()





