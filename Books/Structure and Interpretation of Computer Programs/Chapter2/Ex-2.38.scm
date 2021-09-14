(define (fold-left op initial sequence)
    (define (iter result rest)
        (if (null? rest)
        result
        (iter (op result (car rest)) (cdr rest))))
    (iter initial sequence))

(define (fold-right op initial sequence)
    (if (null? sequence)
        initial
        (op (car sequence)
            (fold-right op initial (cdr sequence)))))

(fold-right / 1 (list 1 2 3))
(fold-left / 1 (list 1 2 3))
(fold-right list '() (list 1 2 3))
(fold-left list '() (list 1 2 3))

;; Looks like that op should no be influenced by the operationd order. It should make no difference
;; if the process starts from the left or from the right. Adding numbers or multiplying numbers for example.

(fold-right + 0 (list 1 2 3))
(fold-left + 0 (list 1 2 3))


(fold-right * 1 (list 1 2 3))
(fold-left * 1 (list 1 2 3))

