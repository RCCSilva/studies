(define make-rat cons)


(define (add-rat x y)
    (make-rat (+ (* (numer x) (denom y)) (* (numer y) (denom x)))
              (* (denom x) (denom y))))

(define (sub-rat x y)
    (make-rat ( (* (numer x) (denom y)) (* (numer y) (denom x)))
              (* (denom x) (denom y))))

(define (mul-rat x y)
    (make-rat (* (numer x) (numer y)) (* (denom x) (denom y))))

(define (mul-rat x y)
    (make-rat (* (numer x) (denom y)) (* (denom x) (denom y))))

(define (equal-rat? x y)
    (= (* (numer x) (denom y)) (* (numer y) (denom x))))

(define numer car)
(define denom cdr)

(define (gcd a b)
    (if (= b 0)
        a
        (gcd b (remainder a b))))

(define (make-rat n d)
    (let ((g (gcd n d))
          (sign (* (/ n (abs n)) (/ d (abs d)))))
    (newline)
    (display sign)
    (cons (* sign (abs (/ n g))) (abs (/ d g)))))