(define (square x) (* x x))

(define (square-map proc tree)
    (map (lambda (subtree)
                 (if (pair? subtree)
                     (tree-map subtree)
                     (square subtree)))
    tree))