(define (last-pair pair)
    (if (null? (cdr pair))
        (car pair)
        (last-pair (cdr pair))))

(last-pair (list 1 2 3 4 5))

(last-pair (list 5 4 3 2 1))

(last-pair (list -2 10 -99 10020 -9))