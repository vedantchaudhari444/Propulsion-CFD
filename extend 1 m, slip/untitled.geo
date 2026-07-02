// ===================================================
// 2D Half Nozzle with 1.0 m Extension (STRUCTURED)
// ===================================================

SetFactory("OpenCASCADE");

// -----------------------------
L_noz = 1.0;
L_ext = 1.0;
L_tot = L_noz + L_ext;

// Equal divisions (VERY IMPORTANT)
N_stream = 120;   // along flow direction
N_normal = 60;    // vertical direction

// -----------------------------
// Points
// -----------------------------
wallPts[] = {};

For i In {0:N_stream}
  x = L_noz * i / N_stream;
  y = 0.36*x^3 - 0.54*x^2 + 0.36;
  p = newp;
  Point(p) = {x, y, 0, 1.0};
  wallPts[] += {p};
EndFor

// Extension
y_out = 0.18;

For i In {1:N_stream}
  x = L_noz + L_ext * i / N_stream;
  p = newp;
  Point(p) = {x, y_out, 0, 1.0};
  wallPts[] += {p};
EndFor

// -----------------------------
// Curves
// -----------------------------
top_wall = news;
Spline(top_wall) = wallPts[];

// Bottom (symmetry)
p1 = newp; Point(p1) = {0, 0, 0, 1.0};
p2 = newp; Point(p2) = {L_tot, 0, 0, 1.0};

bottom_wall = newl;
Line(bottom_wall) = {p2, p1};

// Inlet
p_in_top = wallPts[0];
inlet = newl;
Line(inlet) = {p1, p_in_top};

// Outlet
p_out_top = wallPts[#wallPts[]-1];
outlet = newl;
Line(outlet) = {p_out_top, p2};

// -----------------------------
// Surface
// -----------------------------
loop = newll;
Curve Loop(loop) = {inlet, top_wall, outlet, bottom_wall};

surface = news;
Plane Surface(surface) = {loop};

// -----------------------------
// NAMING (UPDATED)
// -----------------------------
Physical Line("INLET")   = {inlet};
Physical Line("OUTLET")  = {outlet};
Physical Line("TOPWALL") = {top_wall};
Physical Line("BOTWALL") = {bottom_wall};
Physical Surface("FLUID") = {surface};

// -----------------------------
// TRANSFINITE (STRUCTURED FIX)
// -----------------------------

// SAME divisions on opposite edges
Transfinite Curve {top_wall, bottom_wall} = N_stream + 1 Using Progression 1;

// SAME divisions on vertical edges
Transfinite Curve {inlet, outlet} = N_normal + 1 Using Progression 1;

// Structured grid
Transfinite Surface {surface};
Recombine Surface {surface};