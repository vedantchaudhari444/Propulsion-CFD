% Root Finding Methods
% Written by: JoshTheEngineer
% Website   : www.joshtheengineer.com
% YouTube   : www.youtube.com/user/joshtheengineer
% Started: 10/11/16
% Updated: 10/11/16 - Started code
%                   - Works as expected
%
% PURPOSE
%  - Solve the Area-Mach Number equation for Mach number
%  - Demonstrate a few different root finding methods

clear;
clc;

%% INPUTS

% Define some paramters
g   = 1.4;
gm1 = g-1;
gp1 = g+1;

% Define anonymous function with two inputs (M and ARatio)
% - Will be used in the methods below
% - Pass M and ARatio as arguments to AM_EQN to get function value
% -     funVal = AM_EQN(M,ARatio)
AM_EQN = @(M,ARatio) sqrt((1/M^2)*(((2+gm1*M^2)/gp1)^...
                            (gp1/gm1)))-ARatio;

% Solve for Msub and Msup using this area ratio (A/A*)
ARatio = readmatrix("C:\Users\adity\Documents\IITB_Internship\SU2\SU2_Projects\CD_Nozzle26\Codes\Ar.csv");
%ARatio = 5;

% Error tolerance
errTol = 1e-4;

% Flags for printing iterations to screen
verboseBisection   = 0;
verboseIncremental = 0;
%ARatio(100)


%% PLOT THE EQUATION

M       = linspace(0.03,5,100)';
A_Astar = sqrt((1./M.^2).*(((2+gm1.*M.^2)/gp1).^(gp1/gm1)));

figure(1);
cla; hold on; grid on; box on;
plot(A_Astar,M,'r-','LineWidth',3);
xlabel('$\frac{A}{A^*}$','Interpreter','Latex','FontSize',22,...
                            'FontName','Arial');
ylabel('$M$','Interpreter','Latex','FontSize',22,...
                            'FontName','Arial');
set(gcf,'Color','w');
set(gca,'XMinorTick','On','YMinorTick','On');
set(gca,'LineWidth',2.5,'FontSize',22);
set(gca,'TickLength',1.5*get(gca,'TickLength'));

%% MATLAB SOLVER

% Set up the solver
for k=1:length(ARatio)
problem.objective = @(M) (1/M^2)*(((2+gm1*M^2)/gp1)^(gp1/gm1))-ARatio^2;    % Objective function
problem.solver    = 'fzero';                                                % Find the zero
problem.options   = optimset(@fzero);                                       % Default options

% Solve subsonic root
problem.x0 = [1e-6 1];                                                      % Subsonic solver bounds
Msub       = fzero(problem);                                                % Solve for subsonic M
problem.x0 = [1+1e-6 50];                                                   % Supersonic solver bounds
Msup       = fzero(problem);                                                % Solve for supersonic M

% Print solutions to command window
fprintf('==== MATLAB SOLVER ====\n');
fprintf('Msub: %3.4f\n',Msub);
fprintf('Msup: %3.4f\n',Msup);
fprintf('=======================\n\n');
end

%% SUBSONIC INCREMENTAL SEARCH
for k=1:length(ARatio)
% Initial values
dM       = 0.1;                                                             % Initial M step size
M        = 1e-6;                                                            % Initial M value
iConvSub = 0;                                                               % Initial converge index

if (verboseIncremental == 1)
    fprintf('Incremental Search Method: Subsonic\n');
    fprintf('-----------------------------------\n');
end

% Iterate to solve for root
iterMax = 100;                                                              % Maximum iterations
stepMax = 100;
% Maximum step iterations

for i = 1:1:iterMax
    for j = 1:1:stepMax
        
        % Evaluate function at j and j+1
        fj   = AM_EQN(M,ARatio(k));
        fjp1 = AM_EQN(M+dM,ARatio(k));
        
        % Print iterations to command window
        if (verboseIncremental == 1)
            fprintf('fj | fjp1: %3.4f\t%3.4f\n',fj,fjp1);
        end
        
        % Update M depending on sign change or not
        % - If no sign change, then we are not bounding root yet
        % - If sign change, then we are bounding the root, update dM
        if (fj*fjp1 > 0)
            M = M + dM;                                                     % Update M
        elseif (fj*fjp1 < 0)
            dM = dM*0.1;                                                    % Refine the M increment
            break;                                                          % Break out of j loop
        end
        
    end % END: j Loop
    
    % Check for convergence
    if (abs(fj-fjp1) <= errTol)                                             % If converged
        iConvSub = i;                                                       % Set converged index
        break;                                                              % Exit loop
    end
    
