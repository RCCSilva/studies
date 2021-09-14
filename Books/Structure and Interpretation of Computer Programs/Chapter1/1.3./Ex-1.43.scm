(define (repeated proc n)
	(define (iter i inst)
		(if (>= i n)
			inst
			(iter (+ i 1) (lambda (x) (proc (inst x))))))
	(iter 1 proc))

((repeated square 2) 5)
