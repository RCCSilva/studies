(define zero (lambda (f) (lambda (x) x)))

(define (add-1 n)
	(lambda (f) (lambda (x) (f ((n f) x)))))

(add-1 zero)

((lambda (f) (lambda (x) (f ((n f) x)))) zero)

(lambda (f) (lambda (x) (f ((zero f) x))))
(lambda (f) (lambda (x) (f (f x))))
