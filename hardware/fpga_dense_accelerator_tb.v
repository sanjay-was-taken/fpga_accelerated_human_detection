`timescale 1ns / 1ps
// =============================================================================
// Testbench   : fpga_dense_accelerator_tb
// Description : Drives a single 16-element feature vector, waits two clock
//               cycles for output to register, then displays the prediction
//               and FPGA vs CPU performance comparison.
// Clock       : 10 ns (100 MHz)
// =============================================================================

module fpga_dense_accelerator_tb;

    reg                clk;
    reg  signed [15:0] x1,  x2,  x3,  x4;
    reg  signed [15:0] x5,  x6,  x7,  x8;
    reg  signed [15:0] x9,  x10, x11, x12;
    reg  signed [15:0] x13, x14, x15, x16;
    wire signed [31:0] y;

    time  start_time, end_time;
    real  fpga_latency_ns, speedup;

    localparam real    CPU_LATENCY_NS = 1151.447;
    localparam integer THRESHOLD      = 0;

    fpga_dense_accelerator uut (
        .clk (clk),
        .x1  (x1),  .x2  (x2),  .x3  (x3),  .x4  (x4),
        .x5  (x5),  .x6  (x6),  .x7  (x7),  .x8  (x8),
        .x9  (x9),  .x10 (x10), .x11 (x11), .x12 (x12),
        .x13 (x13), .x14 (x14), .x15 (x15), .x16 (x16),
        .y   (y)
    );

    initial clk = 0;
    always #5 clk = ~clk;

    initial begin
        x1=169; x2=0;   x3=120; x4=10;
        x5=0;   x6=200; x7=5;   x8=0;
        x9=0;   x10=0;  x11=0;  x12=0;
        x13=0;  x14=0;  x15=180; x16=0;

        #2;
        start_time = $time;
        @(posedge clk);
        @(posedge clk);
        end_time = $time;

        fpga_latency_ns = end_time - start_time;
        speedup         = CPU_LATENCY_NS / fpga_latency_ns;

        $display("");
        $display("=================================================");
        $display("  INFERENCE RESULT");
        $display("=================================================");
        if (y > THRESHOLD)
            $display("  Prediction : PERSON     (y = %0d)", y);
        else
            $display("  Prediction : NO PERSON  (y = %0d)", y);
        $display("-------------------------------------------------");
        $display("  FPGA Latency  : %0.3f ns", fpga_latency_ns);
        $display("  CPU Latency   : %0.3f ns", CPU_LATENCY_NS);
        $display("  Speedup       : %0.2f x",  speedup);
        $display("=================================================");
        $display("");

        $finish;
    end

endmodule