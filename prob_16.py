from timeit import default_timer as timer


start = timer()


if __name__ == '__main__':
    a = 2**1000
    str_a = str(a)
    s = 0
    for i in str_a:
        s = s + int(i)
    print(s)

end = timer()

time_taken = (end-start)*1000

print("Total time taken to run this program: %d ms"%(time_taken))