(define (accumulate op initial sequence)
    (if (null? sequence)
        initial
        (op (car sequence)
            (accumulate op initial (cdr sequence)))))

(define (count-leaves t)
    (accumulate (lambda (this that)
                        (newline)
                        (display this)
                        (if (not (list? this))
                            (+ 1 that)
                            (+ (count-leaves this) that))) 0 t))