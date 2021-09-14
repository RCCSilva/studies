(define (make-interval a b) (cons a b))

(define upper-bound cdr)
(define lower-bound car)

(define (add-interval x y)
    (make-interval (+ (lower-bound x) (lower-bound y))
    (+ (upper-bound x) (upper-bound y))))

(define (sub-interval x y)
    (make-interval (- (lower-bound x) (lower-bound y))
    (- (upper-bound x) (upper-bound y))))

(define (width interval)
    (/ (- (upper-bound interval) (lower-bound interval)) 2))

;; Given, Z + Y = Z. (width Z) + (width Y) = (width Z)

(define x (make-interval 0 10)) ;; width 5

(define y (make-interval 1 7)) ;; width 3

(width (add-interval x y)) ;; width 8

;; Given, Z - Y = Z. (width Z) - (width Y) = (width Z)

(define x (make-interval 0 10)) ;; width 5

(define y (make-interval 1 7)) ;; width 3

(width (sub-interval x y)) ;; width 2