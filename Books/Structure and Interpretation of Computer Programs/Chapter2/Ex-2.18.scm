(define (reverse list-input)
    (define (iter-reverse items answer)
        (if (null? items)
            answer
            (iter-reverse (cdr items) (cons (car items) answer))))
    (iter-reverse list-input '()))


(reverse (list 1 2 3 4 5))

(reverse (list 5 4 3 2 1))

