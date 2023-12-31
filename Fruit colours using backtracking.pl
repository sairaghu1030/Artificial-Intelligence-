% Define facts about fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(watermelon, green).

% Define a predicate to query the color of a fruit
color_of_fruit(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Querying for all fruits and their colors using backtracking
% This will backtrack through all available fruits and their colors
?- color_of_fruit(Fruit, Color), write('The color of '), write(Fruit), write(' is '), write(Color), nl, fail.
