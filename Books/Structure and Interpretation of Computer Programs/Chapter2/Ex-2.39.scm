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

; (op 1 (op 2 (op 3 '()))) 
; (op 1 (op 2 '(3))
; (op 1 '(3 2))
; '(3 2 1)

; (cons 3 (cons 2 (cons 1 '())))

(define (reverse sequence)
    (fold-right (lambda (x y) (if (null? y) (list x) (append y (list x)))) '() sequence))

(define (reverse sequence) 
    (fold-left (lambda (x y) (cons y x)) '() sequence))
