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
input float[64] _θ_10_;
input float[64] _θ_11_;
input float[64] _θ_12_;
input float[64] _θ_13_;
input float[64] _θ_14_;
input float[64] _θ_15_;
input float[64] _θ_16_;
input float[64] _θ_17_;
input float[64] _θ_18_;
input float[64] _θ_19_;
input float[64] _θ_20_;
input float[64] _θ_21_;
input float[64] _θ_22_;
input float[64] _θ_23_;
input float[64] _θ_24_;
input float[64] _θ_25_;
input float[64] _θ_26_;
input float[64] _θ_27_;
input float[64] _θ_28_;
input float[64] _θ_29_;
input float[64] _θ_30_;
input float[64] _θ_31_;
input float[64] _θ_32_;
input float[64] _θ_33_;
input float[64] _θ_34_;
input float[64] _θ_35_;
input float[64] _θ_36_;
input float[64] _θ_37_;
input float[64] _θ_38_;
input float[64] _θ_39_;
qubit[10] q;
ry(_θ_0_) q[0];
ry(_θ_1_) q[1];
ry(_θ_2_) q[2];
ry(_θ_3_) q[3];
ry(_θ_4_) q[4];
ry(_θ_5_) q[5];
ry(_θ_6_) q[6];
ry(_θ_7_) q[7];
ry(_θ_8_) q[8];
ry(_θ_9_) q[9];
rz(_θ_10_) q[0];
rz(_θ_11_) q[1];
rz(_θ_12_) q[2];
rz(_θ_13_) q[3];
rz(_θ_14_) q[4];
rz(_θ_15_) q[5];
rz(_θ_16_) q[6];
rz(_θ_17_) q[7];
rz(_θ_18_) q[8];
rz(_θ_19_) q[9];
cx q[8], q[9];
cx q[7], q[8];
cx q[6], q[7];
cx q[5], q[6];
cx q[4], q[5];
cx q[3], q[4];
cx q[2], q[3];
cx q[1], q[2];
cx q[0], q[1];
ry(_θ_20_) q[0];
ry(_θ_21_) q[1];
ry(_θ_22_) q[2];
ry(_θ_23_) q[3];
ry(_θ_24_) q[4];
ry(_θ_25_) q[5];
ry(_θ_26_) q[6];
ry(_θ_27_) q[7];
ry(_θ_28_) q[8];
ry(_θ_29_) q[9];
rz(_θ_30_) q[0];
rz(_θ_31_) q[1];
rz(_θ_32_) q[2];
rz(_θ_33_) q[3];
rz(_θ_34_) q[4];
rz(_θ_35_) q[5];
rz(_θ_36_) q[6];
rz(_θ_37_) q[7];
rz(_θ_38_) q[8];
rz(_θ_39_) q[9];
