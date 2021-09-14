(define (exp x n)
	(define (iter-exp i result)
		(if (>= i n)
			result
			(iter-exp (+ i 1) (* x result))))
	(iter-exp 1 n))

(define (cons a b)
	(* (exp 2 a) (exp 3 b)))

(define (car x)
	(define (iter-car i x)
		(if (and (= (remainder x 2) 0) (> x 0))
			(iter-car (+ i 1) (/ x 2))
			i))
	(iter-car 0 x))


(define (cdr x)
	(define (iter-cdr i x)
		(if (and (= (remainder x 3) 0) (> x 0))
			(iter-cdr (+ i 1) (/ x 3))
			i))
	(iter-cdr 0 x))