SetFactory("OpenCASCADE"); 
Merge "untitled.iges"; 
//+ 
Transfinite Surface {1};
 //+ 
Transfinite Curve {1, 3} = 70 Using Progression 1; 
//+ 
Recombine Surface {1}; 
//+ 
Transfinite Curve {2, 4} = 100 Using Progression 1;
//+
Extrude {0, 0, 0.36} {
  Surface{1}; Layers {100}; Recombine;
}
//+
Physical Surface("Inlet", 13) = {2};
//+
Physical Surface("Wall", 14) = {6, 1};
//+
Physical Surface("Botwall", 15) = {5};
//+
Physical Surface("Topwall", 16) = {3};
//+
Physical Surface("Outlet", 17) = {4};
