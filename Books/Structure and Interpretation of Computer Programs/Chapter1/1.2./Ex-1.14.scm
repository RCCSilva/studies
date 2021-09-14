(11 5)                                          | 1
(11 4) (-39 5)                                  | 2
(11 3) (-4 4) 0                                 | 3
(11 2) (1 3) 0 0                                | 4
(11 1) (6 2) (1 2) (-9 3) 0 0                   | 5
(11 0) (10 1) (6 1) (1 2) (1 1) (-4 2) 0 0 0    | 9
; ...

; Roughly the algorithm increases in n ^ 2 in number of steps.
; For a sufficiently large n, each node may lead to two more nodes and so on.
; This will eventually stop since some nodes will either reach a value less than 0
; or equal to 0.