end % END: i Loop

% Set subsonic Mach number to final M from iterations
Msub(k) = M;
end
%% Writing subsonic soln to csv file
% Specify the filename for the CSV file
filename = 'subsonic.csv';

% Open the file for writing
fileID = fopen(filename, 'w');

% Check if the file was opened successfully
if fileID == -1
    error('Could not open file for writing.');
end

% Write the header row (optional, but good practice)
fprintf(fileID, 'Msubsonic\n');

% Write the data rows
for i = 1:length(Msub)
    fprintf(fileID, '%f\n', Msub(i));
end

% Close the file
fclose(fileID);

disp(['Data successfully written to ', filename]);
%% SUPERSONIC INCREMENTAL SEARCH
for k=1:length(ARatio)
% Initial values
dM       = 1;                                                               % Initial M step size
M        = 1+1e-6;                                                          % Initial M value
iConvSup = 0;                                                               % Initial converge index

if (verboseIncremental == 1)
    fprintf('\nIncremental Search Method: Supersonic\n');
    fprintf('-------------------------------------\n');
end

% Iterate to solve for root
iterMax = 100;                                                              % Maximum iterations
stepMax = 100;
% Maximum step iterations
for i = 1:1:iterMax
    for j = 1:1:stepMax
        
        % Evaluate function at j and j+1
        fj   = AM_EQN(M,ARatio(k));
        fjp1 = AM_EQN(M+dM,ARatio(k));
        
        % Print iterations to command window
        if (verboseIncremental == 1)
            fprintf('fj | fjp1: %3.4f\t%3.4f\n',fj,fjp1);
        end
        
        % Update M depending on sign change or not
        % - If no sign change, then we are not bounding root yet
        % - If sign change, then we are bounding the root, update dM
        if (fj*fjp1 > 0)
            M = M + dM;                                                     % Update M
        elseif (fj*fjp1 < 0)
            dM = dM*0.1;                                                    % Refine the M increment
            break;                                                          % Break out of j loop
        end
        
    end % END: j Loop
    
    % Check for convergence
    if (abs(fj-fjp1) <= errTol)                                             % If converged
        iConvSup = i;                                                       % Set converged index
        break;                                                              % Exit loop
    end
    
end % END: i Loop

% Set supersonic Mach number to final M from iterations
Msup(k) = M;
end

% Print solutions to command window
%fprintf('==== INCREMENTAL SEARCH SOLVER ====\n');
%fprintf('Msub: %3.4f after %i iterations\n',Msub,iConvSub);
%fprintf('Msup: %3.4f after %i iterations\n',Msup,iConvSup);
%fprintf('===================================\n\n');
%% Writing supersonic soln to csv file
% Specify the filename for the CSV file
filename = 'supersonic.csv';

% Open the file for writing
fileID = fopen(filename, 'w');

% Check if the file was opened successfully
if fileID == -1
    error('Could not open file for writing.');
end

% Write the header row (optional, but good practice)
fprintf(fileID, 'Msupersonic\n');

% Write the data rows
for i = 1:length(Msup)
    fprintf(fileID, '%f\n', Msup(i));
end

% Close the file
fclose(fileID);

disp(['Data successfully written to ', filename]);


%% Pressure values

P0 = 1038350.4;
%% Psup calculation
for i = 1:length(Msup)
    M = Msup(i);
Psup(i) = P0*(1+(M*M*(g-1)/2))^(g/(1-g));
end
%% Psup to csv
% Specify the filename for the CSV file
filename = 'Psupersonic.csv';

% Open the file for writing
fileID = fopen(filename, 'w');

% Check if the file was opened successfully
if fileID == -1
    error('Could not open file for writing.');
end

