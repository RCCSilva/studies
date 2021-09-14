(define (cont-frac n d k)
	(define (iter-frac i)
		(if (> i k)
		0
		(/ (n i) (- (d i ) (iter-frac (+ i 1))))))
	(iter-frac 1))

(define (tan-cf x k)
	(define (tan-new-n j)
		(if (= j 1) x (* x x)))

	(define (tan-new-d j) (- (+ j j) 1))

	(cont-frac tan-new-n tan-new-d k))

(tan-cf 2 100)