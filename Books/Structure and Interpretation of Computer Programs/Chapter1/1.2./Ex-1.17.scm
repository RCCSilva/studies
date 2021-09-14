(define (double x)
	(+ x x))
(define (halve x)
	(/ x 2))

(define (fast-* x y)
	(cond ((= y 1) x)
		  ((even? y) (fast-* (double x) (halve y)))
		  (else (+ x (fast-* x (- y 1))))))