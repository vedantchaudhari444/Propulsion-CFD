SetFactory("OpenCASCADE");

//======================================================
// PARAMETERS
//======================================================

Lcurve    = 1.0;
Lstraight = 1.0;
Lexit     = 0.0411;

Hin    = 0.36;
Hmid   = 0.18;
Hexit  = 0.1764;

//======================================================
// BOTTOM WALL
//======================================================

Point(1) = {0,0,0};
Point(2) = {1,0,0};
Point(3) = {2,0,0};
Point(4) = {2.0411,0,0};

Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};

//======================================================
// TOP WALL
//======================================================

p0 = newp;
Point(p0) = {0,Hin,0};

pts[] = {p0};

// Cubic curve (0 → 1 m)
For i In {1:100}

    x = i/100.0;
    y = 0.36*x^3 - 0.54*x^2 + 0.36;

    p = newp;
    Point(p) = {x,y,0};

    pts += {p};

EndFor

Spline(4) = pts[];

// Straight section (1 → 2 m)

Point(1001) = {2.0,Hmid,0};
Line(5) = {pts[#pts[]-1],1001};

// Exit section (2 → 2.0411 m)

Point(1002) = {2.0411,Hexit,0};
Line(6) = {1001,1002};

//======================================================
// SIDES
//======================================================

Line(7) = {1,p0};
Line(8) = {4,1002};

Line(9) = {1001, 3};
//+
Curve Loop(1) = {4, 5, 9, -2, -1, 7};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {6, -8, -3, -9};
//+
Plane Surface(2) = {2};
//+
Transfinite Surface {1} = {5, 1, 1001, 3};
//+
Transfinite Curve {2, 1, 1, 5, 4} = 100 Using Progression 1;
//+
Transfinite Curve {7, 9} = 70 Using Progression 1;
//+
Transfinite Curve {6, 3} = 30 Using Progression 1;
//+
Transfinite Curve {9, 8} = 70 Using Progression 1;
//+
Recombine Surface {1, 2};
//+
Transfinite Surface {2} = {1002, 1001, 3, 4};
//+
Extrude {0, 0, 0.36} {
  Surface{1}; Surface{2}; Layers {100}; Recombine;
}
//+
Physical Surface("Wall", 27) = {9, 13, 1, 2};
//+
Physical Surface("Botwall", 28) = {7, 6, 12};
//+
Physical Surface("Topwall", 29) = {3, 4, 10};
//+
Physical Surface("Inlet", 30) = {8};
//+
Physical Surface("Outlet", 31) = {11};
//+
Recombine Surface {8, 3, 7, 1, 4, 9, 10, 6, 5, 2, 13, 12, 11};
