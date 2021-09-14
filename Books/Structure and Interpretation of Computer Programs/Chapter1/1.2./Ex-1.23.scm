(define (smallest-divisor n) (find-divisor n 2))

(define (next x) (if (= x 2) 3 (+ x 2)))

(define (find-divisor n test-divisor)
	(cond ((> (square test-divisor) n) n)
		  ((divides? test-divisor n) test-divisor)
		  (else (find-divisor n (next test-divisor)))))

(define (divides? a b) (= (remainder b a) 0))

(define (prime? n) (= (smallest-divisor n) n))

(define (timed-prime-test n)
	(newline)
	(display n)
	(start-prime-test n (runtime))
	)

(define (start-prime-test n start-time)
	(if (prime? n) (report-prime n (- (runtime) start-time)) 0))

(define (report-prime n elapsed-time)
	(newline)
	(display n)
	(display " *** ")
	(display elapsed-time)
	1)

(define (search-for-primes n count)
	(if (< count 3) (search-for-primes (+ n 2) (+ count (start-prime-test n (runtime))))))

; (search-for-primes 10000000000001 0)

; 10000000000037 *** 1.6
; 10000000000051 *** 1.5500000000000003
; 10000000000099 *** 1.5500000000000007

; (search-for-primes 100000000000001 0)

; 100000000000031 *** 4.96
; 100000000000067 *** 5.1
; 100000000000097 *** 5.000000000000002

; (search-for-primes 1000000000000001 0)

; 1000000000000037 *** 17.729999999999997
; 1000000000000091 *** 16.97
; 1000000000000159 *** 16.17

