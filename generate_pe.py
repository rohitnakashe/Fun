import os

def generate_priority_encoder(num_inputs):
    # Calculate the number of output bits for the initial encoder (log2(num_inputs) rounded up)
    n = (num_inputs - 1).bit_length()  # Log2(num_inputs) rounded up
    
    if n % 2 != 0:
        raise ValueError("n must be even")

    def write_file(filename, content):
        with open(filename, "w") as f:
            f.write(content)
    
    def generate_pe_module(num_inputs, n):
        if num_inputs == 4:
            content = """module priority_encoder_4_to_2(
  input  [3:0] in,
  output [1:0] out,
  output valid
);
    assign out[1] = in[3] | in[2];
    assign out[0] = in[3] | (~in[2] & in[1]);
    assign valid = |in;
endmodule
"""
            write_file("priority_encoder_4_to_2.v", content)
            return
        
        # Divide the encoder into smaller ones
        lower_pe_size = num_inputs // 4
        lower_n = (lower_pe_size - 1).bit_length()  # Output size for lower encoder
        
        # Generate module names
        lower_pe_name = f"priority_encoder_{lower_pe_size}_to_{lower_n}"
        current_pe_name = f"priority_encoder_{num_inputs}_to_{n}"
        
        content = f"""module {current_pe_name} (
  input  [{num_inputs - 1}:0] in,
  output reg [{n - 1}:0] out,
  output reg valid
);

  wire [{lower_n - 1}:0] out0, out1, out2, out3;
  wire valid0, valid1, valid2, valid3;
  wire [{lower_n - 1}:0] out_upper;

  {lower_pe_name} pe0 (.in(in[{lower_pe_size - 1}:0]), .out(out0), .valid(valid0));
  {lower_pe_name} pe1 (.in(in[{2 * lower_pe_size - 1}:{lower_pe_size}]), .out(out1), .valid(valid1));
  {lower_pe_name} pe2 (.in(in[{3 * lower_pe_size - 1}:{2 * lower_pe_size}]), .out(out2), .valid(valid2));
  {lower_pe_name} pe3 (.in(in[{4 * lower_pe_size - 1}:{3 * lower_pe_size}]), .out(out3), .valid(valid3));

  {lower_pe_name} pe_upper (
    .in({{valid3, valid2, valid1, valid0}}),
    .out(out_upper),
    .valid(valid)
  );

  always @(*) begin
    case (out_upper)
      2'b00: out = {{out_upper, out0}};
      2'b01: out = {{out_upper, out1}};
      2'b10: out = {{out_upper, out2}};
      2'b11: out = {{out_upper, out3}};
      default: out = {n}'b0;
    endcase
  end
endmodule
"""
        
        write_file(f"{current_pe_name}.v", content)
        
        # Recursively generate for smaller encoders, updating 'n' each time
        if lower_pe_size >= 4:
            generate_pe_module(lower_pe_size, n - 2)
    
    # Start the generation process with the initial values
    generate_pe_module(num_inputs, n)
    print("Generated Verilog files.")

# Example usage
generate_priority_encoder(1024)
