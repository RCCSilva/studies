(define (average x y) (/ (+ x y) 2))

(define (fixed-point f first-guess)
	(define (close-enough? v1 v2)
		(< (abs (- v2 v1)) 0.00001))
	(define (try guess)
		(display guess)
		(newline)
		(let ((next (f guess)))
			(if (close-enough? guess next)
				guess
				(try next))))
	(try first-guess))


(fixed-point (lambda (x) (+ 1 (/ 1 x))) 1)
