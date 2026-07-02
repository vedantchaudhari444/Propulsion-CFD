SetFactory("OpenCASCADE");

L = 0.25;
N = 50;

wallPts[] = {};

For i In {0:N}
  x = L * i / N;

  // scale x to original polynomial domain
  xs = 2*x;   

  y = 0.36 + 2.88*xs^3 - 2.16*xs^2;

  p = newp;
  Point(p) = {x, y, 0, 1.0};
  wallPts[] += {p};
EndFor

wall = news;
Spline(wall) = wallPts[];

p_in_bot = newp;
Point(p_in_bot) = {0, 0, 0, 1.0};

p_out_bot = newp;
Point(p_out_bot) = {L, 0, 0, 1.0};

inlet = newl;
Line(inlet) = {p_in_bot, wallPts[0]};

outlet = newl;
Line(outlet) = {wallPts[#wallPts[]-1], p_out_bot};

symmetry = newl;
Line(symmetry) = {p_out_bot, p_in_bot};

loop = newll;
Curve Loop(loop) = {inlet, wall, outlet, symmetry};

surface = news;
Plane Surface(surface) = {loop};

Physical Line("INLET")    = {inlet};
Physical Line("OUTLET")   = {outlet};
Physical Line("WALL")     = {wall};
Physical Line("SYMMETRY") = {symmetry};
Physical Surface("FLUID") = {surface};

Transfinite Curve {inlet, outlet} = 20;
Transfinite Curve {wall, symmetry} = 60;

Transfinite Surface {surface};
Recombine Surface {surface};
