module top_module ( input clk, input d, output q );

    wire a, b;
    my_dff inst1 (clk, d, a );
    my_dff inst2 (clk, a, b );
    my_dff inst3 (clk, b, q );
    
endmodule
