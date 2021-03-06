(define (square x) (* x x))



(define (tree-map proc tree)
    (map (lambda (subtree)
                 (if (pair? subtree)
                     (tree-map proc subtree)
                     (proc subtree)))
    tree))

(define (square-tree tree)
    (tree-map square tree))