% Write the header row (optional, but good practice)
fprintf(fileID, 'Psupersonic\n');

% Write the data rows
for i = 1:length(Psup)
    fprintf(fileID, '%f\n', Psup(i));
end

% Close the file
fclose(fileID);

disp(['Data successfully written to ', filename]);
%% Psub calculation
for i = 1:length(Msub)
    M = Msub(i);
Psub(i) = P0*(1+(M*M*(g-1)/2))^(g/(1-g));
end
%% Psub to csv
% Specify the filename for the CSV file
filename = 'Psubsonic.csv';

% Open the file for writing
fileID = fopen(filename, 'w');

% Check if the file was opened successfully
if fileID == -1
    error('Could not open file for writing.');
end

% Write the header row (optional, but good practice)
fprintf(fileID, 'Psubsonic\n');

% Write the data rows
for i = 1:length(Psub)
    fprintf(fileID, '%f\n', Psub(i));
end

% Close the file
fclose(fileID);

disp(['Data successfully written to ', filename]);
%% SUBSONIC BISECTION

% Initial Mach number bounds
MLo = 1e-6;         % Initial lower bound of Mach number
MHi = 1;            % Initial upper bound of Mach number

iterMax = 100;
for i = 1:1:iterMax
    % Calculate middle Mach number
    MMid = 0.5*(MLo+MHi);
    
    % Evaluate Lo, Mid, and Hi function values
    fMLo  = AM_EQN(MLo,ARatio);
    fMMid = AM_EQN(MMid,ARatio);
    fMHi  = AM_EQN(MHi,ARatio);
    
    % Print iteration to command window
    if (verboseBisection == 1)
        fprintf('fM(%i): %3.4f\t%3.4f\t%3.4f\n',i,fMLo,fMMid,fMHi);
    end
    
    % Update Mach numbers based on sign changes
    % - If the product is positive, there is no sign change in interval
    % - If the product is negative, there is a sign change in the interval
    % - Move the Mach number from current value to Mid value if there was
    %    no sign change, because we want to keep bounding the root
    if (fMLo*fMMid > 0)
        MLo = MMid;
    elseif (fMHi*fMMid > 0)
        MHi = MMid;
    end
    
    % Convergence criteria
    if (abs(fMMid-fMLo) <= errTol)
        if (verboseBisection == 1)
            fprintf('Converged after %i iterations\n',i);
            fprintf('Msub: %3.4f\n\n',MMid);
        end
        Msub = MMid;
        break;
    end
    
end

%% SUPERSONIC BISECTION

% Initial Mach number bounds
MLo = 1+1e-6;           % Initial lower bound of Mach number
MHi = 50;               % Initial upper bound of Mach number

iterMax = 100;
for i = 1:1:iterMax
    % Calculate middle Mach number
    MMid = 0.5*(MLo+MHi);
    
    % Evaluate Lo, Mid, and Hi function values
    fMLo  = AM_EQN(MLo,ARatio);
    fMMid = AM_EQN(MMid,ARatio);
    fMHi  = AM_EQN(MHi,ARatio);
    
    % Print iteration to command window
    if (verboseBisection == 1)
        fprintf('fM(%i): %3.4f\t%3.4f\t%3.4f\n',i,fMLo,fMMid,fMHi);
    end
    
    % Update Mach numbers based on sign changes
    % - If the product is positive, there is no sign change in interval
    % - If the product is negative, there is a sign change in the interval
    % - Move the Mach number from current value to Mid value if there was
    %    no sign change, because we want to keep bounding the root
    if (fMLo*fMMid > 0)
        MLo = MMid;
    elseif (fMHi*fMMid > 0)
        MHi = MMid;
    end
    
    % Convergence criteria
    if (abs(fMMid-fMLo) <= errTol)
        if (verboseBisection == 1)
            fprintf('Converged after %i iterations\n',i);
            fprintf('Msub: %3.4f\n\n',MMid);
        end
            Msup = MMid;
        break;
    end
end

% Print bisection method solutions to the command window
fprintf('==== BISECTION SOLVER ====\n');
fprintf('Msub: %3.4f\n',Msub);
fprintf('Msup: %3.4f\n',Msup);
fprintf('==========================\n\n');
