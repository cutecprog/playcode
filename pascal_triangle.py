def main():
        print pascal_triangle(4,3)

def pascal_triangle(row, col):
        """Computes value of Pascal's triangle at row and column.

        """
        gray_theory = lambda last, row, col: last * ((row + 1) - col) / col
        p = 1
        for i in range(1, col):
                p = gray_theory(p, row, i)
        return p

if __name__=="__main__":
        main()
