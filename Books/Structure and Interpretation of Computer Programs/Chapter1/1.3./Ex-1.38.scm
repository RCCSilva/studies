(define (cont-frac n d k)
	(define (iter-frac i)
		(if (> i k)
		0
		(/ (n i) (+ (d i ) (iter-frac (+ i 1))))))
	(iter-frac 1))

(define (use? x) (= (remainder (- x 2) 3) 0))

(define (new-d x)
	(cond ((= x 1) 1)
		  ((= x 2) 2)
		  ((use? x) (- x (/ (- x 1) 3) 2))
		  (else 1)))
	

(cont-frac (lambda (i) 1.0) new-d 10000) ; .721597