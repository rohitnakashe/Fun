def generate_fa_module():
    # Create the 'fa' module
    fa_module = """
module fa (
  input A, B, Cin,
  output sum, cout
);
  wire s1, c1, c2;

  ha mod1 (.A(A), .B(B), .sum(s1), .carry(c1));
  ha mod2 (.A(s1), .B(Cin), .sum(sum), .carry(c2));

  assign cout = c1 | c2;

endmodule
"""
    return fa_module


def generate_ha_module():
    # Create the 'ha' module
    ha_module = """
module ha (
  input A, B,
  output sum, carry
);
  assign sum = A ^ B;
  assign carry = A & B;
endmodule
"""
    return ha_module


def generate_bit_adder_module(bit_size):
    # Create the module for a specific bit_size, with dynamic module name
    bit_adder_module = f"""
module {bit_size}_bit_adder(
  input bit [{bit_size-1}:0] A, B,
  input bit Cin,
  output bit [{bit_size}:0] sum,
  output cout);

  wire {', '.join([f'c{i}' for i in range(1, bit_size)])};

  """

    # Instantiate 'bit_size' number of full adders
    for i in range(bit_size):
        bit_adder_module += f"  fa mod{i+1} (.A(A[{i}]), .B(B[{i}]), .Cin(c{i} if i > 0 else Cin), .sum(sum[{i}]), .cout(c{i+1}));\n"

    # Add the last carry out for full adder
    bit_adder_module += f"  fa mod{bit_size} (.A(A[{bit_size-1}]), .B(B[{bit_size-1}]), .Cin(c{bit_size-1}), .sum(sum[{bit_size-1}]), .cout(cout));\n"

    bit_adder_module += "endmodule\n"

    return bit_adder_module


def save_verilog_file(file_name, code):
    # Open the file in write mode and save the Verilog code
    with open(file_name, "w") as file:
        file.write(code)
    print(f"Verilog file saved as {file_name}")


# Get the Verilog code for the different modules
bit_size = 6
fa_code = generate_fa_module()
ha_code = generate_ha_module()
bit_adder_code = generate_bit_adder_module(bit_size)

# Save each module in its own file
save_verilog_file("fa.v", fa_code)
save_verilog_file("ha.v", ha_code)
save_verilog_file(f"{bit_size}_bit_adder.v", bit_adder_code)
