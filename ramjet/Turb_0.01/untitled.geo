//+
SetFactory("Built-in");
//+
SetFactory("Built-in");
//+
SetFactory("Built-in");
//+
SetFactory("OpenCASCADE");

// -----------------------------
// Parameters
// -----------------------------
L = 1.0;          // Length
N = 50;           // Number of points on wall curve

// -----------------------------
// Create wall points from cubic
// y = 0.36*x^3 - 0.54*x^2 + 0.36
// -----------------------------
wallPts[] = {};

For i In {0:N}
  x = L * i / N;
  y = 0.36*x^3 - 0.54*x^2 + 0.36;
  p = newp;
  Point(p) = {x, y, 0, 1.0};
  wallPts[] += {p};
EndFor

// -----------------------------
// Wall spline
// -----------------------------
wall = news;
Spline(wall) = wallPts[];

// -----------------------------
// Inlet line
// -----------------------------
p_in_bot = newp;
Point(p_in_bot) = {0, 0, 0, 1.0};

p_in_top = wallPts[0];

inlet = newl;
Line(inlet) = {p_in_bot, p_in_top};

// -----------------------------
// Outlet line
// -----------------------------
p_out_bot = newp;
Point(p_out_bot) = {L, 0, 0, 1.0};

p_out_top = wallPts[#wallPts[]-1];

outlet = newl;
Line(outlet) = {p_out_top, p_out_bot};

// -----------------------------
// Symmetry line
// -----------------------------
symmetry = newl;
Line(symmetry) = {p_out_bot, p_in_bot};

// -----------------------------
// Create surface
// -----------------------------
loop = newll;
Curve Loop(loop) = {inlet, wall, outlet, symmetry};

surface = news;
Plane Surface(surface) = {loop};

// -----------------------------
// Physical groups (VERY IMPORTANT)
// -----------------------------
Physical Line("INLET") = {inlet};
Physical Line("OUTLET") = {outlet};
Physical Line("WALL") = {wall};
Physical Line("SYMMETRY") = {symmetry};
Physical Surface("FLUID") = {surface};
//+
Transfinite Curve {1} = 60 Using Progression 1;
//+
Transfinite Curve {2} = 20 Using Progression 1;
//+
Transfinite Curve {3} = 20 Using Progression 1;
//+
Transfinite Curve {4} = 60 Using Progression 1;
//+
Transfinite Surface {6};
//+
Recombine Surface {6};
