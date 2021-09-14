(define (A x y)
	(cond ((= y 0) 0)
		((= x 0) (* 2 y))
		((= y 1) 2)
		(else (A (- x 1) (A x (- y 1))))))

(define (f n) (A 0 n)) ; f(n) = 2*n

(define (g n) (A 1 n)) ; g(n) = 2^n

; $ g(n) = 2^n $
; Trying with (A 1 2)
; (A 1 2)
; (A 0 (A 1 1))
; (A 0 2)
; 4

; Trying with (A 1 3)
; (A 1 3)
; (A 0 (A 1 2))
; (A 0 (A 0 (A 1 1)))
; (A 0 (A 0 2))
; (A 0 4)
; 8

(define (h n) (A 2 n)) ; 2 * (n...)

(A 2 2)
(A 1 (A 2 1))
(A 1 2)
(A 0 (A 1 1))
4

; Looks like that the resulte will be something X multiplied by 2, since
; it will always end with (A 1 ...) which gives us 2 * y
; 

(define (k n) (* 5 n n)) ; k(n) = 2n^2