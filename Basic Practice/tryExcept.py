if __name__ == '__main__':
    tstcases = int(input())
    for i in range(tstcases):
        try:
            nums = list(map(int,input().split()))
            res = nums[0]//nums[1]
            print(res)
        except ZeroDivisionError as e:
            print(f'Error Code: integer division or modulo by zero')
        except ValueError as e:
            print(f'Error Code: {e}')
        except TypeError as e:
            print(f'Error Code:{e}')

