% Facts representing information about planets
planet(mercury, rocky, small, 0.39).
planet(venus, rocky, medium, 0.72).
planet(earth, rocky, medium, 1.0).
planet(mars, rocky, small, 1.52).
planet(jupiter, gas_giant, large, 5.2).
planet(saturn, gas_giant, large, 9.5).
planet(uranus, ice_giant, medium, 19.2).
planet(neptune, ice_giant, medium, 30.1).
planet(pluto, dwarf, small, 39.5).

% Rule to retrieve and display information about all planets
all_planets_info :-
    planet(Planet, Type, Size, Distance),
    format('Planet: ~w, Type: ~w, Size: ~w, Distance: ~w AU~n', [Planet, Type, Size, Distance]),
    fail.
all_planets_info.

% Example usage:
% To retrieve and display information about all planets:
% ?- all_planets_info.
