(quote (quote abracadabra))
''abracadabra

; Both of these expressions return the same result

;"e quotation mark is just a single-character abbreviation for
;  wrapping the next complete expression with quote to form (quote ⟨ expression ⟩)"

; As explained by the authors, the ' works as an abbreviation for "(quote <expression>)"
; Given that, and the applicative order evaluation (in -> out), the expression gets first 
; transformed to '(quote abracadabra). After that, we get (quote (quote abracadabra)).
; Finally, the outside function gets evatualted and it transforms (quote abracadabra)