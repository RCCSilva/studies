(define (identity x i) x)

(define (product a b nexta nextb i max-i)
	(display (/ a b))
	(if (> i max-i)
	1
	(* (/ a b) (product (nexta a i) (nextb b i) nexta nextb (+ i 1) max-i))
	)
)

(= (product 1 1 identity identity 1 10) 1)

(= (product 3 1 identity identity 1 3) 27)

(define (even? x) (= (remainder x 2) 0))

(define (product a b nexta nextb max-i)
    (define (iter-product a b result i)
        (display a)
        (newline)
        (display b)
        (newline)
        (newline)
        (if (> i max-i)
            result
            (iter-product (nexta a i) (nextb b i) (* result (/ a b)) (+ i 1))))
    (iter-product a b 1 1))

(= (product 1 1 identity identity 10) 1)
(= (product 3 1 identity identity 3) 27)

(define (my-next-a x i)
    (if (even? i) x (+ x 2)))

(define (my-next-b x i)
    (if (even? i) (+ x 2) x))

(define (aprox-pi n)
    (product 2 3 my-next-a my-next-b n))