class mat_in_park():
    def __init__(self,park,mat_size):
        self.park = park
        self.park_row = len(park)
        self.park_col = len(park[0])
        self.mat_size = mat_size

    def find_mat(self,row,col):
        for y in range(self.mat_size):
            for x in range(self.mat_size):
                if self.park[row+y][col+x] != '-1':
                    return False
        return True
                
    def __call__(self):
        for row in range(self.park_row - self.mat_size + 1):
            for col in range(self.park_col - self.mat_size + 1):
                if self.find_mat(row,col):
                    return True
        return False
                    
def solution(mats, park):
    mats.sort(reverse=True)
    for mat_size in mats:
        if mat_in_park(park,mat_size)():
            return mat_size
    return -1