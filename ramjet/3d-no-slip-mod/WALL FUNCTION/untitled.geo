SetFactory("OpenCASCADE");

//======================================================
// 3D HALF-NOZZLE + STRAIGHT EXTENSION + EXIT
// TOTAL LENGTH = 2.0411 m
// EXTRUSION WIDTH = 0.36 m
//
// INTERNAL SECTIONS ARE ONLY USED FOR MESHING
// NO INTERFACE BOUNDARY CONDITIONS
//
// PHYSICAL BOUNDARIES:
// TOPWALL
// BOTWALL
// INLET
// OUTLET
// WALL
// FLUID
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
Nexit     = 20;

Nnormal = 80;
Nwidth  = 40;

// Moderate refinement toward TOPWALL
BLratio = 0.96;


//======================================================
// BOTTOM WALL POINTS
//======================================================

Point(1) = {0,0,0};
Point(2) = {1,0,0};
Point(3) = {2,0,0};
Point(4) = {2.0411,0,0};


//======================================================
// BOTTOM WALL CURVES
//======================================================

Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};


//======================================================
// TOP WALL : 0 -> 1 m
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
// TOP WALL : 1 -> 2 m
//======================================================

Point(1001) = {2.0,Hmid,0};

Line(5) = {pts[#pts[]-1],1001};


//======================================================
// TOP WALL : 2 -> 2.0411 m
//======================================================

Point(1002) = {2.0411,Hexit,0};

Line(6) = {1001,1002};


//======================================================
// VERTICAL LINES
//======================================================

// INLET
Line(7) = {1,p0};

// INTERNAL MESH DIVISION AT x = 1 m
Line(9) = {2,pts[#pts[]-1]};

// INTERNAL MESH DIVISION AT x = 2 m
Line(10) = {3,1001};

// OUTLET
Line(8) = {4,1002};


//======================================================
// SURFACE 1
//======================================================

Curve Loop(1) = {
    7,
    4,
    -9,
    -1
};

Plane Surface(1) = {1};


//======================================================
// SURFACE 2
//======================================================

Curve Loop(2) = {
    9,
    5,
    -10,
    -2
};

Plane Surface(2) = {2};


//======================================================
// SURFACE 3
//======================================================

Curve Loop(3) = {
    10,
    6,
    -8,
    -3
};

Plane Surface(3) = {3};


//======================================================
// TRANSFINITE STREAMWISE
//======================================================

Transfinite Curve {1,4}
    = Ncurve + 1 Using Progression 1;

Transfinite Curve {2,5}
    = Nstraight + 1 Using Progression 1;

Transfinite Curve {3,6}
    = Nexit + 1 Using Progression 1;


//======================================================
// WALL-NORMAL REFINEMENT
//======================================================

Transfinite Curve {7,9,10,8}
    = Nnormal + 1 Using Progression BLratio;


//======================================================
// TRANSFINITE SURFACES
//======================================================

Transfinite Surface {1}
    = {1,p0,pts[#pts[]-1],2};

Transfinite Surface {2}
    = {2,pts[#pts[]-1],1001,3};

Transfinite Surface {3}
    = {3,1001,1002,4};


//======================================================
// STRUCTURED QUADRILATERAL MESH
//======================================================

Recombine Surface {1,2,3};


//======================================================
// EXTRUDE TO 3D
//======================================================
//
// Store the generated entities so boundary names
// are attached to the correct surfaces.
//======================================================

out[] = Extrude {0,0,W}
{
    Surface{1,2,3};

    Layers{Nwidth};

    Recombine;
};


//======================================================
// PHYSICAL VOLUME
//======================================================
//
// For the three extruded surfaces, the extrusion
// returns the created volumes in the returned list.
// The actual volume entities are therefore used below.
//======================================================

Physical Volume("Fluid") =
{
    out[1],
    out[7],
    out[13]
};


//======================================================
// PHYSICAL BOUNDARIES
//======================================================
//
// The lateral surface generated from each original
// boundary curve is assigned using the extrusion
// return ordering:
//
// Surface 1:
//   7  = INLET
//   4  = TOPWALL
//   9  = INTERNAL
//   1  = BOTWALL
//
// Surface 2:
//   9  = INTERNAL
//   5  = TOPWALL
//   10 = INTERNAL
//   2  = BOTWALL
//
// Surface 3:
//   10 = INTERNAL
//   6  = TOPWALL
//   8  = OUTLET
//   3  = BOTWALL
//
// The original 2D surfaces and their opposite
// extruded surfaces form WALL (z=0 and z=W).
//======================================================


// INLET
Physical Surface("Inlet") =
{
    out[2]
};


// OUTLET
Physical Surface("Outlet") =
{
    out[16]
};


// TOP WALL
Physical Surface("Topwall") =
{
    out[3],
    out[9],
    out[15]
};


// BOTTOM WALL
Physical Surface("Botwall") =
{
    out[5],
    out[11],
    out[17]
};


// SIDE WALLS
// z = 0 and z = 0.36
Physical Surface("Wall") =
{
    1,
    2,
    3,
    out[0],
    out[6],
    out[12]
};


//======================================================
// MESH OPTIONS
//======================================================

Mesh.RecombineAll = 1;
Mesh.Smoothing = 10;