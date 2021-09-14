(define (cube x) (iter-cube 0.5 1.0 x))

(define (iter-cube old-guess actual-guess x)
	(if (good-enough? old-guess actual-guess)
		actual-guess
		(iter-cube actual-guess (improve actual-guess x) x)))

(define (improve actual-guess x)
	(/ 
		(+ 
			(/ x 
				(* actual-guess actual-guess))
			(+ actual-guess actual-guess))
		3))

(define (good-enough? old-guess actual-guess)
	(< (abs (- actual-guess old-guess)) 0.001))