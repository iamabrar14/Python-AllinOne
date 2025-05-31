def countDown(number):
    if number == 0:
        print("Done")
    else:
        print(f'count{number}')
        countDown(number - 1)


countDown(3)
