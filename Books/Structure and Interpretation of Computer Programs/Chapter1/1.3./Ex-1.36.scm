(define (fixed-point f first-guess)
	(define (close-enough? v1 v2)
		(< (abs (- v2 v1)) 0.00001))
	(define (try guess)
		(let ((next (f guess)))
			(if (close-enough? guess next)
				guess
				(try next))))
	(try first-guess))

(fixed-point (lambda (x) (/ (log 1000) (log x))) 2) ; 33 iterations

(fixed-point (lambda (x) (average x (/ (log 1000) (log x)))) 2) ; 8 iterations
