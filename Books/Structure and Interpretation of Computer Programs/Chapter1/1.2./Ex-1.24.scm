(define (expmod base exp m)
	(cond ((= exp 0) 1)
		  ((even? exp)
		  	(remainder 
		  		(square (expmod base (/ exp 2) m))
		  		m))
		  (else
		  	(remainder
		  		(* base (expmod base (- exp 1) m))
		  		m))))

(define (fermat-test n)
	(define (try-it a)
		(= (expmod a n n) a))
	(try-it (+ 1 (random (- n 1)))))

(define (fast-prime? n times)
	(cond ((= times 0) true)
		  ((fermat-test n) (fast-prime? n (- times 1)))
		  (else false)))

(define (timed-prime-test n)
	(newline)
	(display n)
	(start-prime-test n (runtime))
	)

(define (start-prime-test n start-time)
	(if (fast-prime? n 100) (report-prime n (- (runtime) start-time)) 0))

(define (report-prime n elapsed-time)
	(newline)
	(display n)
	(display " *** ")
	(display elapsed-time)
	1)

(define (search-for-primes n count)
	(if (< count 3) (search-for-primes (+ n 2) (+ count (start-prime-test n (runtime))))))

; (search-for-primes 10000000000001 0)

;10000000000037 *** .02
; 10000000000051 *** 9.999999999999998e-3
; 10000000000099 *** 0.

; (search-for-primes 100000000000001 0)

; 100000000000031 *** 1.0000000000000002e-2
; 100000000000067 *** 9.999999999999995e-3
; 100000000000097 *** 1.0000000000000009e-2

; (search-for-primes 1000000000000001 0)

; 1000000000000037 *** 9.999999999999995e-3
; 1000000000000091 *** 0.
; 1000000000000159 *** 2.0000000000000004e-2
