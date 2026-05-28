`timescale 1ns / 1ps
// =============================================================================
// Module      : fpga_dense_accelerator
// Description : Single-neuron dense layer accelerator. Computes the dot
//               product of a 16-element input vector with trained weights,
//               adds a bias, and registers the output on the rising clock edge.
// Revision    : 0.02  27-May-2026
// =============================================================================

module fpga_dense_accelerator (
    input  wire                clk,
    input  wire signed [15:0]  x1,  x2,  x3,  x4,
    input  wire signed [15:0]  x5,  x6,  x7,  x8,
    input  wire signed [15:0]  x9,  x10, x11, x12,
    input  wire signed [15:0]  x13, x14, x15, x16,
    output reg  signed [31:0]  y
);

    // Trained weights (quantised integers - replace with training script output)
    parameter signed [15:0] w1  = -66,  w2  = -94,  w3  = -117, w4  =  82;
    parameter signed [15:0] w5  =  43,  w6  =  114, w7  = -115, w8  =  136;
    parameter signed [15:0] w9  =  32,  w10 = -92,  w11 =  50,  w12 = -181;
    parameter signed [15:0] w13 =  10,  w14 = -170, w15 =  122, w16 = -177;
    parameter signed [15:0] b   = -14;

    always @(posedge clk) begin
        y <= ( w1*x1  + w2*x2  + w3*x3   + w4*x4   )
           + ( w5*x5  + w6*x6  + w7*x7   + w8*x8   )
           + ( w9*x9  + w10*x10 + w11*x11 + w12*x12 )
           + ( w13*x13 + w14*x14 + w15*x15 + w16*x16 )
           + b;
    end

endmodule