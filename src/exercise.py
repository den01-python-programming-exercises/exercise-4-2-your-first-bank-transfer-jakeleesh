from src.account import Account


def main():
    #write your code below this line
    matthew = Account("Matthew's account", 1000)
    mine = Account("My account", 0)
    matthew.withdraw(100)
    mine.deposit(100)
    print(matthew)
    print(mine)

if __name__ == '__main__':
    main()
