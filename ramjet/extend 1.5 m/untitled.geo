// ===================================================
// 2D Half Nozzle with Downstream Extension (1.5 m)
// Single WALL and SYMMETRY boundaries
// ===================================================

SetFactory("OpenCASCADE");

// -----------------------------
// Parameters
// -----------------------------
L_noz = 1.0;        // Nozzle length
L_ext = 1.5;        // Extension length
L_tot = L_noz + L_ext;

N_noz = 50;         // Points on nozzle wall
N_ext = 20;         // Points on extension wall

// -----------------------------
// Nozzle wall (cubic curve)
// y = 0.36*x^3 - 0.54*x^2 + 0.36
// -----------------------------
wallPts[] = {};

For i In {0:N_noz}
  x = L_noz * i / N_noz;
  y = 0.36*x^3 - 0.54*x^2 + 0.36;
  p = newp;
  Point(p) = {x, y, 0, 1.0};
  wallPts[] += {p};
EndFor

// -----------------------------
// Extension wall (straight)
// -----------------------------
y_out = 0.18;   // outlet half height

For i In {1:N_ext}
  x = L_noz + L_ext * i / N_ext;
  p = newp;
  Point(p) = {x, y_out, 0, 1.0};
  wallPts[] += {p};
EndFor

// -----------------------------
// Top wall spline (single WALL)
// -----------------------------
wall = news;
Spline(wall) = wallPts[];

// -----------------------------
// Bottom symmetry line (single SYMMETRY)
// -----------------------------
p_sym_in = newp;
Point(p_sym_in) = {0, 0, 0, 1.0};

p_sym_out = newp;
Point(p_sym_out) = {L_tot, 0, 0, 1.0};

symmetry = newl;
Line(symmetry) = {p_sym_out, p_sym_in};

// -----------------------------
// Inlet
// -----------------------------
p_in_top = wallPts[0];

inlet = newl;
Line(inlet) = {p_sym_in, p_in_top};

// -----------------------------
// Outlet
// -----------------------------
p_out_top = wallPts[#wallPts[]-1];

outlet = newl;
Line(outlet) = {p_out_top, p_sym_out};

// -----------------------------
// Create surface
// -----------------------------
loop = newll;
Curve Loop(loop) = {inlet, wall, outlet, symmetry};

surface = news;
Plane Surface(surface) = {loop};

// -----------------------------
// Physical groups
// -----------------------------
Physical Line("INLET")    = {inlet};
Physical Line("OUTLET")   = {outlet};
Physical Line("WALL")     = {wall};
Physical Line("SYMMETRY") = {symmetry};
Physical Surface("FLUID") = {surface};

// -----------------------------
// Transfinite definitions
// -----------------------------
Transfinite Curve {inlet, outlet} = 20 Using Progression 1;
Transfinite Curve {wall, symmetry} = 80 Using Progression 1;

Transfinite Surface {surface};
Recombine Surface {surface};
