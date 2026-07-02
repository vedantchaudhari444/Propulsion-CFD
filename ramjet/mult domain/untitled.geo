// ======================================
// CLEAN 2-ZONE STRUCTURED SCRIPT
// ======================================

SetFactory("OpenCASCADE");

// -----------------------------
L1 = 1.0;   // zone 1 length
L2 = 1.0;   // zone 2 length
H1 = 0.36;  // inlet height
H2 = 0.18;  // outlet height

Nx = 80;
Ny = 60;

// -----------------------------
// POINTS
p1 = newp; Point(p1) = {0, 0, 0, 1};
p2 = newp; Point(p2) = {L1, 0, 0, 1};
p3 = newp; Point(p3) = {L1+L2, 0, 0, 1};

p4 = newp; Point(p4) = {0, H1, 0, 1};
p5 = newp; Point(p5) = {L1, H2, 0, 1};
p6 = newp; Point(p6) = {L1+L2, H2, 0, 1};

// -----------------------------
// CURVES

// bottom
bot1 = newl; Line(bot1) = {p2, p1};
bot2 = newl; Line(bot2) = {p3, p2};

// top
top1 = newl; Line(top1) = {p4, p5};
top2 = newl; Line(top2) = {p5, p6};

// inlet/outlet
inlet  = newl; Line(inlet)  = {p1, p4};
outlet = newl; Line(outlet) = {p6, p3};

// interface (duplicate)
int1 = newl; Line(int1) = {p5, p2};
int2 = newl; Line(int2) = {p2, p5};

// -----------------------------
// SURFACE 1
loop1 = newll;
Curve Loop(loop1) = {inlet, top1, int1, bot1};
s1 = news;
Plane Surface(s1) = {loop1};

// -----------------------------
// SURFACE 2
loop2 = newll;
Curve Loop(loop2) = {int2, top2, outlet, bot2};
s2 = news;
Plane Surface(s2) = {loop2};

// -----------------------------
// PHYSICAL GROUPS
Physical Surface("ZONE_1") = {s1};
Physical Surface("ZONE_2") = {s2};

Physical Line("INLET") = {inlet};
Physical Line("OUTLET") = {outlet};

Physical Line("TOPWALL_1") = {top1};
Physical Line("TOPWALL_2") = {top2};

Physical Line("BOTWALL_1") = {bot1};
Physical Line("BOTWALL_2") = {bot2};

Physical Line("INTERFACE_1") = {int1};
Physical Line("INTERFACE_2") = {int2};

// -----------------------------
// TRANSFINITE (MATCHING)
Transfinite Curve {top1, bot1} = Nx+1;
Transfinite Curve {top2, bot2} = Nx+1;

Transfinite Curve {inlet, int1, int2, outlet} = Ny+1;

Transfinite Surface {s1};
Transfinite Surface {s2};

Recombine Surface {s1};
Recombine Surface {s2};