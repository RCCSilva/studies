(define (make-interval a b) (cons a b))

(define upper-bound cdr)
(define lower-bound car)

(define (mul-interval x y)
    (let ((p1 (* (lower-bound x) (lower-bound y)))
    (p2 (* (lower-bound x) (upper-bound y)))
    (p3 (* (upper-bound x) (lower-bound y)))
    (p4 (* (upper-bound x) (upper-bound y))))
    (make-interval (min p1 p2 p3 p4)
    (max p1 p2 p3 p4))))


(define (div-interval x y)
    (if (or (= (upper-bound y) 0) (= (lower-bound y) 0))
        (error "Interval Y has either lower bound or upper bound equal to 0.")
    (mul-interval 
        x
        (make-interval (/ 1.0 (upper-bound y))
                       (/ 1.0 (lower-bound y))))))