(define (make-interval a b) (cons a b))

(define upper-bound cdr)
(define lower-bound car)

(define (add-interval x y)
    (make-interval (+ (lower-bound x) (lower-bound y))
    (+ (upper-bound x) (upper-bound y))))

(define (add-interval x y)
    (make-interval (- (lower-bound x) (lower-bound y))
    (- (upper-bound x) (upper-bound y))))

