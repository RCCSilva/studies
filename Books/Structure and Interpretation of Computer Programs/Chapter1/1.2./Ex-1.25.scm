; Not working
(define (fast-exp b n)
	()
	(cond ((= n 0) 1)
		  ((even? n) (square (fast-exp b (/ n 2))))
		  (else (* b (fast-exp b (- n 1))))))

(define (even? x) (= (remainder x 2) 0))

(define (expmod base exp m)
	(remainder (fast-exp base exp) m))

(define (fermat-test n)
	(define (try-it a)
		(= (expmod a n n) a))
	(try-it (+ 1 (random (- n 1)))))

(define (fast-prime? n times)
	(display n)
	(cond ((= times 0) true)
		  ((fermat-test n) (fast-prime? n (- times 1)) )
		  (else false)))

(define (start-prime-test n start-time)
	(if (fast-prime? n 100) (report-prime n (- (runtime) start-time)) 0))

(define (report-prime n elapsed-time)
	(newline)
	(display n)
	(display " *** ")
	(display elapsed-time)
	1)

(define (search-for-primes n count)
	(display n)
	(if (< count 3) (search-for-primes (+ n 2) (+ count (start-prime-test n (runtime))))))

; (search-for-primes 10000000000001 0)

;10000000000037 *** .02
; 10000000000051 *** 9.999999999999998e-3
; 10000000000099 *** 0.
