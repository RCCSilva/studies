(define (fixed-point f first-guess)
	(define (close-enough? v1 v2)
		(< (abs (- v2 v1)) 0.00001))
	(define (try guess)
		(let ((next (f guess)))
			(if (close-enough? guess next)
				guess
				(try next))))
	(try first-guess))

(define (average v1 v2) (/ (+ v1 v2) 2))

(define (average-damp f)
	(lambda (x) (average x (f x))))

(fixed-point (average-damp (average-damp (lambda (y) (/ 4 (* y y y y y y))))) 1.0)