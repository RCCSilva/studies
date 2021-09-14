;; func: function => function
;; a: int => Start point
;; b: int => End point
;; n: int => Number of iterations

(define (even? x) (= (remainder x 2) 0))

(define (cube x) (* x x x))

(define (sum term a next b i)
	(if (> a b)
		0
		(+ (term a i) (sum term (next a) next b (+ i 1)))))

;; The term also receives the current index which may be used if 

(define (simpson-rule func a b n)
	(define h (/ (- b a) n))
	(define (snext l) (+ l h))
	(define (ufunc value index)
		(cond ((or (= index 0) (= index b)) (func value))
			  ((even? index) (* 2 (func value)))
			  (else (* 4 (func value)))))

	(* (/ h 3) (sum ufunc a snext b 0)))


; (simpson-rule cube 0 1 100)
; (simpson-rule cube 0 1 1000)