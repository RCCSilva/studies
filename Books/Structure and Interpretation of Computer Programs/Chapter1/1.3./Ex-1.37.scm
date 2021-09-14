(define (cont-frac n d k)
	(define (iter-frac i)
		(if (> i k)
		0
		(/ (n i) (+ (d i ) (iter-frac (+ i 1))))))
	(iter-frac 1))

(cont-frac (lambda (i) 1.0) (lambda (i) 1.0) 10000)

; (define (cont-frac n d k)
; 	(define (iter-frac i result)
; 		(if (> i k)
; 		result
; 		(iter-frac (+ i 1) (/ result (/ (n i) (d i))))))
; 	(iter-frac 1 0))

; (cont-frac (lambda (i) 1.0) (lambda (i) 1.0) 10000)
