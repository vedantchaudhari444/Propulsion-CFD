// Gmsh project created on Fri Apr 04 14:30:33 2025
SetFactory("OpenCASCADE");
//+
SetFactory("OpenCASCADE");
//+
Point(1) = {0.2, 0, 0, 1.0};
//+
Point(2) = {0, 0, 0, 1.0};
//+
Point(3) = {0, 0.2, 0, 1.0};
//+
Point(4) = {0.2, 0.2, 0, 1.0};
//+
Line(1) = {2, 3};
//+
Line(2) = {1, 4};
//+
Line(3) = {2, 1};
//+
Line(4) = {3, 4};
//+
Curve Loop(1) = {1, 4, -2, -3};
//+
Curve Loop(2) = {1, 4, -2, -3};
//+
Curve Loop(3) = {1, 4, -2, -3};
//+
Surface(1) = {3};
