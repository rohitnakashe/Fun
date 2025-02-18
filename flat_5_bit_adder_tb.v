// Code your testbench here
// or browse Examples
module tb_five_fa;

  // Testbench signals
  reg [4:0] A, B;
  reg Cin;
  wire [5:0] sum;
  wire cout;

  // Instantiate the 5-bit full adder
  five_fa dut (
    .A(A),
    .B(B),
    .Cin(Cin),
    .sum(sum),
    .cout(cout)
  );

  // Test vectors
  initial begin
    // Initialize signals
    A = 5'b00000; B = 5'b00000; Cin = 0;
    
    // Display header
    $display("A       B       Cin  |  sum   cout");
    $display("--------------------------------------");

    // Apply 10 test cases
    #10 A = 5'b00001; B = 5'b00001; Cin = 0;
    #10 A = 5'b11111; B = 5'b11111; Cin = 1;
    #10 A = 5'b01010; B = 5'b10101; Cin = 1;
    #10 A = 5'b10000; B = 5'b10000; Cin = 0;
    #10 A = 5'b11100; B = 5'b00011; Cin = 1;
    #10 A = 5'b00111; B = 5'b11001; Cin = 0;
    #10 A = 5'b01101; B = 5'b10100; Cin = 1;
    #10 A = 5'b01011; B = 5'b11110; Cin = 0;
    #10 A = 5'b10010; B = 5'b01101; Cin = 1;
    #10 A = 5'b11100; B = 5'b11100; Cin = 0;
    
    // Finish simulation
    #10 $finish;
  end

  // Monitor the output
  always @ (A, B, Cin, sum, cout) begin
    $display("%b  %b    %b   |  %b  %b", A, B, Cin, sum, cout);
  end

endmodule
