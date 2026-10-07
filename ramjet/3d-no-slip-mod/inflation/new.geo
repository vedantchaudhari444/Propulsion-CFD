SetFactory("OpenCASCADE");

//======================================================
// 3D HALF NOZZLE
// TOTAL LENGTH = 2.0411 m
// WIDTH       = 0.36 m
//
// 3 STRUCTURED HEX BLOCKS
//
// BLOCK 1 : 0 -> 1.0 m
// BLOCK 2 : 1 -> 2.0 m
// BLOCK 3 : 2 -> 2.0411 m
//
// INTERNAL INTERFACES ARE NOT PHYSICAL BOUNDARIES
//======================================================


//======================================================
// PARAMETERS
//======================================================

Lcurve    = 1.0;
Lstraight = 1.0;
Lexit     = 0.0411;

Hin   = 0.36;
Hmid  = 0.18;
Hexit = 0.1764;

W = 0.36;


//======================================================
// MESH PARAMETERS
//======================================================

Ncurve    = 100;
Nstraight = 100;
Nexit     = 30;

Nnormal = 100;
Nwidth  = 100;

// Fine cells toward TOPWALL
TopRatio = 0.93;


//======================================================
// BOTTOM WALL POINTS
//======================================================

Point(1) = {0,      0,0};
Point(2) = {1.0,    0,0};
Point(3) = {2.0,    0,0};
Point(4) = {2.0411, 0,0};


//======================================================
// TOP WALL - CURVED SECTION
// 0 -> 1 m
//
// y = 0.36*x^3 - 0.54*x^2 + 0.36
//======================================================

p0 = newp;
Point(p0) = {0,Hin,0};

pts[] = {p0};

For i In {1:Ncurve}

    x = i/Ncurve;
    y = 0.36*x^3 - 0.54*x^2 + 0.36;

    p = newp;
    Point(p) = {x,y,0};

    pts[] += {p};

EndFor

Spline(4) = pts[];


//======================================================
// TOP WALL - STRAIGHT SECTION
// 1 -> 2 m
//======================================================

Point(1001) = {2.0,Hmid,0};

Line(5) = {pts[#pts[]-1],1001};


//======================================================
// TOP WALL - EXIT SECTION
// 2 -> 2.0411 m
//======================================================

Point(1002) = {2.0411,Hexit,0};

Line(6) = {1001,1002};


//======================================================
// BOTTOM WALL
//======================================================

Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};


//======================================================
// INLET
//======================================================

Line(7) = {1,p0};


//======================================================
// INTERNAL INTERFACE 1
// x = 1 m
//======================================================

Line(9) = {2,pts[#pts[]-1]};


//======================================================
// INTERNAL INTERFACE 2
// x = 2 m
//======================================================

Line(10) = {3,1001};


//======================================================
// OUTLET
//======================================================

Line(8) = {4,1002};


//======================================================
// BLOCK 1 : 0 -> 1 m
//======================================================

Curve Loop(1) = {
    7,
    4,
    -9,
    -1
};

Plane Surface(1) = {1};


//======================================================
// BLOCK 2 : 1 -> 2 m
//======================================================

Curve Loop(2) = {
    9,
    5,
    -10,
    -2
};

Plane Surface(2) = {2};


//======================================================
// BLOCK 3 : 2 -> 2.0411 m
//======================================================

Curve Loop(3) = {
    10,
    6,
    -8,
    -3
};

Plane Surface(3) = {3};


//======================================================
// TRANSFINITE BLOCK 1
//======================================================

Transfinite Curve {1,4}
    = Ncurve + 1 Using Progression 1;

// Bottom/top node count must match
Transfinite Curve {7}
    = Nnormal + 1 Using Progression TopRatio;

Transfinite Curve {9}
    = Nnormal + 1 Using Progression (1/TopRatio);

Transfinite Surface {1}
    = {1,p0,pts[#pts[]-1],2};


//======================================================
// TRANSFINITE BLOCK 2
//======================================================

Transfinite Curve {2,5}
    = Nstraight + 1 Using Progression 1;

Transfinite Curve {9}
    = Nnormal + 1 Using Progression (1/TopRatio);

Transfinite Curve {10}
    = Nnormal + 1 Using Progression (1/TopRatio);

Transfinite Surface {2}
    = {2,pts[#pts[]-1],1001,3};


//======================================================
// TRANSFINITE BLOCK 3
//======================================================

Transfinite Curve {3,6}
    = Nexit + 1 Using Progression 1;

Transfinite Curve {10}
    = Nnormal + 1 Using Progression (1/TopRatio);

Transfinite Curve {8}
    = Nnormal + 1 Using Progression TopRatio;

Transfinite Surface {3}
    = {3,1001,1002,4};


//======================================================
// RECOMBINE 2D SOURCE SURFACES
//======================================================

Recombine Surface {1,2,3};


//======================================================
// EXTRUDE ALL BLOCKS TOGETHER
//======================================================

Extrude {0,0,W}
{
    Surface{1,2,3};
    Layers{Nwidth};
    Recombine;
}


//======================================================
// PHYSICAL BOUNDARIES
//
// IMPORTANT:
// Internal interfaces x=1 and x=2 are NOT included.
// Therefore they are NOT walls or boundary conditions.
//======================================================

// Inlet
Physical Surface("Inlet") = {8};

// Outlet
Physical Surface("Outlet") = {11};

// Bottom wall
Physical Surface("Botwall") = {7,6,12};

// Top wall
Physical Surface("Topwall") = {3,4,10};

// Remaining external side surfaces
Physical Surface("Wall") = {9,13,1,2};

// Fluid volume
Physical Volume("Fluid") = {1,2,3};


//======================================================
// FINAL QUAD/HEX RECOMBINATION
//======================================================

Recombine Surface {
    8,
    3,
    7,
    1,
    4,
    9,
    10,
    6,
    5,
    2,
    13,
    12,
    11
};


//======================================================
// MESH OPTIONS
//======================================================

Mesh.RecombineAll = 1;
Mesh.Smoothing = 10;