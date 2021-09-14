(define (sqrt-iter old-guess actual-guess x)
(if (good-enough? old-guess actual-guess)
actual-guess
(sqrt-iter actual-guess (improve actual-guess x) x)))

(define (improve guess x)
(average guess (/ x guess)))

(define (average x y)
(/ (+ x y) 2))

(define (good-enough? old-guess actual-guess)
(< (abs (- actual-guess old-guess)) 0.001))

(define (sqrt x)
(sqrt-iter 0.5 1.0 x))

; (sqrt 0.0001) which should had return something close to 0.01, gave 0.03.
; Using the new approach we were able to reach 0.01.