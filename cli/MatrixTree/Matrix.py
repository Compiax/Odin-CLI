###########################################################
#   File Details
###########################################################
#   The matrix uses list to recursively generate the points
#   needed for the matrix. This will be used to input a n-dimensional
#   matrix.
#   This is used ONLY by the SetVarHandler class.
#   Created by Kyle Erwin - 19/07/2017

class Matrix():
    points = []
    root = ""

    ###########################################################
    #   Constructors
    ###########################################################
    def build(self, dimensions):
        self.reccuriveBuild(self.root, dimensions, 0)

    def reccuriveBuild(self, node, dimensions, index):
        if index < len(dimensions):
            count = 0;

            while count < int(dimensions[index]):
                child = node + "[" + str(count) + "]"
                self.reccuriveBuild(child, dimensions, index + 1)
                count += 1
        else:
            self.points.append(node)

    ###########################################################
    #   Transferal Methods
    ###########################################################
    def getPoints(self):
        return self.points

    ###########################################################
    #   Print Methods
    ###########################################################
    def printPoints(self):
        print(self.points)
        for point in self.points:
            print(point)

    ###########################################################
    #   Delete
    ###########################################################
    def detlete(self):
        del self.points[:]