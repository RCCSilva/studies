(define (expmod base exp m)
	(cond ((= exp 0) 1
		  ((even? exp)
		  	(remainder (* (expmod base (/ exp 2) m)
		  		          (expmod base (/ exp 2) m))
		  	m ))
		  (else
		  	(remainder (* base (expmod base (- exp 1) m)) m ))
		  )
	)
	)

(expmod 10 4 2)
(remainder (* (expmod 10 2 2) (expmod 10 2 2)))
(remainder (* ( * (expmod 10 1 2) (expmod 10 1 2)) ( * (expmod 10 1 2) (expmod 10 1 2))))

; As we can see, written like that, expmod procedure doubles the number of expmod calls by each step
; That would give us a n^2 order of growth algorithm if it wasn't for the (/ exp 2) which halves the
; the number os steps required. Hence, Louis anulates the advantages of having the exponent

(expmod 10 4 2)
(remainder (square (expmod (10 2 2))))
(remainder (square (square (expmod (10 2 1))))

; When the algorithm uses the square procedure, expmod can be called only once at each iteration.