(define (fringe x)
    (cond ((not (pair? x)) (list x))
          ((null? (cdr x)) (fringe (car x)))
          (else (append (fringe (car x)) (fringe (cdr x))))))
    