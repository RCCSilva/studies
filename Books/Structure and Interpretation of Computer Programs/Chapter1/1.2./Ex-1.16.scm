(define (fast-exp a b n)
	(cond ((= n 0) a)
		  ((= n 2) (fast-exp (* a (square b)) b (- n 2)))
		  ((even? n) (fast-exp (* a (square b)) b (/ n 2)))
		  (else (fast-exp (* a b) b (- n 1)))))

(define (even? b)
	(= (remainder b 2) 0))