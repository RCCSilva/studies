; Fibonacci procedure using onely computed values

(define phi (/ (+ 1 (sqrt 5)) 2))

(define psi (/ (- 1 (sqrt 5)) 2))

; n ^ x
(define (new-exp n x)
	(if (= x 0) 1
		(* n (new-exp n (- x 1)))))

(define (new-fib n)
	(floor ( / (- (new-exp phi n) (new-exp psi n)) (sqrt 5))))

; Recursive procedure for Fibonacci

(define (fib n)
	(cond ((= n 0) 0)
		  ((= n 1) 1)
		  (else (+ (fib (- n 1)) (fib (- n 2))))))

; Testing if the results are equal

(define (fib-equal? n)
	(if (= (fib n) (new-fib n)) 1 0))