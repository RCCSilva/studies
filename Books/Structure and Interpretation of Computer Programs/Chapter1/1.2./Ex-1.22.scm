(define (smallest-divisor n) (find-divisor n 2))

(define (find-divisor n test-divisor)
	(cond ((> (square test-divisor) n) n)
		  ((divides? test-divisor n) test-divisor)
		  (else (find-divisor n (+ test-divisor 1)))))

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

; 10000000000037 *** 2.54
; 10000000000051 *** 2.54
; 10000000000099 *** 2.5

; (search-for-primes 100000000000001 0)

; 100000000000031 *** 7.83
; 100000000000067 *** 7.950000000000003
; 100000000000097 *** 7.850000000000001

; (search-for-primes 1000000000000001 0)

; 1000000000000037 *** 26.97
; 1000000000000091 *** 26.799999999999997
; 1000000000000159 *** 27.04000000000002

; 2.5 -> 7.8 -> 26.9

; 2.5 * (sqrt 10) = 7.9

; 7.9 * (sqrt 10) = 25

; The computing time seems to grow in a O((sqrt x))