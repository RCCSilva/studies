(define (accumulate combiner null-value term a next b)
    (if (> a b)
        null-value
        (combiner (term a) (accumulate combiner null-value term (next a) next b))))

(accumulate * 1 identity 1 (lambda (x) (+ x 1)) 3) ; 6
(accumulate + 0 identity 1 (lambda (x) (+ x 1)) 4) ; 6


(define (accumulate combiner term a next b result)
    (if (> a b)
        result
        (accumulate combiner term (next a) next b (combiner (term a) result) )))

(accumulate * identity 1 (lambda (x) (+ x 1)) 3 1) ; 6
(accumulate + identity 1 (lambda (x) (+ x 1)) 4 0) ; 6