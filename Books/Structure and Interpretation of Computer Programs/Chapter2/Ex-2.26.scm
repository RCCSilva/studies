(define x (list 1 2 3))
(define y (list 4 5 6))

(append x y) ;;  (1 2 3 4 5 6)

;; Since a list is a set of pairs where the ´car of the pair is the value the cdr is the next value (null in the end)
;; `Append` changes the final null value of the first argument to be the second parameter

(cons x y)

;; The first value of this operations has as the first value the list '(1 2 3), but it does not have as the second value a list.
;; Instead the list '(4 5 6) is concatenated in the first level os the data structure.

(list x y)

;; Now, we have a list of lists, where the first and second value of the mother list are lists. 