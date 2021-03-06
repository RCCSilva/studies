(define (gcd a b)
	(if (= b 0)
	a
	(gcd b (remainder a b))))

; Normal-order evaluation
; 1
(gcd 206 40)

; 2
(gcd 40 (remainder 206 40))
	(if (= (remainder 206 40) 0) ; 6 = 0?
	(gcd (remainder 206 40) (remainder 40 (remainder 206 40)))

; 3
(gcd (remainder 206 40) (remainder 40 (remainder 206 40)))
	(if (= (remainder 40 (remainder 206 40)) 0) ; 6 = 0?
	(gcd (remainder 40 (remainder 206 40)) (remainder (remainder 206 40) (remainder 40 (remainder 206 40)))

(gcd (remainder 40 (remainder 206 40)) (remainder (remainder 206 40) (remainder 40 (remainder 206 40)))
	(if (= (remainder (remainder 206 40) (remainder 40 (remainder 206 40))) 0) ; 2 = 0?
	(gcd (remainder (remainder 206 40) (remainder 40 (remainder 206 40)) 
		 (remainder (remainder 40 (remainder 206 40)) (remainder (remainder 206 40) (remainder 40 (remainder 206 40)))

(gcd (remainder (remainder 206 40) (remainder 40 (remainder 206 40)) 
	 (remainder (remainder 40 (remainder 206 40)) (remainder (remainder 206 40) (remainder 40 (remainder 206 40)))

	 (if (= (remainder (remainder 40 (remainder 206 40)) (remainder (remainder 206 40) (remainder 40 (remainder 206 40)))) 0)
	 	(remainder (remainder 206 40) (remainder 40 (remainder 206 40)) 

; Considering that if always evaluates the predicate first, there are 14 evaluations of "remainder" in 
; the predicate form and 4 in the reduction form

; Applicative-order evaluation
(gcd 206 40)
(gcd 40 (remainder 206 40))
(gcd 40 6)
(gcd 6 (remainder 40 6))
(gcd 6 4)
(gcd 4 (remainder 6 4))
(gcd 4 2)
(gcd 2 (remainder 4 2))
(gcd 2 0)
2