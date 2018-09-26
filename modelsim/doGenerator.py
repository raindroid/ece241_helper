def generator(index=1, *kw):
    k = 0
    s = ""
    while k < 2**len(kw):
        s+="#Test Case " + str(index) + "\n"
        t = k
        for i in range(len(kw)):
            s+="force {"+kw[i]+"} "+ str(t % 2) + "\n"
            t //= 2
        s+="run 10ns\n\n"
        k += 1
        index += 1
    return s

if __name__ == '__main__':
    print(generator(13, "pin12", "pin13"))