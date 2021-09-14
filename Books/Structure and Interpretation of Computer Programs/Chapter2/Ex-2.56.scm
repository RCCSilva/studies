(define (variable? x) (symbol? x))
(define (same-variable? v1 v2) (and (variable? v1) (variable? v2) (eq? v1 v2)))
(define (sum? e) (and (pair? e) (eq? (car e) '+)))
(define (addend e) (cadr e))
(define (augend e) (caddr e))

;; Exponentiation
(define (exponentiation? e) (eq? (car e) '**))
(define (base e) (cadr e))
(define (exponent e) (cadr (cdr e)))
(define (make-exponentiation a b)
    (cond ((eq? b '0) 1)
          ((eq? b '1) a)
          (else (list '** a b))))

;; Sum

(define (=number? exp num) (and (number? exp) (= exp num)))
(define (make-sum a1 a2) 
    (cond ((=number? a1 0) a2)
          ((=number? a2 0) a1)
          ((and (number? a1) (number? a2)) (+ a1 a2))
          (else (list '+ a1 a2))))

;; Product
(define (product? e) (and (pair? e) (eq? (car e) '*)))
(define (multiplier e) (cadr e))
(define (multiplicand e) (caddr e))
(define (make-product m1 m2)
    (cond ((or (=number? m1 0) (=number? m2 0)) 0)
          ((=number? m1 1) m2)
          ((=number? m2 1) m1)
          ((and (number? m1) (number? m2)) (* m1 m2))
          (else (list '* m1 m2))))
            

(define (deriv exp var)
    (cond 
        ((number? exp) 0)
        ((variable? exp) (if (same-variable? exp var) 1 0))
        ((sum? exp) (make-sum (deriv (addend exp) var) (deriv (augend exp) var)))
        ((product? exp) (make-sum (make-product (multiplier exp) (deriv (multiplicand exp) var))
                                  (make-product (multiplicand exp) (deriv (multiplier exp) var))))
        ((exponentiation? exp)  (make-product
                                    (make-exponentiation 
                                      (make-product (base exp) (exponent exp))
                                      (make-sum (exponent exp) '-1))
                                    (deriv (base exp) var)))
        (else (error "UNKOWN expression type: DERIV" exp))))