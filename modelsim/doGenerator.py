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
        t = k
        for i in range(len(kw)):
            s+="force {"+kw[i]+"} "+ str(t % 2) + "\n"
            t //= 2
        s+="run 10ns\n\n"
        k += 1
        index += 1
    return s

if __name__ == '__main__':
    print(generator("lect9.v", "ripple-carryadder", 1, "x", "y", "s"))
