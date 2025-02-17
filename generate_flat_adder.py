def generate_flat_adder(n_bits):
    filename = f"flat_{n_bits}bit_adder.v"
    with open(filename, "w") as f:
        f.write(f"module flat_{n_bits}bit_adder (\n")
        f.write(f"    input  [{n_bits-1}:0] A,\n")
        f.write(f"    input  [{n_bits-1}:0] B,\n")
        f.write("    input        Cin,\n")
        f.write(f"    output wire [{n_bits-1}:0] Sum,\n")
        f.write("    output   wire    Cout\n");
        f.write(");\n    reg [ {}:0] result;\n".format(n_bits))
        f.write("    always @(*) begin\n")
        f.write(f"        case ({{A, B, Cin}}) // Format: {{A[{n_bits-1}:0], B[{n_bits-1}:0], Cin}}\n")
        
        for a in range(2**n_bits):
            for b in range(2**n_bits):
                for cin in range(2):
                    result = a + b + cin
                    f.write(f"            {n_bits + n_bits + 1}'b" + \
                            f"{a:0{n_bits}b}{b:0{n_bits}b}{cin}:" )
                    f.write(f" result = {n_bits + 1}'b{result:0{n_bits + 1}b}; // A={a:0{n_bits}b}, B={b:0{n_bits}b}, Cin={cin}\n")
        
        f.write("            default: result = {0}'b0;\n".format(n_bits + 1))
        f.write("        endcase\n    end\n")
        f.write("    assign Sum  = result[{}:0];\n".format(n_bits-1))
        f.write("    assign Cout = result[{}];\n".format(n_bits))
        f.write("endmodule\n")
    print(f"Generated {filename}")

# Generate a 4-bit adder as an example
generate_flat_adder(5)
