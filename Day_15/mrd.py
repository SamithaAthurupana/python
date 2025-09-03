# Method resolution order - MRD

class Top:
    def m_top(self):
        print("Top class")

class Middle(Top):
    def m_middle(self):
        print("middle class")

class Bottom(Middle, Top):
    def m_bottom(self):
        print("bottom class")

bottom = Bottom()
bottom.m_bottom()
bottom.m_middle()
bottom.m_top()