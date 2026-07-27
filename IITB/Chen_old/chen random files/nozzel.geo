// Gmsh project created on Mon Jan 12 15:17:42 2026
SetFactory("OpenCASCADE");
//+
Point(1) = {0.0, 00.051, 0, 1.0};
//+
Point(2) = {0.102, 00.051, 0, 1.0};
//+
Point(3) = {0.102, 00.05049, 0, 1.0};
//+
Point(4) = {0.10251, 00.05049, 0, 1.0};
//+
Point(5) = {0.10251, 00.051, 0, 1.0};
//+
Point(6) = {0.178, 0.051, 0, 1.0};
//+
Point(7) = {0.192946, 0.050561, 0, 1.0};
//+
Point(8) = {0.229, 0.048, 0, 1.0};
//+
Point(9) = {0.28905, 0.05266, 0, 1.0};
//+
Point(10) = {0.63372, 0.10613, 0, 1.0};
//+
Point(11) = {0.735, 0.114, 0, 1.0};
//+
Point(12) = {1.041, 0.114, 0, 1.0};
//+
Point(13) = {1.0410, 0.0, 0, 1.0};
//+
Point(14) = {0.735, 0.0, 0, 1.0};
//+
Point(15) = {0.634, 0.0, 0, 1.0};
//+
Point(16) = {0.289, 0.0, 0, 1.0};
//+
Point(17) = {0.229, 0.0, 0, 1.0};
//+
Point(18) = {0.193, 0.0, 0, 1.0};
//+
Point(19) = {0.178, 0.0, 0, 1.0};
//+
Point(20) = {0.10251, 0.0, 0, 1.0};
//+
Point(21) = {0.102, 0.0, 0, 1.0};
//+
Point(22) = {0.0, 0.0, 0, 1.0};
//+
Point(23) = {0.0, 0.0, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {1, 22};
//+
Line(3) = {22, 21};
//+
Line(4) = {2, 3};
//+
Line(5) = {3, 4};
//+
Line(6) = {5, 4};
//+
Line(7) = {21, 20};
//+
Line(8) = {3, 21};
//+
Line(9) = {4, 20};
//+
Line(10) = {5, 6};
//+
Line(11) = {20, 19};
//+
Line(12) = {6, 7};
//+
Line(13) = {19, 18};
//+
Spline(14) = {7, 8};
//+
Spline(15) = {8, 9};
//+
Spline(16) = {18, 17};
//+
Spline(17) = {17, 16};
//+
Spline(18) = {9, 10};
//+
Spline(19) = {16, 15};
//+
Spline(20) = {10, 15};
//+
Spline(21) = {10, 11};
//+
Spline(22) = {11, 14};
//+
Spline(23) = {15, 14};
//+
Spline(24) = {11, 12};
//+
Spline(25) = {14, 13};
//+
Spline(26) = {12, 13};
//+
Spline(27) = {6, 19};
//+
Spline(28) = {7, 18};
//+
Spline(29) = {8, 17};
//+
Spline(30) = {9, 16};
//+
Curve Loop(1) = {1, 4, 8, -3, -2};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {8, 7, -9, -5};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {10, 27, -11, -9, -6};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {27, 13, -28, -12};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {28, 16, -29, -14};
//+
Plane Surface(5) = {5};
//+
Curve Loop(6) = {29, 17, -30, -15};
//+
Plane Surface(6) = {6};
//+
Curve Loop(7) = {30, 19, -20, -18};
//+
Plane Surface(7) = {7};
//+
Curve Loop(8) = {20, 23, -22, -21};
//+
Plane Surface(8) = {8};
//+
Curve Loop(9) = {22, 25, -26, -24};
//+
Plane Surface(9) = {9};
//+
Transfinite Surface {1} = {1, 2, 21, 22};
//+
Transfinite Surface {2} = {3, 4, 21, 20};
//+
Transfinite Surface {3} = {5, 6, 19, 20};
//+
Transfinite Surface {4} = {6, 7, 18, 19};
//+
Transfinite Surface {5} = {7, 8, 17, 18};
//+
Transfinite Surface {6} = {8, 9, 16, 17};
//+
Transfinite Surface {7} = {9, 10, 15, 16};
//+
Transfinite Surface {8} = {10, 11, 14, 15};
//+
Transfinite Surface {9} = {11, 12, 13, 14};
//+
Transfinite Curve {3, 1} = 11 Using Progression 1;
//+
Transfinite Curve {2} = 11 Using Progression 1;
//+
Transfinite Curve {4} = 2 Using Progression 1;
//+
Transfinite Curve {8} = 9 Using Progression 1;
//+
Transfinite Curve {8, 9} = 10 Using Progression 1;
//+
Transfinite Curve {5, 7} = 5 Using Progression 1;
//+
Transfinite Curve {27} = 11 Using Progression 1;
//+
Transfinite Curve {9} = 10 Using Progression 1;
//+
Transfinite Curve {6} = 2 Using Progression 1;
//+
Transfinite Curve {10, 11} = 10 Using Progression 1;
//+
Transfinite Curve {28} = 11 Using Progression 1;
//+
Transfinite Curve {12, 13} = 10 Using Progression 1;
//+
Transfinite Curve {14, 16} = 10 Using Progression 1;
//+
Transfinite Curve {29} = 11 Using Progression 1;
//+
Transfinite Curve {15, 17} = 10 Using Progression 1;
//+
Transfinite Curve {30} = 11 Using Progression 1;
//+
Transfinite Curve {18, 19} = 10 Using Progression 1;
//+
Transfinite Curve {20} = 11 Using Progression 1;
//+
Transfinite Curve {21, 23} = 10 Using Progression 1;
//+
Transfinite Curve {22} = 11 Using Progression 1;
//+
Transfinite Curve {24, 25} = 10 Using Progression 1;
//+
Transfinite Curve {26} = 11 Using Progression 1;
//+
Recombine Surface {1, 2, 3, 4, 5, 6, 7, 8, 9};
//+
Recursive Delete {
  Curve{20}; Curve{22}; Surface{4}; 
}
