(define (filtered-accumulate combiner term a next b result filter null-value)
	(define (super-term a) (if (filter a) (term a) null-value)) 
    (if (> a b)
    	result
        (filtered-accumulate combiner term (next a) next b (combiner (super-term a) result) filter null-value)))

(define (square x) (* x x))
(define (inc x) (+ x 1))
(define (even? x) (= (remainder x 2) 0))

(filtered-accumulate + square 1 inc 4 0 even? 0) ; 6

(accumulate + identity 1 (lambda (x) (+ x 1)) 4 0) ; 6