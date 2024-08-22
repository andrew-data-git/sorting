import random
import sorting

# Press the green button in the gutter to run the script.
if __name__ == '__main__':



    # generate numbers
    # n = int(input("Enter the number of elements:"))
    n = 10
    nums = [random.randint(0, i) for i in range(n)]
    print("Numbers are :")
    print(nums)

    # algorithm selection
    # select = int(input("Choose algorithm:  1.Bubble \n 2.Insertion \n 3.Selection \n"))
    select = 1    # if select not in [1,2,3]

    # run
    # print(sorting.sorting(nums, select))
    gen = sorting.sorting(nums, select)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))