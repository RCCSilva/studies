(define (new-if predicate then-clause else-clause)
	(cond (predicate then-clause)
		(else else-clause)))

(define (sqrt-iter guess x)
(new-if (good-enough? guess x)
guess
(sqrt-iter (improve guess x) x)))

(define (improve guess x)
(average guess (/ x guess)))

(define (average x y)
(/ (+ x y) 2))

(define (good-enough? guess x)
(< (abs (- (square guess) x)) 0.001))

(define (sqrt x)
(sqrt-iter 1.0 x))

; If we try to use the new-if instead of if the programs chashes.
; Since scheme uses the applicative-order evaluation the parameters of each
; function are evaluated. Thus, when trying (sqrt 9), for example, scheme, first
; passes it to sqrt-iter (sqrt-iter 1.0 9), which uses the new-if. When this last
; function is called, it first evaluates the (good-enough? 1 9) which returns #f,
; then it evaluates (sqrt-iter (improve guess x) x). The issue is that is runs in a
; infinite loop that tries to improve the guess without being stopped by 
; the "good-enough" predicate. 