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

(define (fermat-test n a)
	(if (= (expmod a n n) a) 0 1))

(define (iter-carmechiel-test n a fails-count)
	(if (> a 0) (iter-carmechiel-test n (- a 1) (fermat-test n a)) fails-count))

(define (carmechiel-test n)
	(iter-carmechiel-test n (- n 1) 0))

; carmechiel-test procedure should return 0 if the number n passes in all a < n fermat-test

; (carmechiel-test 561)
; (carmechiel-test 1105)
; (carmechiel-test 1729)
; (carmechiel-test 2465)
; (carmechiel-test 2821)
; (carmechiel-test 6601)

; All carmechiel numbers return 0. Hence, in the eyes of the fermat-test they are prime numbers.