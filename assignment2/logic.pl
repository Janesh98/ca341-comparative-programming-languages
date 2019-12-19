% converts string to list of characters e.g. "test" = [t, e, s, t]
:- set_prolog_flag(double_quotes, chars).

lcp(L, P) :-
    prefixes(L, X),          % creates a list of possible prefixes
    pop(X, LCP),             % gets last element
    atom_chars(P, LCP),      % converts list to string e.g. [t, e, s, t] = "test"
    !.                       % ! is a cut which stops backtracking, in this case it halts the program.

prefixes(L,Prefixes) :-
    findall(P, check(P, L), Prefixes).

check(P, L) :-
    maplist(add(P), L).

add(P, L) :-
    append(P, _, L).

pop([Prefix], Prefix) :- !.     % iterates through list of lists stopping when
pop([_|T], Prefix) :-           % there is only 1 element remaing, the last element
    pop(T, Prefix).