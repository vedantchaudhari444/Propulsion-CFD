// Gmsh project created on Fri Apr 04 09:41:21 2025
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0, 0.064, 0, 1.0};
//+
Circle(1) = {0, 0.027932, 0, 0.036068, 0, 0.174*Pi};
//+
Rotate {{0, 0, 1}, {0, 0.027932, 0}, 0.326*Pi} {
  Curve{1}; 
}
//+
Point(5) = {0.09029, 0, 0, 1.0};
//+
Point(6) = {0.09029, 0.0229, 0, 1.0};
//+
Recursive Delete {
  Point{6}; 
}
//+
Circle(2) = {0.09029, 0.06862, 0, 0.04572, 0, 0.258*Pi};
//+
Rotate {{0, 0, 1}, {0.09029, 0.06862, 0}, -0.5*Pi} {
  Curve{2}; 
}
//+
Rotate {{0, 0, 1}, {0.09029, 0.06862, 0}, -0.174*Pi} {
  Curve{2}; 
}
//+
Recursive Delete {
  Point{5}; 
}
//+
Point(8) = {0.066479, 0, 0, 1.0};
//+
Point(9) = {0.10218, 0, 0, 1.0};
//+
Point(10) = {0.150495, 0, 0, 1.0};
//+
Point(11) = {0.150495, 0.037296, 0, 1.0};
//+
Line(3) = {1, 2};
//+
Line(4) = {10, 11};
//+
Point(12) = {0.018769, 0, 0, 1.0};
//+
Line(5) = {1, 12};
//+
Line(6) = {12, 8};
//+
Line(7) = {3, 6};
//+
Line(8) = {8, 9};
//+
Line(9) = {9, 10};
//+
Line(10) = {7, 11};
//+
Recursive Delete {
  Curve{3}; 
}
//+
Line(11) = {1, 4};
//+
Curve Loop(1) = {11, -1, 7, 2, 10, -4, -9, -8, -6, -5};
//+
Surface(1) = {1};
//+
Physical Surface("fluid", 12) = {1};
//+
Physical Curve("inlet", 13) = {11};
//+
Physical Curve("outlet", 14) = {4};
//+
Physical Curve("wall", 15) = {1, 7, 2, 10};
//+
Physical Curve("symmetry", 16) = {5, 6, 8, 9};
//+
Transfinite Surface {1};
//+
Transfinite Surface {1} = {1, 4, 11, 10};
//+
Transfinite Curve {11, 4} = 50 Using Progression 1;
//+
Transfinite Curve {1, 5} = 15 Using Progression 1;
//+
Transfinite Curve {7, 6} = 45 Using Progression 1;
//+
Transfinite Curve {2, 8} = 30 Using Progression 1;
//+
Transfinite Curve {10, 9} = 35 Using Progression 1;
//+
Transfinite Curve {11, 4} = 20 Using Progression 1;
//+
Transfinite Curve {1, 5} = 5 Using Progression 1;
//+
Transfinite Curve {7, 6} = 15 Using Progression 1;
//+
Transfinite Curve {2, 8} = 10 Using Progression 1;
//+
Transfinite Curve {10, 9} = 10 Using Progression 1;
//+
Transfinite Curve {10, 9} = 12 Using Progression 1;
//+
Transfinite Curve {1, 5} = 6 Using Progression 1;
//+
Transfinite Curve {2, 8} = 11 Using Progression 1;
//+
Transfinite Curve {10, 9} = 13 Using Progression 1;
//+
Transfinite Curve {11, 4} = 30 Using Progression 1;
//+
Transfinite Curve {1, 5} = 9 Using Progression 1;
//+
Transfinite Curve {7, 6} = 23 Using Progression 1;
//+
Transfinite Curve {2, 8} = 17 Using Progression 1;
//+
Transfinite Curve {10, 9} = 20 Using Progression 1;
//+
Transfinite Curve {11, 4} = 45 Using Progression 1;
//+
Transfinite Curve {1, 5} = 14 Using Progression 1;
//+
Transfinite Curve {7, 6} = 35 Using Progression 1;
//+
Transfinite Curve {2, 8} = 26 Using Progression 1;
//+
Transfinite Curve {10, 9} = 30 Using Progression 1;
//+
Transfinite Curve {10, 9} = 30 Using Bump 1.02;
//+
Transfinite Curve {10, 9} = 30 Using Bump 1.1;
//+
Transfinite Curve {10, 9} = 30 Using Bump 2;
//+
Transfinite Curve {10, 9} = 40 Using Bump 5;
//+
Transfinite Curve {10, 9} = 60 Using Bump 10;
//+
Transfinite Curve {11, 4} = 60 Using Progression 1.5;
//+
Transfinite Curve {11, 4} = 60 Using Progression 0.75;
//+
Transfinite Curve {11, 4} = 60 Using Progression 0.95;
//+
Recombine Surface {1};
//+
Transfinite Curve {9, 10} = 80 Using Bump 10;
//+
Transfinite Curve {6, 9, 10} = 80 Using Progression 1;
//+
Transfinite Curve {9, 10} = 80 Using Progression 1;
//+
Transfinite Curve {6} = 35 Using Progression 1;
//+
Transfinite Curve {10, 9} = 35 Using Progression 1;
//+
Transfinite Curve {11, 4} = 60 Using Progression 0.9;
//+
Transfinite Curve {11, 4} = 60 Using Progression 0.92;
//+
Transfinite Curve {11, 4} = 60 Using Progression 0.91;
//+
Physical Curve(" wall", 15) -= {1, 7, 2, 10};
//+
Physical Curve(" symmetry", 16) -= {5, 6, 8, 9};
//+
Physical Curve(" inlet", 13) -= {11};
//+
Physical Curve(" outlet", 14) -= {4};
//+
Physical Curve("INLET", 17) = {11};
//+
Physical Curve("OUTLET", 18) = {4};
//+
Physical Curve("WALL", 19) = {1, 7, 2, 10, 5, 6, 8, 9};
