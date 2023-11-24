% Rules for moving disks between towers
move(1,X,Y,_) :-
    write('Move disk from '), write(X), write(' to '), write(Y), nl.
move(N,X,Y,Z) :-
    N > 1,
    M is N-1,
    move(M,X,Z,Y),
    move(1,X,Y,_),
    move(M,Z,Y,X).

% Rule to solve Towers of Hanoi for N disks
hanoi(N) :-
    move(N,'A','B','C').

% Example usage:
% To solve Towers of Hanoi for 3 disks:
% ?- hanoi(3).
