def generate_flat_adder(n_bits):
    filename = f"flat_{n_bits}bit_adder.v"
    with open(filename, "w") as f:
        f.write(f"module flat_{n_bits}bit_adder (\n")
        f.write(f"    input  [{n_bits-1}:0] A,\n")
        f.write(f"    input  [{n_bits-1}:0] B,\n")
        f.write("    input        Cin,\n")
        f.write(f"    output wire [{n_bits-1}:0] Sum,\n")
        f.write("    output wire  Cout\n")
        f.write(");\n\n")
        
        f.write("    always @(*) begin\n")
        f.write(f"        case ({{A, B, Cin}}) // Format: {{A[{n_bits-1}:0], B[{n_bits-1}:0], Cin}}\n")
        
        for a in range(2**n_bits):
            for b in range(2**n_bits):
                for cin in range(2):
                    result = a + b + cin
                    Cout = (result >> n_bits) & 1  # Extract carry-out directly
                    Sum = result & ((1 << n_bits) - 1)  # Extract sum directly
                    
                    # Using Verilog's concatenation operator `{Cout, Sum}`
                    f.write(f"            {n_bits * 2 + 1}'b{a:0{n_bits}b}{b:0{n_bits}b}{cin}: ")
                    f.write(f" {{Cout, Sum}} = {{{Cout}, {n_bits}'b{Sum:0{n_bits}b}}}; ")
                    f.write(f"// A={a:0{n_bits}b}, B={b:0{n_bits}b}, Cin={cin}\n")

        f.write(f"            default: {{Cout, Sum}} = {n_bits + 1}'b0;\n")
        f.write("        endcase\n    end\n")
        f.write("endmodule\n")

    print(f"Generated {filename}")

# Generate a 4-bit adder without a result register
generate_flat_adder(4)
