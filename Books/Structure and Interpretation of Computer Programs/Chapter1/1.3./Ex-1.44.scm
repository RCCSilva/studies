(define (repeated proc n)
	(define (iter i inst)
		(if (>= i n)
			inst
			(iter (+ i 1) (lambda (x) (proc (inst x))))))
	(iter 1 proc))

(define (smooth f)
	(let ((dx 0.00001))
		(lambda (x) (/ (+ (f (- x dx)) (f x) (f (+ x dx))) 3) )))

(define (repeated-smooth f n)
	((repeated smooth n) f))

((repeated-smooth square 2) 2)