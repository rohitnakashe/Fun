import math

def generate_priority_encoder(num_inputs):
    assert (num_inputs & (num_inputs - 1)) == 0, "num_inputs must be a power of 2"
    
    n = int(math.log2(num_inputs))  # Calculate 'n' from num_inputs
    filename = f"priority_encoder_{num_inputs}_to_{n}.v"
    
    with open(filename, "w") as f:
        f.write(f"module priority_encoder_{num_inputs}_to_{n} (\n")
        f.write(f"    input  [{num_inputs - 1}:0] in,\n")
        f.write(f"    output reg [{n-1}:0] out,\n")
        f.write(f"    output reg valid\n")
        f.write(");\n\n")
        
        f.write("    always @(*) begin\n")
        f.write("        valid = |in;\n")
        f.write("        casex (in)\n")
        
        for i in range(num_inputs - 1, -1, -1):
            f.write(f"            {num_inputs}'b{'0' * (num_inputs - 1 - i)}" +
                    f"{'1'}{'x' * i}: out = {n}'d{i};\n")
        
        f.write(f"            default: out = {n}'d0;\n")
        f.write("        endcase\n")
        f.write("    end\n")
        f.write("endmodule\n")
    
    print(f"Generated {filename}")

# Example usage for a 64:6 priority encoder
generate_priority_encoder(64)
