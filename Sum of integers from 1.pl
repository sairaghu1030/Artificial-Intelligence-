% Base case: Sum of integers from 1 to 1 is 1
sum_integers(1, 1).

% Recursive case: Calculate sum of integers from 1 to N
% by reducing the problem to sum_integers(N-1, SumNMinus1)
% and then adding N to SumNMinus1
sum_integers(N, Sum) :-
    N > 1,            % Ensure N is greater than 1
    N1 is N - 1,      % Calculate N-1
    sum_integers(N1, SumNMinus1),  % Calculate sum from 1 to N-1
    Sum is SumNMinus1 + N.  % Calculate sum from 1 to N

% Example usage:
% To find the sum of integers from 1 to 5:
% ?- sum_integers(5, Result).
% Result = 15