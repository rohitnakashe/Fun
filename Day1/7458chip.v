module top_module ( 
    input p1a, p1b, p1c, p1d, p1e, p1f,
    output p1y,
    input p2a, p2b, p2c, p2d,
    output p2y );

	wire l,m,n,o;
    assign l = p2a && p2b;
    assign m = p2c && p2d;
	assign n = p1a && p1b && p1c;
    assign o = p1d && p1e && p1f;
	assign p1y = n || o;
	assign p2y = l || m;
    
endmodule
