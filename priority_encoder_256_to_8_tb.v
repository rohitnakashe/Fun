module priority_encoder_256_to_8_tb;

    reg [255:0] In;
    wire [7:0] Out;
    wire valid;

    priority_encoder_256_to_8 dut (
        .in(In),
        .out(Out),
        .valid(valid)
    );

    initial begin
        $display("In (Hex Input)                                                      | Out | Valid");
        $display("------------------------------------------------------------------------------------------------");

        // No input set (all 0s)
        In = 256'h0000000000000000000000000000000000000000000000000000000000000000;
        #10; $display("%0h | %3d | %b", In, Out, valid);

        // Single-bit set at LSB (bit 0)
        In = 256'h0000000000000000000000000000000000000000000000000000000000000001;
        #10; $display("%0h | %3d | %b", In, Out, valid);

        // Single-bit set at MSB (bit 255)
        In = 256'h8000000000000000000000000000000000000000000000000000000000000000;
        #10; $display("%0h | %3d | %b", In, Out, valid);

        // Single-bit set in upper half (bit 200)
        In = 256'h0000000000000000000000000000000000000000000000008000000000000000;
        #10; $display("%0h | %3d | %b", In, Out, valid);

        // All bits set (full scale test)
        In = 256'hFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF;
        #10; $display("%0h | %3d | %b", In, Out, valid);

        // Multiple bits set in different regions
        In = 256'h00000000FFFFFFFF00000000FFFFFFFF00000000FFFFFFFF00000000FFFFFFFF;
        #10; $display("%0h | %3d | %b", In, Out, valid);

        // Alternating bits pattern (checkerboard)
        In = 256'hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA;
        #10; $display("%0h | %3d | %b", In, Out, valid);

        // Another alternating pattern
        In = 256'h5555555555555555555555555555555555555555555555555555555555555555;
        #10; $display("%0h | %3d | %b", In, Out, valid);

        // Randomized bit pattern test
        In = 256'hF0F00F0FFFFFFF1234F0F00F0FFFFFFF1234F0F00F0FFFFFFF1234F0F00F0FFFF;
      	#10; $display("%0h | %3d | %b", In, Out, valid);

        // Single-bit set at different locations
        In = 256'h0000800000000000000080000000000000008000000000000000800000000000;
        #10; $display("%0h | %3d | %b", In, Out, valid);

        // Random bits set throughout the input
        In = 256'h102030405060708090A0B0C0D0E0F0F0102030405060708090A0B0C0D0E0F0F0;
        #10; $display("%0h | %3d | %b", In, Out, valid);
        
        $finish;
    end
endmodule
