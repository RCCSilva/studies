(define (double x)
	(+ x x))

(define (halve x)
	(/ x 2))

(define (new-* a b)
	(iter 0 a b))

(define (iter a b c)
	(cond ((= c 1) (+ a b))
		  ((even? c) (iter a (double b) (halve c)))
		  (else (iter (+ a b) b (- c 1)))))