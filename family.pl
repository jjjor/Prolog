% Fatos
pai(joao, maria).
pai(joao, jose).
mae(ana, maria).
mae(ana, jose).

% Regras
irmao(X, Y) :- pai(Z, X), pai(Z, Y), mae(W, X), mae(W, Y), X \= Y.
