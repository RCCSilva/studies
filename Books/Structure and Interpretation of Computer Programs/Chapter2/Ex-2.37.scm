(define (accumulate op initial sequence)
    (if (null? sequence)
        initial
        (op (car sequence)
            (accumulate op initial (cdr sequence)))))

(define (accumulate-n op init seqs)
(if (null? (car seqs))
    '()
    (cons (accumulate op init (map car seqs))
          (accumulate-n op init (map cdr seqs)))))

(define (dot-product v w)
    (accumulate + 0 (map * v w)))

(define (matrix-*-vector m v)
    (define (accumulate-row row)
        (dot-product row v))
    (map accumulate-row m))

(define (transpose mat)
    (accumulate-n (lambda (this that) (cons this that)) '() mat))

(define (repeat-list input-list n)
    (define (iter response-list i)
        (if (<= i 1)
            response-list
            (iter (append response-list (list input-list)) (- i 1))))
    (iter (list input-list) n))

(define (matrix-*-matrix m n)
    (let ((cols (transpose n)))
        (define (row-by-cols row)
            (map dot-product (repeat-list row (length cols)) cols))
        (map row-by-cols m)))
