def main():
        gray_theory = lambda last, row, col: last * ((row + 1) - col) / col
        for i in range(0, 100):
                p = 1
                for j in range(1, (i+2)/2):
                        p = gray_theory(p, i, j)
                print p

if __name__=="__main__":
        main()
