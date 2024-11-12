OPENQASM 3.0;
include "stdgates.inc";
input float[64] _θ_0_;
input float[64] _θ_1_;
input float[64] _θ_2_;
input float[64] _θ_3_;
input float[64] _θ_4_;
input float[64] _θ_5_;
input float[64] _θ_6_;
input float[64] _θ_7_;
input float[64] _θ_8_;
input float[64] _θ_9_;
qubit[5] q;
ry(_θ_0_) q[0];
ry(_θ_1_) q[1];
ry(_θ_2_) q[2];
ry(_θ_3_) q[3];
ry(_θ_4_) q[4];
cx q[3], q[4];
cx q[2], q[3];
cx q[1], q[2];
cx q[0], q[1];
ry(_θ_5_) q[0];
ry(_θ_6_) q[1];
ry(_θ_7_) q[2];
ry(_θ_8_) q[3];
ry(_θ_9_) q[4];
