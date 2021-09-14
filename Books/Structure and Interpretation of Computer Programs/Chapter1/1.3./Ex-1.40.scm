(define dx 0.0000001)

(define (deriv g) (lambda (x) (/ (- (g (+ x dx)) (g x)) dx)))

(define (newtown-transform g)
	(lambda (x) (- x (/ (g x) ((deriv g) x)))))

(define (fixed-point f first-guess)
	(define (close-enough? v1 v2)
		(< (abs (- v2 v1)) 0.00001))
	(define (try guess)
		(let ((next (f guess)))
			(if (close-enough? guess next)
				guess
				(try next))))
	(try first-guess))

(define (newtowns-method g guess)
	(fixed-point (newtown-transform g) guess))

(define (square x) ( * x x))
(define (cube x) (* x x x))

(define (cubic a b c)
	(lambda (x) (+ (cube x) (* a (square x)) (* b x) c)))

(newtowns-method (cubic 1 2 3) 1)