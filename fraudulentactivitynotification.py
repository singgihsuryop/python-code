# Tested Code
class Test :
    @staticmethod
    def main( args) :
        print(Test.solution("9 5", [2, 3, 4, 2, 3, 6, 8, 4, 5]))
        print(Test.solution("5 4", [1, 2, 3, 4, 4]))
    @staticmethod
    def  solution( input,  expenditure) :
        n = int(input.split(" ")[0])
        d = int(input.split(" ")[1])
        isEven = False
        if (d % 2 == 0) :
            isEven = True
        else :
            isEven = False
        median = 0
        countAlert = 0
        i = d
        while (i < n) :
            if (not isEven) :
                median = expenditure[(i - d) + ((int(d / 2)))]
            else :
                median = expenditure[(i - d) + (int((((int(d / 2)) - 1) + ((int(d / 2)))) / 2))]
            if (expenditure[i] >= median * 2) :
                countAlert += 1
            i += 1
        return countAlert
    

if __name__=="__main__":
    Test.main([])
