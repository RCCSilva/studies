(define x (list (list 1 2) (list 3 4)))

(define (reverse list-input)
    (define (iter-reverse items answer)
        (if (null? items)
            answer
            (iter-reverse (cdr items) (cons (car items) answer))))
    (iter-reverse list-input '()))

(define (deep-reverse items)
    (define (iter things answer)
        (if (null? things)
            answer
            (iter (cdr things) (cons (reverse (car things)) answer))))
    (iter items '()))