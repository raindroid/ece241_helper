def generator(filename, modname, index=1, *kw):
    print("""
# set the working dir, where all compiled verilog goes
vlib work

# compile all verilog modules in mux.v to working dir
# could also have multiple verilog files
vlog {0}

#load simulation using mux as the top level simulation module
vsim {1}\n\n""".format(filename, modname),

          r"""#log all signals and add some signals to waveform window
          log {/*}
          add wave {/*}
          """)

    k = 0
    s = ""
    while k < 2**len(kw):
        s+="#Test Case " + str(index) + "\n"
        for i in range(2):
            t = k
            for i in range(7):
                s += "force {SW[" + str(i) + "]} 0\n"
            for i in range(len(kw)):
                s += "force {"+kw[i]+"} "+ str(t % 2) + "\n"
                t //= 2
        s+="run 10ns\n\n"
        k += 1
        index += 1
    return s

def force_case_generator(*kw):
    n = len(kw)
    while True:
        bit = [0 for i in range(n)]
        inp = str(input())
        for i in range(n):
            bit[i] = inp[i]

        for i in range(n):
            print("force {" + kw[i] + "} " + str(bit[i]))
        print("run 10ps")

if __name__ == '__main__':
    # print(generator("top.v", "top", 1, "SW[7]", "SW[8]", "SW[9]"))
    force_case_generator("SW[0]","SW[1]","SW[2]","SW[3]","SW[4]","SW[5]","SW[6]","SW[7]","SW[8]")